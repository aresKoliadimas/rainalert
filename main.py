import requests

MY_API = "###"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": 40.640064,
    "lon": 22.944420,
    "appid": MY_API,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
tw_data = weather_data['hourly'][0:12]

will_rain = False
for hour in tw_data:
    for weather in hour['weather']:
        if int(weather['id']) < 700:
            will_rain = True

if will_rain:
    print("Bring an umbrella")
