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
    - save_trends
* general_insurance
    - code_action
    - save_trends

## story 2 for general_insurance
* general_insurance
    - code_action
    - save_trends

## story for get A2 form
* get_me_form_a2
    - save_trends
    - send_form_a2

## story for get A2 form data
* autofill_a2_form
    - save_trends
    - send_form_a2_data
