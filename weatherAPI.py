import requests
import os
from datetime import datetime

def main():
	cityName = input('Enter city name: ').lower()
	countryCode = input('Enter country code: ').lower()

	key = os.environ.get('WEATHER_KEY') #Returns None if not found
	query = {'q': '{cityName},{countryCode}', 'units': 'imperial', 'appid': key}
	#print(query)

	url = 'http://api.openweathermap.org/data/2.5/forcast'

	data = requests.get(url, params=query).json()
	#printing all data print(data)
	forcast_items = data['list']

	for forcast in forcast_items:
		timestamp = forcast['dt']
		date= datetime.fromtimestamp(timestamp)
		weather_description = data['weather'][0]['description']
		temp_f = data['main']['temp']
		wind_speed = data['wind']['speed']
		print(f'The time and date is {date},\n the temperature is {temp_f:.2f}F,\n the weather is {weather_description},\n the wind speed is {wind_speed}MPH .')

if __name__ == '__main__':
	main()	