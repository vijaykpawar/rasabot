## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## curency path 1
* inform{"currency":"USD"}
 - get_currency

## curency path 2
* inform{"currency":"INR"}
 - get_currency

## New Story 1
* greet
    - utter_greet
* ask
    - utter_ask_currency
* inform{"currency":"INR"}
    - get_currency
    - utter_did_that_help


## New Story 2
* greet
    - utter_greet
* ask
    - utter_ask_currency
* inform{"currency":"USD"}
    - get_currency
    - utter_did_that_help

## form faq
* remittance_form
    - utter_remittance_form