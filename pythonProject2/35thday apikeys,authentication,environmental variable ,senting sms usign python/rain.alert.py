from requests import get
from twilio.rest import Client
# on python anywhere
# from twilio.http.http_client import TwilioHttpClient
from os import environ

#to set the environmental variable for the security purpose

aucc_sid = environ.get('ACC_SID')
auth_token = environ.get('auth_token')
API_KEY = environ.get('api_key')
# for the authentication api_key to protect these keys
# please use environmental variable to avoid problems
lat_long = (11.069255, 77.107141)
link_api = 'https://api.openweathermap.org/data/2.5/onecall?lat=11.069255&lon=77.107141&exclude=daily,current,minutely&appid=ea93dc93d91cde6bd74f0adc08f8b4e5'

response = get(link_api)
response.raise_for_status()
data_json = response.json()

dat_lis_12_hours = []
for i in range(0, 12):
    dat_lis_12_hours.append(data_json['hourly'][i]['weather'][0])
print(dat_lis_12_hours)

endgame = False
i = 0
body = f"subject :weather condition:{dat_lis_12_hours[i]['main']}\nexcepted{dat_lis_12_hours[i]['main']} in just {i + 1}hours\ndescription:{dat_lis_12_hours[i]['description']}\nNote : please take the umbrella"
while not endgame:
    weather_id = dat_lis_12_hours[i]['id']
    print(weather_id)
    if weather_id < 700:
        # on python anywhere
        # proxy_client = TwilioHttpClient()
        # proxy_client.session.proxies={'https':environ['https_proxy']}
        client = Client(aucc_sid, auth_token)

        message = client.messages \
            .create(
            body=f"Recipient:Santhosh"
                 f":weather condition:{dat_lis_12_hours[i]['main']}\n\n"
                 f"excepted{dat_lis_12_hours[i]['main']} in just {i + 1}hours\ndescription:{dat_lis_12_hours[i]['description']}\nNote : please take the umbrella",
            from_='+14043345380',
            to= "+917305227758"
        )
        
        print(message.status)

        #             .create(

        #             from="",
        #             to="+917305227758"
        # )

        endgame = True
    i += 1
