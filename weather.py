import requests
from api_key import serviceurl, api_key

#Initial input and request
city = input('Enter city: ')
if len(city) < 1: city = 'Columbus'  #For testing
url = serviceurl + 'appid=' + api_key + "&q=" + city #hiding API key
data = requests.get(url)

#Data pulled from API
weather = data.json()['weather'][0]['main']
temp = data.json()['main']['temp']

#Converting temp to fahrenheit
tempF = round(temp*(9/5) - 459.67)

#Output
print('The weather in', city, 'is', weather)
print('The temperature in', city, 'is', tempF,'F')