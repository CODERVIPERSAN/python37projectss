from datetime import datetime
import random

now = datetime.now()
weekdays = now.isoweekday()
with open(file="quotes.txt") as file:
    rand_choice = random.choice(file.readlines())
if weekdays == weekdays:
    # simple mail transfer protocol
    from smtplib import SMTP

    my_email = "pythonista.santhosh@gmail.com"
    password ="santhoram2002"

    with SMTP("smtp.gmail.com",port=587) as connection:  # specifies the email providers smtp sever----
        connection.ehlo()
        connection.starttls()  # makes the connection secure -
        connection.ehlo()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="santhoram2002@gmail.com",
                            msg="Subject:santhosh_motivation quote of the day \n\n "
                                f"{rand_choice}")
# ////////##########################storing the date
data_of_birth = datetime(year=2002, month=5, day=8, hour=4,)
print(data_of_birth)
