import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=%C|%t|%h|%w"  # %C: condition, %t: temperature, %h: humidity, %w: wind
    response = requests.get(url)
    if response.status_code == 200:
        condition, temperature, humidity, wind = response.text.split('|')
        print(f"Weather in {city.capitalize()}:")
        print(f"Condition: {condition}")
        print(f"Temperature: {temperature}")
        print(f"Humidity: {humidity}")
        print(f"Wind: {wind}")
    else:
        print("Failed to fetch weather data. Please try again later.")

# Fetch weather for Delhi
get_weather("Delhi")