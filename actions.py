# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
import requests, json
from typing import Any, Text, Dict, List

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
        if x["rates"] != "error" and ent is not None:
            #if x[rates]
            message = x["rates"]
            for key, value in message.items():
                if key == ent.upper():
                    msg = msg + str(key) + " " + str(value) + ""

        else:
            msg = "Currency FX rate not found"
        print("inside action currency is entity is  ::"+str(ent))
        dispatcher.utter_message(str(msg))

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

        msg="getting  trends from db"
        dispatcher.utter_message(str(msg))

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
        #print(s)


        if len(ent_list) != 0:
            ent = ent_list[0]['value']

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["tera"]
        mycol = mydb["intents"]
        print(s.get("intent"))
        x = mycol.insert_one(s.get("intent"))
        print("saved latest message")


        #dispatcher.utter_message(str(msg))

        return []
