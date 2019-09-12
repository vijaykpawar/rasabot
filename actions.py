# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
import requests, json
from typing import Any, Text, Dict, List

from docutils.utils.math.latex2mathml import mspace
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionWeather(Action):

    def name(self):
        return "get_currency"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) :
        ent_list = tracker.latest_message['entities']
        ent = ""
        if len(ent_list) != 0:
            ent = ent_list[0]['value']
        base_url = "https://api.exchangeratesapi.io/latest?"
        complete_url = base_url + "&base=USD"
        print("User wants base currency as "+complete_url)
        response = requests.get(complete_url)
        x = response.json()
        msg = " Source : European Central Bank "
        fx_rate = ""
        if x["rates"] != "error" and ent is not None and ent != "":
            #if x[rates]
            message = x["rates"]
            for key, value in message.items():
                if key == ent.upper():
                    fx_rate = str(value)
                    msg = msg + str(key) + "/USD" + " " + str(value) + ""

        else:
            msg = "Currency FX rate not found"
        print("inside action currency is entity is  ::"+str(ent))
        res = {"message": msg, "fxRateControl": fx_rate, "formCode": "A2"}
        dispatcher.utter_custom_json(res)

        return []


class ActionTrends(Action):

    def name(self):
        return "get_trends"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) :
        ent_list = tracker.latest_message['entities']
        ent = ""
        if len(ent_list) != 0:
            ent = ent_list[0]['value']

        msg = "getting  trends from db"
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        tera_db = client["tera"]
        intents = tera_db["intents"]
        from bson.son import SON
        group_query = [{"$group": {"_id": "$name", "count": {"$sum": 1}}}, {"$sort": SON([("count", -1), ("_id", -1)])},
                       {"$limit": 3}]
        trends = []
        group_by_results = intents.aggregate(group_query)
        for cursor in group_by_results:
            res = intents.find({"name": cursor.get("_id")}).sort("confidence", -1).limit(1)
            trends.append(res[0].get("text"))

        msg = {"message": "Top 3 most asked Questions: ", "showTrends": "true",
               "valueOfResponse": trends};
        dispatcher.utter_custom_json(msg)

        return []


import pymongo
class ActionSaveTrends(Action):
    def name(self):
        return "save_trends"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) :
        ent_list = tracker.latest_message['entities']
        ent = ""

        s = tracker.latest_message

        if len(ent_list) != 0:
            ent = ent_list[0]['value']

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["tera"]
        mycol = mydb["intents"]
        print(s.get("intent"))
        intent = s.get("intent")
        intent["text"]=s.get("text")
        x = mycol.insert_one(intent)
        print("saved latest message")

        #dispatcher.utter_message(str(msg))

        return []



class ActionSaveTrends(Action):
    def name(self):
        return "code_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) :
        ent_list = tracker.latest_message['entities']
        ent = ""
        if len(ent_list) != 0:
            ent = ent_list[0]['value']
        print("Inside code action")
        msg = {"message":"Please fill purpose code S321","purposeCodeControl":"S321","formCode":"A2"}
        dispatcher.utter_custom_json(msg)
        return []
