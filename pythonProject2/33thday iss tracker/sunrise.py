import requests
from datetime import datetime
# //parameter as dictionary
parameter = {
    'lat': 11.028560,
    'lng': 77.131477,
    'formatted':0
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()
data = response.json()
print(data)
now = (datetime.now()).hour
sunrise = (data['results']['sunrise'].split("T")[1]).split(':')[0]
sunset = (data['results']['sunset'].split("T")[1]).split(':')[0]

######################################################

