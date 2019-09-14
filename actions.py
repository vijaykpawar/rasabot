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
        msg = ""
        fx_rate = ""
        if x["rates"] != "error" and ent is not None and ent != "":
            #if x[rates]
            message = x["rates"]
            for key, value in message.items():
                if key == ent.upper():
                    fx_rate = str(value)
                    msg = msg + str(key) + "/USD" + " " + str(value) + ""
                    msg = msg +"( Source : European Central Bank )"

        else:
            msg = "Currency FX rate not found"
        print("inside action currency is entity is  ::"+str(ent))
        res = {"message": msg, "fxRateControl": fx_rate, "canfill":"true"}
        dispatcher.utter_custom_json(res)
        msg = "Also for fx rate refer <a href=\"https://www.gbm.hsbc.com/evolve/overview/\" target=\"_blank\">HSBC evolve</a>"
        dispatcher.utter_message(msg)

        return []


class ActionGetTrends(Action):

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

        msg = {"message": "People also asked : ", "showTrends": "true",
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


class ActionCodeAction(Action):
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
        msg = {"message":"Please fill purpose code S0603","purposeCodeControl":"S0603","purposeCodeDesc":"Transfer for general insurance premium including reinsurance premium; and term life insurance premium","canfill":"true"}
        dispatcher.utter_custom_json(msg)
        return []


class ActionSendA2Form(Action):
    def name(self):
        return "send_form_a2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) :
        print("Inside get a2 form action")
        msg = {"message":"Here you go","formCode":"A2"}
        dispatcher.utter_custom_json(msg)
        return []


class ActionSendA2FormData(Action):
    def name(self):
        return "send_form_a2_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) :
        print("Inside get a2 form action get data ")
        msg = {"message":"Here you go","formCode":"A2"}
        dispatcher.utter_custom_json(msg)
        return []

class ActionSaveA2FormData(Action):
    def name(self):
        return "save_form_a2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) :
        print("Inside get a2 form save  data ")
        print(str(tracker.__dict__))
        dispatcher.utter_message("Saved draft successfully")
        #dispatcher.utter_custom_json(msg)
        return []