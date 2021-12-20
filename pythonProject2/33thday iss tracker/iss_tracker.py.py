# api application programming interface
# an application programming interface ---is a set of commands
# ,functions ,protocols and objects that programmers can use to
# to create software or interact with an external system

# interface between our program and external sources
# api endpoint ---- is kind of url location of the particular data
#        eg api.coinbase.com
# api request ----
#######################################################
import requests
from datetime import datetime
from smtplib import SMTP

LAT = 11.028560
LONG = 77.131477


def is_over():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    # <Response [200]>
    # response code ---
    # 1XX hold on
    # 2XX here you go --successful
    # 3XX go away
    # 4XX you screwed up ----you search is doesnt exists
    # 5XX i screwed up ---- may be sever down or some other sever based issues
    response.raise_for_status()
    data_lat_long = (
        float(response.json()['iss_position']['latitude']), float(response.json()['iss_position']['longitude']))
    if (LAT - 5 <= data_lat_long[0] <= LAT + 5) and (LONG - 5 <= data_lat_long[1] <= LONG + 5):
        return True


# //parameter as dictionary
parameter = {
    'lat': LAT,
    'lng': LONG,
    'formatted': 0
}



def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
    response.raise_for_status()
    data = response.json()
    now = (datetime.now()).hour
    sunrise = int((data['results']['sunrise'].split("T")[1]).split(':')[0]) + 6
    sunset = int((data['results']['sunset'].split("T")[1]).split(':')[0]) + 6
    if not sunrise < now < sunset:
        return True


######################################################
endgame = False
frequency = 0
while not endgame:
    print(frequency)
    if is_night():
        if is_over():
            with SMTP("smtp.gmail.com") as connection:
                frequency += 1
                connection.starttls()
                connection.login(user="pythonista.santhosh@gmail.com", password="santhoram2002")
                connection.sendmail(from_addr="pythonista.santhosh@gmail.com", to_addrs="pythonista.santhosh@gmail.com",
                                    msg="Subject: iss_near u\n\n "
                                        "start searching for iss, tracker alert ")
                if frequency == 5:
                    endgame = True
