import requests

api_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = input("Enter your api key: ")

weather_params = {
    "lat": 43.65,
    "lon": 79.38,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(api_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# Get the next 12 hours of weather data
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    weather_code = hour_data["weather"][0]["id"]

    if (int(weather_code) < 700):
        will_rain = True

if will_rain:
    print("Bring an umbrella")

