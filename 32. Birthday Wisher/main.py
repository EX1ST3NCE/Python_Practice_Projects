import datetime as dt
import pandas as pd
import smtplib
import random

MY_EMAIL = "********@gmail.com"
MY_PASS = "*****************"

df = pd.read_csv('birthdays.csv')
day = dt.datetime.now().day
month = dt.datetime.now().month

for i in range(len(df)):
    if df['day'][i] == day and df['month'][i] == month:
        file = f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(file) as letter:
            old_letter = letter.read()
            new_letter = old_letter.replace("[NAME]", df['name'][i])

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(MY_EMAIL, MY_PASS)
            connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=df['email'][i],
            msg=f"Subject:Happy Birthday!!!\n\n{new_letter}",
        )