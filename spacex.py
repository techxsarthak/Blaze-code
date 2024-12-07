import requests

def get_launches():
    url = "https://api.spacexdata.com/v4/launches"
    response = requests.get(url)
    if response.status_code == 200:
        launches = response.json()
        for launch in launches[:5]:  # Display first 5 launches
            print(f"Launch Name: {launch['name']}")
            print(f"Date: {launch['date_utc']}")
            print(f"Rocket: {launch['rocket']}")
            print("-------------------------")
    else:
        print("Failed to fetch launches.")

get_launches()
