import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "MY_EMAIL"
MY_PASS = "MY_PASS"
SMPT_GMAIL = "smpt.gmail.com"
MY_LAT = 42.697708 # Your latitude
MY_LONG = 23.321867 # Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LAT-5) <= iss_latitude <= (MY_LAT+5) and (MY_LONG-5) <= iss_longitude >= (MY_LONG+5):
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.

while True:
    # BONUS: run the code every 60 seconds.
    time.sleep(60)
    if is_night() and is_iss_overhead():
        with smtplib.SMTP(SMPT_GMAIL) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASS)
            connection.sendmail(
                to_addrs=MY_EMAIL,
                from_addr=MY_EMAIL,
                msg=f"Subject:Look UP! \n\n The ISS is over your head"
            )

    # 1.Connection [with]
    # 2.Security (starttls)
    # 3.Login (my_email, my_pass)
    # 4 Send
    #     to_addrs=
    #     from_addres=
    #     msg=f"Subject: \n\n MSG"

