# Python program to find current
# weather details of any city
# using openweathermap api

# import required modules
import requests, json

loc = "null"
base_url = "https://api.exchangeratesapi.io/latest?"
complete_url = base_url  # "&base=" + str(loc)
print("User wants base currency as " + complete_url)
response = requests.get(complete_url)
x = response.json()
if x["rates"] != "404":
	message = x["rates"]
else:
	message = "No Found"

print(message)

