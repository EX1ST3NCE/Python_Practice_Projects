import requests
from datetime import datetime
import smtplib
import time

# Email and Password Values
MY_EMAIL = '****************@gmail.com'
MY_PASS = '*********************'

# Latitude & Longitude values of Bangalore
MY_LAT = 12.971599
MY_LONG = 77.594566

# API call to ISS Station
def iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_lat = float(data['iss_position']['latitude'])
    iss_lng = float(data['iss_position']['longitude'])

    # Position is within +5 or -5 degrees of the ISS position
    if MY_LAT -5 <= iss_lat >= MY_LAT+5 and MY_LONG-5 <= iss_lng >= MY_LONG+5:
        return True


# API call for getting the sunset and sunrise timings in bangalore 
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
    current_hour = datetime.now().utcnow().hour
    if current_hour >= sunset or current_hour <=sunrise:
        return True

while True:
    time.sleep(60)
    if iss_overhead() and is_night(): 
        with smtplib.SMTP_SSL('smtp.gmail.com') as connection:
            connection.login(MY_EMAIL, MY_PASS)
            connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs='***************@gmail.com',
            msg="Subject:Look Up!!!\n\nGo outside, the ISS satellite is nearby!!",
        )