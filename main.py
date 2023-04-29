import requests
from datetime import datetime

GENDER = "male"  # YOUR GENDER male/female
WEIGHT_KG = 53.2  # YOUR WEIGHT
HEIGHT_CM = 179.07  # YOUR HEIGHT
AGE = 20  # YOUR AGE

APP_ID = "e60f2180"  # YOUR APP ID
API_KEY = "8215717b01a61ac97a9cfaf808529e57"  # YOUR API KEY

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/626acddb20e9a4b332e74f6bcdb60ea5/myWorkouts/workouts/"

exercise_text = input("Tell me which exercises you did: ")

header = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'Content-Type': 'application/json'
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=header)
result = response.json()

################### Start of Step 4 Solution ######################

today_date = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%X")
bearer_headers = {
        "Authorization": "Bearer ZmFyaGFubWFsaWs6MzU1NDk5MDc0ODkxNjM2"
    }
print(result)
for exercise in result['exercises']:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": time_now,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)
    print(sheet_response.json())
