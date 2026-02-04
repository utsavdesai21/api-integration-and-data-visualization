import requests
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

API_KEY = "a0c2c75a5ee6cf512393fd7ef212a1b4"
CITIES = ["Ahmedabad", "Mumbai", "Delhi", "Bangalore"]

weather_data = []

for city in CITIES:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_data.append({
            "City": city,
            "Temperature (°C)": data["main"]["temp"],
            "Feels Like (°C)": data["main"]["feels_like"],
            "Humidity (%)": data["main"]["humidity"],
            "Pressure (hPa)": data["main"]["pressure"]
        })
    else:
        print(f"API error for {city}: {data.get('message')}")

# ❗ Stop if no data was fetched
if not weather_data:
    print("\n❌ No valid weather data fetched.")
    print("➡️ Wait 10–15 minutes for API key activation, then run again.")
    exit()

df = pd.DataFrame(weather_data)

sns.set(style="whitegrid")

plt.figure(figsize=(8,5))
sns.barplot(x="City", y="Temperature (°C)", data=df)
plt.title("City-wise Temperature Comparison")
plt.savefig("temperature_dashboard.png")
plt.show()

plt.figure(figsize=(8,5))
sns.lineplot(x="City", y="Humidity (%)", data=df, marker="o")
plt.title("Humidity Comparison")
plt.savefig("humidity_dashboard.png")
plt.show()