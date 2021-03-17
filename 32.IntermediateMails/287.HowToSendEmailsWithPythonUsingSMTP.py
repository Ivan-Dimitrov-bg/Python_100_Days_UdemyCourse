import smtplib

my_email = "some_email@gmail.com"
password = "dfa;sfa23dsfs"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="Some_email2@gmail.com",
        msg="Subject:Hello\n\nThis is the body of the Email"
    )
