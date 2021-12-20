##################### Extra Hard Starting Project ######################
from pandas import  read_csv
from datetime import datetime
from random import choice
from re import sub
from smtplib import SMTP

# 1. Update the birthdays.csv
dataframe = read_csv("./birthdays.csv")
records = dataframe.to_dict(orient="records")
# orient ="list"

print(records)

# 2. Check if today matches a birthday in the birthdays.csv
now = datetime.now()
for data in records:
    if now.day == data['day'] and now.month == data['month']:
        choice_extension = choice(["letter_1.txt", "letter_2.txt", "letter_3.txt"])
        with open(f"letter_templates/{choice_extension}") as wish:
            bir_wish = wish.read()
        letter = sub("\[NAME\]", data['name'], bir_wish)
        my_email = "pythonista.santhosh@gmail.com"
        password = "santhoram2002"
        with SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=f"{data['email']}", msg=f"Subject: Wish from santhosh\n\n"
                                                                                     f"{letter}")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
