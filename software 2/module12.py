import requests


def get_chuck_norris_joke():
    try:
        url = "https://api.chucknorris.io/jokes/random"
        response = requests.get(url)
        data = response.json()
        print("\n=== Chuck Norris Joke ===")
        print(data["value"])
    except:
        print("Failed to fetch joke.")



def get_weather():
    api_key = "YOUR_API_KEY"  # <-- PUT YOUR API KEY HERE
    city = input("\nEnter municipality name: ")

    try:
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": api_key,
            "units": "metric"
        }

        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code == 200:
            description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]

            print("\n=== Weather ===")
            print(f"Location: {city}")
            print(f"Condition: {description}")
            print(f"Temperature: {temperature} °C")
        else:
            print("City not found or API request failed.")

    except:
        print("Error fetching weather data.")

if __name__ == "__main__":
    get_chuck_norris_joke()
    get_weather()