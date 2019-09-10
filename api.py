# Python program to find current
# weather details of any city
# using openweathermap api

# import required modules
import requests, json
loc = "USD"
base_url = "https://api.exchangeratesapi.io/latest?base=USD"
complete_url = base_url  # "&base=" + str(loc)
print("User wants base currency as " + complete_url)
response = requests.get(complete_url)
x = response.json()
if x["rates"] != "404":
	message = x["rates"]
	msg = " Source : European Central Bank <br>"
	for key, value in message.items():
		msg = msg + str(key) + " " + str(value) + " <br>"

	print(str(msg))
else:
	message = "No Found"



