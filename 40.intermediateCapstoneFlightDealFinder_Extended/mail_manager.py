import random
import smtplib
import datetime as dt
import os
from data_manager import DataManager

class Manage_Mail:

    def __init__(self):
        self.manager = DataManager()
        self.my_mail = os.environ["my_email"]
        self.password = os.environ["my_password"]
        self.all_mails = {}

    def send_email(self, mail_to, mail_subject, mail_body):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.my_mail, password=self.password)
            connection.sendmail(
                from_addr=self.my_mail,
                to_addrs=mail_to,
                msg=f"{mail_subject}\n\n{mail_body}"
            )

    def add_user_email(self):
        print("Welcome to Angela's Flight Club.")
        first_name = print("We find the best flight deals and email you. What is your first name?")
        second_name = print("Second Name:")
        email = print("Email:")
        repeat_email = print("Repeat Email:")
        if email == repeat_email:
            self.manager.save_user(first_name, second_name, email)




