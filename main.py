from twilio.rest import Client
import requests
import os

#Your twilio account sid 
account_sid = "AC980d47f9484e0e592f5eb832dc88358d"

#Your twilio api auth token. You get it once you create a twilio account and sign in for the free API tier.
#Here we decided to hide it as an environment variable for conveniency and security
#You could just set your auth_token as a variable as shown below
#auth_token = "Your_twilio_auth_token"
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")


#Your open weather API key
#APP_ID = "Your_Openweather_API_key"
APP_ID = os.environ.get("OWM_APP_ID")
MY_LONG = #The longitude of your current location
MY_LAT = 3.95313 #The latitude of your current location

def notify(message: str):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message,
        from_="+16403008970",
        to="+237696130289")
    print(message.status)

PARAMETER = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "daily,minutely,current",
    "appid": APP_ID
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=PARAMETER)
response.raise_for_status()
weather_data = response.json()
twelve_hour_condition = []
will_rain: bool = False

for index in range(0,11):
    hour_condition = weather_data["hourly"][index]["weather"][0]["id"]
    if hour_condition < 700:
        will_rain = True

if will_rain:
    notify("Hello, It's going to rain today.   Don't forget to bring an umbrella")

else:
    notify("Hello, there will be no rain today. Enjoy your day")




