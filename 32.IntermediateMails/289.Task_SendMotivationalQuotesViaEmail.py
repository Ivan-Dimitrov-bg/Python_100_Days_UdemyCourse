import random
import smtplib
import datetime as dt


def send_email(subject, msg):
    my_mail = "some_emal@gmail.com"
    password = "dsfasfdfserw"
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


