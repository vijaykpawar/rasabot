## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## say goodbye
* goodbye
  - utter_goodbye

## currency path 1
* inform
 - get_currency

## currency path 2
* inform
 - get_currency
 - save_trends

## New Story 1
* greet
    - utter_greet
* ask
    - utter_ask_currency
* inform
    - get_currency
    - save_trends


## story 2 for currency
* ask
    - utter_ask_currency
* inform
    - get_currency
    - save_trends

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

## story 2 for general_insurance
* general_insurance
    - code_action
