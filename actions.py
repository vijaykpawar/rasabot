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
        msg = " Source : European Central Bank <br>"
        if x["rates"] != "error":
            #if x[rates]
            message = x["rates"]
            for key, value in message.items():
                msg = msg + str(key) + " " + str(value) + "<br>"
        else:
            msg = "Currency FX rate not found"
        print("inside action currency is entity is  ::"+str(ent))
        dispatcher.utter_message(str(msg))

        return []
