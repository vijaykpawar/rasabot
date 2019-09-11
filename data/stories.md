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
  - utter_greet

## say goodbye
* goodbye
  - utter_goodbye

## currency path 1
* inform
 - get_currency

## currency path 2
* inform
 - get_currency

## New Story 1
* greet
    - utter_greet
* ask
    - utter_ask_currency
* inform
    - get_currency
    - utter_did_that_help


## New Story 2
* greet
    - utter_greet
* ask
    - utter_ask_currency
* inform
    - get_currency
    - utter_did_that_help

## story 2 for currency
* ask
    - utter_ask_currency
* inform
    - get_currency
    - utter_did_that_help

## form faq
* remittance_form
    - utter_remittance_form
    - save_trends

## ask trends story
* trends
    - get_trends

## get purpose story
* purpose
    - utter_purpose
* general_insurance
    - code_action
