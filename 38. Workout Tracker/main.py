import requests
import os
from datetime import datetime

# USER DATA
GENDER = "Male"
WEIGHT_KG = 75
HEIGHT_CM = 177
AGE = 23

# NUTRITIONIX API AND ENDPOINT
APP_ID  = "9baa40ec"
API_KEY = "3ea198a507a86f8ab62bf1651ecdf995"
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

# SHEETY ENDPOINT
SHEETY_ENDPOINT = "https://api.sheety.co/f263c0f3bff357573d7bc6dac901e665/workouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

# NUTRITIONIX API HEADERS
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

# BEARER AUTHENTICATION FOR SHEETY
bearer_headers = {
    "Authorization": "Bearer MYREALLYLONGPASSWORD"
}

# PARAMS FOR NUTRITIONIX API
params = {
    "query": f"{exercise_text}",
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}


# NUTRIONIX API INITIALIZATION AND DATA UPDATE USING HTTP POST

response = requests.post(NUTRITIONIX_ENDPOINT, json=params, headers=headers)
result = response.json()
print(result)

# TODAY'S DATE AND TIME
now = datetime.now()
today = now.date().strftime("%d/%m/%Y")
time = now.time().strftime("%H:%M")

# IMPORTING DATA FROM NUTRIONIX API TO SHEETY SHEET's
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }


# https://docs.google.com/spreadsheets/d/1cecJpiEPwmYluPbr2lHLSNdFtwdumue5aslfi0W8gfk/edit#gid=0
sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs, headers=bearer_headers)
print(sheet_response.text)