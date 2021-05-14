import requests
from twilio.rest import Client

# OpenWeatherMap API Endpoint
OWM_Endpoint  = "https://api.openweathermap.org/data/2.5/onecall"

# Always export the API keys & Auth_token to Env variables
API_KEY = "######################"
account_sid = 'ACcc3060bfd0a40f88c77328518da8d30b'
auth_token = '###################'

MY_LAT = 12.971599
MY_LONG = 77.594566
flag = False

# OpenWeatherMap API
weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily,alerts",
    "appid": API_KEY,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# Checking for the next 12 hours weather code
for i in range(12):
    # If condition code is less than 700, it will rain
    if weather_data["hourly"][i]["weather"][0]["id"] < 700:
        flag = True

# Using Twilio API to send text messages
if flag:
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body="It's going to rain. Remember to bring an ☔",
                        from_='+18056641192',
                        to='+91**********'
                    )

    print(message.status)