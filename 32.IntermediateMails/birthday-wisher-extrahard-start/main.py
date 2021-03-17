##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib

PLACEHOLDER = "[NAME]"
MY_EMAIL = "MY_EMAL"
MY_PASSWORD = "MY_PASSWORD"

def send_letter(letter, to_email):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=to_email,
            msg=f"Subject:Happy Birth Day\n\n {letter}"
        )

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
def pick_a_letter(name):
    list_letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
    random_letter = random.choice(list_letters)
    with open(random_letter) as file_txt:
        current_letter = file_txt.read()
        current_letter = current_letter.replace(PLACEHOLDER, name)
    return current_letter

# 1. Update the birthdays.csv
# done!

# 2. Check if today matches a birthday in the birthdays.csv

now = dt.datetime.now()
now_day = now.day
now_month = now.month

# print(today_day)
data = pandas.read_csv("birthdays.csv")
for item in data.iterrows():
    data_month = data["month"].values[0]
    data_day = data["day"].values[0]
    name = data["name"].values[0]
    mail_address = data["email"].values[0]

    if data_month == now_month and data_day == now_day:
        letter_ready_to_be_send = pick_a_letter(name)
        print(letter_ready_to_be_send)
        send_letter(letter_ready_to_be_send, mail_address)



#smpt gmail = smtp.gmail.com
#yahoo = smtp.mail.yahoo.com
#hotmail = smtp.live.com



