import datetime as dt
import smtplib
import random

MY_EMAIL = "*****@gmail.com"
MY_PASS = "*******"

week_day = dt.datetime.now().weekday()
if week_day == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="*****@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{quote}",
        )