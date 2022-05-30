import datetime as dt
import smtplib
import random

now = dt.datetime.now()
weekday = now.weekday()

MY_EMAIL = input("Enter your Gmail address: ")
MY_PASSWORD = input("Enter your password: ")

if weekday == 6:
    with open('quotes.txt') as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="daytonbraison@gmail.com",msg=f"Subject:Daily Motivational Quote!!\n\n{quote}")
    
    