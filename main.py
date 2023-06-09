import requests
from datetime import datetime
import os

GENDER = YOUR GENDER male/female
WEIGHT_KG = YOUR WEIGHT
HEIGHT_CM = YOUR HEIGHT
AGE = YOUR AGE

APP_ID = os.environ["NT_APP_ID"]  # YOUR APP ID
API_KEY = os.environ["NT_API_KEY"]  # YOUR API KEY

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["SHEET_ENDPOINT"]  # YOUR SHEETY ENDPOINT

exercise_text = input("Tell me which exercises you did: ")

header = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

parameters = {
    'query': exercise_text,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=header)
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%X")
bearer_headers = {
        "Authorization": f"Bearer {os.environ['TOKEN']}"
    }

for exercise in result['exercises']:
    sheet_inputs = {
        'workout': {
            'date': today_date,
            'time': time_now,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)
    print(sheet_response.text)
