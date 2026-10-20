import requests 
url = "https://api.open-meteo.com/v1/forecast?latitude=46.2389&longitude=14.3556&hourly=temperature_2m&current=temperature_2m&timezone=Europe%2FBerlin"

klic = requests.get(url)#.json()

klicJSON= klic.json()

print(klicJSON["current"])


