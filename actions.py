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
        res= ""
        fx_rate = ""
        if x["rates"] != "error" and ent is not None and ent != "":
            #if x[rates]
            message = x["rates"]
            for key, value in message.items():
                if key == ent.upper():
                    fx_rate = str(value)
                    msg = msg + str(key) + "/USD" + " " + str(value) + ""
                    msg = msg +"( Source : European Central Bank )"
                    res = {"message": msg, "fxRateControl": fx_rate, "canfill": "true"}
        else:
            msg = "Please enter quote currency"
            res = {"message": msg}
        print("inside action currency is entity is  ::"+str(ent))

        dispatcher.utter_custom_json(res)
        if ent is not None and ent != "":
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


class ActionCodeInvestmentBankingAction(Action):
    def name(self):
        return "code_investment_banking"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) :
        ent_list = tracker.latest_message['entities']
        ent = ""
        if len(ent_list) != 0:
            ent = ent_list[0]['value']
        print("Inside code action")
        msg = {"message":"Please fill purpose code S0702","purposeCodeControl":"S0702","purposeCodeDesc":"Investment banking – brokerage, under writing commission etc","canfill":"true"}
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
        msg = {"message": "Here you go", "purposeCodeControl": "S0603",
               "purposeCodeDesc": "Transfer for general insurance premium including reinsurance premium; and term life insurance premium",
               "fxRateControl": "72.123",
               "nameControl":"Mr Vikram ",
               "panControl":"BFBEE56GT1",
               "canfill": "true"
               }
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


class ActionDefaultAskAffirmation(Action):
   """Asks for an affirmation of the intent if NLU threshold is not met."""

   def name(self):
       return "action_default_ask_affirmation"


   def run(self, dispatcher, tracker, domain):
       # get the most likely intent
       last_intent_name = tracker.latest_message['intent']['name']
       print(str(tracker.__dict__))


       # get the prompt for the intent
       intent_prompt = ""
       #self.intent_mappings[last_intent_name]

       # Create the affirmation message and add two buttons to it.
       # Use '/<intent_name>' as payload to directly trigger '<intent_name>'
       # when the button is clicked.
       #message = "Did you mean '{}'?".format(intent_prompt)
       #buttons = [{'title': 'Yes',
       #            'payload': '/{}'.format(last_intent_name)},
       #           {'title': 'No',
       #            'payload': '/out_of_scope'}]
       #dispatcher.utter_button_message(message, buttons=buttons)
       print(tracker.latest_message)
       dispatcher.utter_message("Not trained for this .")

       return []



class ActionFallbackAction(Action):
    def name(self):
           return "fallback_action"

    def run(self, dispatcher, tracker, domain):
       # get the most likely intent
       latest = tracker.latest_message

       #print(str(tracker.__dict__))
       # get the prompt for the intent
       intent_prompt = ""
       #self.intent_mappings[last_intent_name]
       # Create the affirmation message and add two buttons to it.
       # Use '/<intent_name>' as payload to directly trigger '<intent_name>'
       # when the button is clicked.
       #message = "Did you mean '{}'?".format(intent_prompt)
       #buttons = [{'title': 'Yes',
       #            'payload': '/{}'.format(last_intent_name)},
       #           {'title': 'No',
       #            'payload': '/out_of_scope'}]
       #dispatcher.utter_button_message(message, buttons=buttons)
       msg="Sorry , I am not yet trained for this , please enter valid question."
       dispatcher.utter_message(msg)
       try:
           from googlesearch import search
       except ImportError:
           print("No module named 'google' found")

       # to search
       query = latest["text"]
       link="";
       for j in search(query, tld="co.in", num=10, stop=1, pause=2):
           link = "<a href="+j+" target=\"_blank\">Here</a> is the result form google ."
           dispatcher.utter_message(link)

       print(latest)

       return []