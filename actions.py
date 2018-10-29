from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json
import smtplib

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"1e82c6993d0289dc4a0f26547ef39bec"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		tier1_2_cities = ['ahmedabad', 'bangalore', 'bengaluru', 'bombay', 'calcutta', 'kolkota', 'madras', 'chennai' , 'delhi' , 'hyderabad' , 'kolkata' , 'mumbai' , 'pune', 'agra', 'ajmer' , 'aligarh', 'allahabad' , 'amravati' , 'amritsar' , 'asansol' , 'aurangabad', 'bareilly','belgaum' , 'bhavnagar' , 'bhiwandi', 'bhopal', 'bhubaneswar', 'bikaner', 'bokaro steel city', 'chandigarh', 'coimbatore', 'cuttack', 'dehradun' , 'dhanbad', 'durg-bhilai nagar' , 'durgapur', 'erode', 'faridabad', 'firozabad', 'ghaziabad', 'gorakhpur', 'gulbarga', 'guntur', 'gurgaon', 'guwahati' ,'gwalior', 'hubli-dharwad', 'indore', 'jabalpur', 'jaipur', 'jalandhar' , 'jammu' , 'jamnagar', 'jamshedpur' , 'jhansi' , 'jodhpur' , 'kannur' 'kanpur', 'kakinada' , 'kochi', 'kottayam' , 'kolhapur', 'kollam', 'kota', 'kozhikode' , 'kurnool' , 'lucknow' , 'ludhiana','madurai' , 'malappuram', 'mathura', 'goa', 'mangalore', 'meerut', 'moradabad', 'mysore', 'nagpur', 'nanded', 'nashik', 'nellore', 'noida','palakkad', 'patna', 'pondicherry', 'raipur', 'rajkot', 'rajahmundry', 'ranchi', 'rourkela', 'salem','sangli' , 'siliguri', 'solapur', 'srinagar', 'sultanpur', 'surat', 'thiruvananthapuram', 'thrissur', 'tiruchirappalli', 'tirunelveli', 'tiruppur', 'ujjain', 'vijayapura', 'vadodara', 'varanasi', 'vasai-virar city', 'vijayawada', 'visakhapatnam', 'warangal'
		]
		if(loc in tier1_2_cities):
			if(loc == 'bengaluru'):
				loc = 'bangalore'
			if(loc == 'bombay'):
				loc = 'mumbai'
			if(loc == 'calcutta'):
				loc = 'Kolkata'
			if(loc == 'Kolkota'):
				loc = 'kolkata'
			if(loc == 'madras'):
				loc = 'chennai'
			cuisine = tracker.get_slot('cuisine')
			location_detail=zomato.get_location(loc, 1)
			d1 = json.loads(location_detail)
			lat=d1["location_suggestions"][0]["latitude"]
			lon=d1["location_suggestions"][0]["longitude"]
			cuisines_dict={'american':1,'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'mexican':73,'north indian':50,'south indian':85}
			results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 20)
			d = json.loads(results)
			response=""
			counter=1
			price = tracker.get_slot('price')
			print(price)
			if d['results_found'] == 0:
				response= "no results"
			else:
				for restaurant in d['restaurants']:
					if counter < 6:
						if price == 'lesser than 300':
							if restaurant['restaurant']['average_cost_for_two'] <=300:
								response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+\
								" has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating']+"\n"
								counter = counter + 1
								#print(response)
						if price == '300 to 700': 
							if restaurant['restaurant']['average_cost_for_two'] >= 300 and restaurant['restaurant']['average_cost_for_two'] <= 700:
								response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+\
								" has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating']+"\n"
								counter = counter + 1
								#print(response)
						if price == 'more than 700':
							if restaurant['restaurant']['average_cost_for_two'] >=700:
								response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+\
								" has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating']+"\n"
								counter = counter + 1
								#print(response)
		else:
			response="We do not operate in that area yet"+loc
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc)]
		
class SendEmail(Action):
	def name(self):
		return 'action_sendemail'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"6ce88a5ec1419e335afa1c7f92f4b739"}
		zomato = zomatopy.initialize_app(config)
		emailid=tracker.get_slot('emailid');
		loc = tracker.get_slot('location')
		tier1_2_cities = ['ahmedabad', 'bangalore', 'bengaluru', 'bombay', 'calcutta', 'kolkota', 'madras', 'chennai' , 'delhi' , 'hyderabad' , 'kolkata' , 'mumbai' , 'pune', 'agra', 'ajmer' , 'aligarh', 'allahabad' , 'amravati' , 'amritsar' , 'asansol' , 'aurangabad', 'bareilly','belgaum' , 'bhavnagar' , 'bhiwandi', 'bhopal', 'bhubaneswar', 'bikaner', 'bokaro steel city', 'chandigarh', 'coimbatore', 'cuttack', 'dehradun' , 'dhanbad', 'durg-bhilai nagar' , 'durgapur', 'erode', 'faridabad', 'firozabad', 'ghaziabad', 'gorakhpur', 'gulbarga', 'guntur', 'gurgaon', 'guwahati' ,'gwalior', 'hubli-dharwad', 'indore', 'jabalpur', 'jaipur', 'jalandhar' , 'jammu' , 'jamnagar', 'jamshedpur' , 'jhansi', 'jodhpur' , 'kannur' 'kanpur', 'kakinada' , 'kochi', 'kottayam' , 'kolhapur', 'kollam', 'kota', 'kozhikode' , 'kurnool' , 'lucknow' , 'ludhiana','madurai' , 'malappuram', 'mathura', 'goa', 'mangalore', 'meerut', 'moradabad', 'mysore', 'nagpur', 'nanded', 'nashik', 'nellore', 'noida','palakkad', 'patna', 'pondicherry', 'raipur', 'rajkot', 'rajahmundry', 'ranchi', 'rourkela', 'salem','sangli' , 'siliguri', 'solapur', 'srinagar', 'sultanpur', 'surat', 'thiruvananthapuram', 'thrissur', 'tiruchirappalli', 'tirunelveli', 'tiruppur', 'ujjain', 'vijayapura', 'vadodara', 'varanasi', 'vasai-virar city', 'vijayawada', 'visakhapatnam', 'warangal'
		]
		if(loc in tier1_2_cities):
			if(loc == 'bengaluru'):
				loc = 'bangalore'
			if(loc == 'bombay'):
				loc = 'mumbai'
			if(loc == 'calcutta'):
				loc = 'Kolkata'
			if(loc == 'Kolkota'):
				loc = 'kolkata'
			if(loc == 'madras'):
				loc = 'chennai'
			cuisine = tracker.get_slot('cuisine')
			location_detail=zomato.get_location(loc, 1)
			d1 = json.loads(location_detail)
			lat=d1["location_suggestions"][0]["latitude"]
			lon=d1["location_suggestions"][0]["longitude"]
			cuisines_dict={'american':1,'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'mexican':73,'north indian':50,'south indian':85}
			results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 10)
			d = json.loads(results)
			response=""
			counter=1
			price = tracker.get_slot('price')
			if d['results_found'] == 0:
				response= "no results"
			else:
				for restaurant in d['restaurants']:
					if counter < 11:
						if price == 'lesser than 300':
							if restaurant['restaurant']['average_cost_for_two'] <=300:
								response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+\
								" having budget of "+ str(restaurant['restaurant']['average_cost_for_two']) +" has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating']+"\n"
								counter = counter + 1
								#print(response)
						if price == '300 to 700': 
							if restaurant['restaurant']['average_cost_for_two'] >= 300 and restaurant['restaurant']['average_cost_for_two'] <= 700:
								response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+\
								" having budget of "+ str(restaurant['restaurant']['average_cost_for_two']) +" has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating']+"\n"
								counter = counter + 1
								#print(response)
						if price == 'more than 700':
							if restaurant['restaurant']['average_cost_for_two'] >=700:
								response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+\
								" having budget of "+ str(restaurant['restaurant']['average_cost_for_two']) +" has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating']+"\n"
								counter = counter + 1
								#print(response)
					
		else:
			response="We do not operate in that area yet"+loc
		
		print("Sending email ...")
		# creates SMTP session 
		s = smtplib.SMTP('smtp.gmail.com', 587)
		
		# start TLS for security 
		s.starttls() 
		
		# Authentication 
		print("login")
		s.login("rasachatbottest@gmail.com", "Rasa123###") 
		
		# message to be sent 
		message = response
		
		# sending the mail 
		s.sendmail("rasachatbottest@gmail.com", emailid, message)
		
		# terminating the session 
		s.quit()		
		
		print("email sent")
		return [SlotSet('location',loc)]