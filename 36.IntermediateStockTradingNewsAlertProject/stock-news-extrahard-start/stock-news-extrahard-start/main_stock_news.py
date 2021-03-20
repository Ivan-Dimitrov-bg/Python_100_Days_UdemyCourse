import requests
import os
from datetime import datetime, timedelta
from twilio.rest import Client
from dateutil.parser import parse
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
PRECENTEGE_CONSTANT = 0.1
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day
# before yesterday then print("Get News").

account_sid = os.environ["account_sid"]
auth_token = os.environ["auth_token"]
api_kay_al = os.environ["key_al"]
tel_send = os.environ["tel_send"]
tel_mine = os.environ["tel_mine"]

email_from = os.environ["email_from"]
email_to = os.environ["email_to"]
email_pass = os.environ["email_pass"]





my_email = "some_email@gmail.com"
password = "dfa;sfa23dsfs"


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
def take_symbol(diff_number: float)-> str:
    if diff_number > 0:
        # return "🔺"
        return "up "
    else:
        # return "🔻"
        return "donw "

def format_for_mail(all_news: [], precent_increase: float) -> str:
    symbol = take_symbol(precent_increase)
    body_formated = ""
    for i in range(0, 3):
        date_time = parse(all_news[i][2]).strftime('%Y-%m-%d %H:%M')
        body_formated = body_formated + f"TSLA: {symbol}{round(precent_increase, 0)}% \n Headline:{date_time} - {all_news[i][0]}  \n Brief: {all_news[i][1]} \n URL:{all_news[i][3]} \n"
    return body_formated

def send_mail(msg: str):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email_from, password=email_pass)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email_to,
            msg=f"Subject:stock info{COMPANY_NAME}\n\n {msg}"
        )


def send_message(all_news: str):
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=all_news,
        from_=tel_send,
        to=tel_mine,
    )
    print(message.status)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news()->[]:

    key_news = os.environ["key_news"]
    params = {
       "qInTitle":"Tesla Inc",
        "apiKey": key_news,
        "sortBy": "popularity",
        "language": "en"
    }

    data_news = requests.get("https://newsapi.org/v2/everything", params=params)
    data_json = data_news.json()
    print(data_json)
    all_news = []
    for i in range(0, 3):
        title = data_json["articles"][i]["title"]
        description = data_json["articles"][i]["description"]
        publishedAt = data_json["articles"][i]["publishedAt"]
        url = data_json["articles"][i]["url"]
        all_news.append((title, description, publishedAt, url))
    return all_news

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and
# description to your phone number.
def get_stock_info()->tuple:
    diff_present = 0

    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": api_kay_al
    }

    data = requests.get("https://www.alphavantage.co/query", params=stock_params)

    day_yesterday = (datetime.now() - timedelta(1)).strftime("%Y-%m-%d")
    day_before_yesterday = (datetime.now() - timedelta(2)).strftime("%Y-%m-%d")
    pr_close_one_day_before = float(data.json()["Time Series (Daily)"][day_yesterday]["4. close"])
    pr_close_two_day_before = float(data.json()["Time Series (Daily)"][day_before_yesterday]["4. close"])

    # second way
    # data_list = [value for (key, value) in data.json()["Time Series (Daily)"].items()]
    # pr_close_one_day_before_2 = float(data_list[0]["4. close"])
    # pr_close_two_day_before_2 = float(data_list[1]["4. close"])
    # print(pr_close_one_day_before_2)
    # print(pr_close_two_day_before_2)
    # print(pr_close_one_day_before)
    # print(pr_close_two_day_before)
    # print(pr_close_one_day_before - pr_close_two_day_before)
    diff_number = pr_close_one_day_before - pr_close_two_day_before

    diff_present = (abs(pr_close_one_day_before - pr_close_two_day_before) / pr_close_one_day_before) * 100
    return (diff_present, diff_number)

def main():
    precent_increase, diff_number = get_stock_info()
    print(precent_increase)
    # precent_increase = 6  #for test
    if precent_increase > float(PRECENTEGE_CONSTANT):
        print("Get News")
        all_news_result = get_news()
        all_news_str = format_for_mail(all_news_result, diff_number)
        print(all_news_str)
        # send_message(all_news_str)
        send_mail(all_news_str)
    else:
        print(f"no {PRECENTEGE_CONSTANT}% differences")

main()





