## Generated Story 2663200858146617602
* greet
    - utter_greet
* restaurant_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_price
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_sendemail
* affirmative
    - utter_ask_emailid
* restaurant_search{"emailid": "aks@gmail.com"}
    - slot{"emailid": "aks@gmail.com"}
    - action_sendemail
    - export
	
## Generated Story -8394346982357441113
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_ask_sendemail
* goodbye
    - utter_goodbye
    - export


## Generated Story 6685268198969609181
* restaurant_search{"cuisine": "american", "location": "bangalore", "price": "300 to 700"}
    - slot{"cuisine": "american"}
    - slot{"location": "bangalore"}
    - slot{"price": "300 to 700"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_sendemail
* negative
    - utter_goodbye
    - export
	
## Generated Story 8407904618803640905
* restaurant_search{"cuisine": "chinese", "price": "more than 700"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "more than 700"}
    - utter_ask_location
* restaurant_search{"location": "vadodara"}
    - slot{"location": "vadodara"}
    - action_restaurant
    - slot{"location": "vadodara"}
    - utter_ask_sendemail
* affirmative
    - utter_ask_emailid
* restaurant_search{"emailid": "kskadsas12312@otlook.com"}
    - slot{"emailid": "kskadsas12312@otlook.com"}
    - action_sendemail
    - utter_goodbye
    - export


## Generated Story -6391831102656066824
* greet
    - utter_greet
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - utter_ask_location
* restaurant_search{"location": "gorakhpur"}
    - slot{"location": "gorakhpur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_restaurant
    - slot{"location": "gorakhpur"}
    - utter_ask_sendemail
* affirmative
    - utter_ask_emailid
* restaurant_search{"emailid": "khanna_123@rediffmail.com"}
    - slot{"emailid": "khanna_123@rediffmail.com"}
    - utter_goodbye
    - export

## Generated Story 5739203135155325964
* restaurant_search{"location": "jodhpur"}
    - slot{"location": "jodhpur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - slot{"location": "jodhpur"}
    - utter_ask_sendemail
* negative
    - utter_goodbye
    - export

## Generated Story -5562060621157900075
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_location
* restaurant_search{"location": "ludhiana"}
    - slot{"location": "ludhiana"}
    - utter_ask_price
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - action_restaurant
    - slot{"location": "ludhiana"}
    - utter_ask_sendemail
* affirmative
    - utter_ask_emailid
* restaurant_search{"emailid": "rajat@asda.com"}
    - slot{"emailid": "rajat@asda.com"}
    - action_sendemail
    - export

## Generated Story 6426434075203350142
* restaurant_search{"cuisine": "north indian", "location": "kochi", "price": "ofmore than 700"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "kochi"}
    - slot{"price": "ofmore than 700"}
    - action_restaurant
    - slot{"location": "kochi"}
    - utter_ask_sendemail
* negative
    - utter_goodbye
    - export

## Generated Story -3660786771167400049
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "kochi", "price": "lesser than 300"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "kochi"}
    - slot{"price": "lesser than 300"}
    - action_restaurant
    - slot{"location": "kochi"}
    - utter_ask_sendemail
* negative
    - utter_goodbye
* restaurant_search{"cuisine": "chinese", "location": "bareilly"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bareilly"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - slot{"location": "bareilly"}
    - utter_ask_sendemail
* negative
    - utter_goodbye
    - export

## Generated Story -5075431089904573749
* restaurant_search{"cuisine": "american", "location": "guntur", "price": "300 to 700"}
    - slot{"cuisine": "american"}
    - slot{"location": "guntur"}
    - slot{"price": "300 to 700"}
    - action_restaurant
    - slot{"location": "guntur"}
    - utter_ask_sendemail
* negative
    - utter_goodbye
    - export

## Generated Story 5628640459121871750
* restaurant_search{"cuisine": "north indian", "location": "kolkata"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "kolkata"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - slot{"location": "kolkata"}
    - utter_ask_sendemail
* negative
    - utter_goodbye
    - export

## Generated Story 7761892486650376245
* greet
    - utter_greet
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - slot{"location": "pune"}
    - utter_ask_sendemail
* affirmative
    - utter_ask_emailid
* restaurant_search{"emailid": "maksmda@asda.com"}
    - slot{"emailid": "maksmda@asda.com"}
    - action_sendemail
    - export
	
## Generated Story 2663200858146617602
* greet
    - utter_greet
* restaurant_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_price
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_sendemail
* affirmative
    - utter_ask_emailid
* restaurant_search{"emailid": "aks@gmail.com"}
    - slot{"emailid": "aks@gmail.com"}
    - action_sendemail
    - export
	
## Generated Story -8394346982357441113
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_ask_sendemail
* goodbye
    - utter_goodbye
    - export


## Generated Story 6685268198969609181
* restaurant_search{"cuisine": "american", "location": "bangalore", "price": "300 to 700"}
    - slot{"cuisine": "american"}
    - slot{"location": "bangalore"}
    - slot{"price": "300 to 700"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_sendemail
* negative
    - utter_goodbye
    - export
	
## Generated Story 8407904618803640905
* restaurant_search{"cuisine": "chinese", "price": "more than 700"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "more than 700"}
    - utter_ask_location
* restaurant_search{"location": "vadodara"}
    - slot{"location": "vadodara"}
    - action_restaurant
    - slot{"location": "vadodara"}
    - utter_ask_sendemail
* affirmative
    - utter_ask_emailid
* restaurant_search{"emailid": "kskadsas12312@otlook.com"}
    - slot{"emailid": "kskadsas12312@otlook.com"}
    - action_sendemail
    - utter_goodbye
    - export


## Generated Story -6391831102656066824
* greet
    - utter_greet
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - utter_ask_location
* restaurant_search{"location": "gorakhpur"}
    - slot{"location": "gorakhpur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_restaurant
    - slot{"location": "gorakhpur"}
    - utter_ask_sendemail
* affirmative
    - utter_ask_emailid
* restaurant_search{"emailid": "khanna_123@rediffmail.com"}
    - slot{"emailid": "khanna_123@rediffmail.com"}
    - utter_goodbye
    - export

## Generated Story 5739203135155325964
* restaurant_search{"location": "jodhpur"}
    - slot{"location": "jodhpur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - slot{"location": "jodhpur"}
    - utter_ask_sendemail
* negative
    - utter_goodbye
    - export

## Generated Story -5562060621157900075
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_location
* restaurant_search{"location": "ludhiana"}
    - slot{"location": "ludhiana"}
    - utter_ask_price
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - action_restaurant
    - slot{"location": "ludhiana"}
    - utter_ask_sendemail
* affirmative
    - utter_ask_emailid
* restaurant_search{"emailid": "rajat@asda.com"}
    - slot{"emailid": "rajat@asda.com"}
    - action_sendemail
    - export

## Generated Story 6426434075203350142
* restaurant_search{"cuisine": "north indian", "location": "kochi", "price": "ofmore than 700"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "kochi"}
    - slot{"price": "ofmore than 700"}
    - action_restaurant
    - slot{"location": "kochi"}
    - utter_ask_sendemail
* negative
    - utter_goodbye
    - export

## Generated Story -3660786771167400049
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "kochi", "price": "lesser than 300"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "kochi"}
    - slot{"price": "lesser than 300"}
    - action_restaurant
    - slot{"location": "kochi"}
    - utter_ask_sendemail
* negative
    - utter_goodbye
* restaurant_search{"cuisine": "chinese", "location": "bareilly"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bareilly"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - slot{"location": "bareilly"}
    - utter_ask_sendemail
* negative
    - utter_goodbye
    - export

## Generated Story -5075431089904573749
* restaurant_search{"cuisine": "american", "location": "guntur", "price": "300 to 700"}
    - slot{"cuisine": "american"}
    - slot{"location": "guntur"}
    - slot{"price": "300 to 700"}
    - action_restaurant
    - slot{"location": "guntur"}
    - utter_ask_sendemail
* negative
    - utter_goodbye
    - export

## Generated Story 5628640459121871750
* restaurant_search{"cuisine": "north indian", "location": "kolkata"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "kolkata"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - slot{"location": "kolkata"}
    - utter_ask_sendemail
* negative
    - utter_goodbye
    - export

## Generated Story 7761892486650376245
* greet
    - utter_greet
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - slot{"location": "pune"}
    - utter_ask_sendemail
* affirmative
    - utter_ask_emailid
* restaurant_search{"emailid": "maksmda@asda.com"}
    - slot{"emailid": "maksmda@asda.com"}
    - action_sendemail
    - export
