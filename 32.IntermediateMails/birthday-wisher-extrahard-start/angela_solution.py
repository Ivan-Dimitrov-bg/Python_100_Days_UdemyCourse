from datetime import datetime
import smtplib
import random
import pandas

MY_EMAIL = "MY_EMAL"
MY_PASSWORD = "MY_PASSWORD"

today_month_day = (datetime.now().month, datetime.now().day)
data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# print(birthday_dict)
if today_month_day in birthday_dict:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_dict["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_dict["email"],
            msg=f"Subject: Happy Birttday!\n\n{connection}"
        )