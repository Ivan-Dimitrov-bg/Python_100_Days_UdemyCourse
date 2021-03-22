import requests
from datetime import datetime
import os

g_token = os.environ["tokin_g"]
api_google_sheetss = os.environ["sheet_endpoint"]

def sheet_data():
    date_w = datetime.today().strftime("%d/%m/%Y")
    print(date_w)
    # time_w = datetime.now().strftime("%X")
    time_iso = datetime.now().time()
    now_time = ((time_iso.hour + ((time_iso.minute + (time_iso.second / 60.0)) / 60.0)) / 24.0)
    exercise_w = "Running"
    duration_w = 22
    calories_w = 130
    return(date_w, now_time, exercise_w, duration_w, calories_w)

def main():
    data_w=sheet_data()
    g_headers={
        "Authorization": f"Bearer {g_token}",
	    "Content-Type": "application/json",
    }
    g_json={
        "workout": {
          "date":data_w[0],
          "time":data_w[1],
          "exercise":data_w[2],
          "duration":data_w[3],
          "calories":data_w[4],
        }
    }
    print(g_json)
    data_api = requests.post(url=api_google_sheetss, json=g_json, headers=g_headers)
    print(data_api)

main()