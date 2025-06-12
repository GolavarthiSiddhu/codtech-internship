import requests
import matplotlib.pyplot as plt

API_KEY = '6386caabc6357f53744f727d4e815343'
CITY = 'Hyderabad'
URL = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

response = requests.get(URL)
data = response.json()

dates = []
temperatures = []

for item in data['list']:
    dates.append(item['dt_txt'])
    temperatures.append(item['main']['temp'])

plt.figure(figsize=(10, 5))
plt.plot(dates[:10], temperatures[:10], marker='o', color='blue')
plt.xticks(rotation=45)
plt.title(f"Weather Forecast for {CITY}")
plt.xlabel("Date and Time")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.grid(True)
plt.show()
