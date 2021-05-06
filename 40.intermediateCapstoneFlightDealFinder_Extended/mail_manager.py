import random
import smtplib
import datetime as dt
import os

my_mail = os.environ["my_email"]
password = os.environ["my_password"]

class Send_Mail:

    def send_email(self, mail_to, mail_subject, mail_body):

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_mail, password=password)
            connection.sendmail(
                from_addr=my_mail,
                to_addrs="Some_mail@gmail.com",
                msg=f"{subject}\n\n{msg}"
            )

    with open("quotes.txt", mode="r") as file:
        data = file.readlines()
        quoteOfTheWeek = random.choice(data)

    day_today = dt.datetime.now().weekday()

    if day_today == 2:
        send_email(subject="Monday Motivational", msg=quoteOfTheWeek)


