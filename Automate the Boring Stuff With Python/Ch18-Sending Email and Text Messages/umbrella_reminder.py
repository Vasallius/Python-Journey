# Vasallius

import requests, json
from twilio.rest import Client

city = input('City:')
API = input('API: ')
accountSID = input('Enter account SID:')
authToken = input('Enter auth token:')
twilio_number = input('Enter twilio number:')
number_to_text = input('Enter your number: )

twilio_client = Client(accountSID,authToken)
r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}')
data = json.loads(r.text)

umbrella_weather = ['Thunderstorm','Drizzle','Rain']

main = data['weather'][0]['main']
description = data['weather'][0]['description']

if main in umbrella_weather:
    message = twilio_client.messages.create(body=f'Hi . It is raining today with a chance of {description}. Bring an umbrella.',from_=twilio_number,to=number_to_text)
else:
    pass