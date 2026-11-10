#mini vaja 1
"""
avto = {
    "znamka": "Audi",
    "model": 8,
    "letnik": "2024"
}
avto["barva"] = "Črna"
print(f"znamka:{avto["znamka"]}")     
print(f"model:{avto["model"]}")     
print(f"letnik:{avto["letnik"]}")     
print(f"barva:{avto["barva"]}") 
"""
#mini vaja 2
"""
sola = {
    "ime": "ŠC Kranj",
    "naslov": {
        "ulica": "Kidričeva cesta 55",
        "posta": 4000,
        "kraj": "Kranj"
    },
    "smeri": ["računalništvo", "elektrotehnika", "mehatronika"]
}


for vrednost in sola["smeri"]:
    print(vrednost)


print(sola["naslov"]["posta"])   
print(sola["smeri"][-1])   
"""
#mini vaja 3
"""
import requests

url = "https://api.open-meteo.com/v1/forecast"
parametri = {
    "latitude": 46.259517,
    "longitude": 14.387113,
    "current": "temperature_2m,wind_speed_10m"
}

odgovor = requests.get(url, params=parametri)
podatki = odgovor.json()

temp = podatki["current"]["temperature_2m"]
enota = podatki["current_units"]["temperature_2m"]
wind = podatki["current"]["wind_speed_10m"]
enota2 = podatki["current_units"]["wind_speed_10m"]
print(f"temperatura je: {temp}{enota}, hitrost vetra je: {wind}{enota2}")  
"""
#mini vaja 4

def trenutna_temperatura(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    parametri = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m"
    }
    odgovor = requests.get(url, params=parametri)
    podatki = odgovor.json()
    return podatki["current"]["temperature_2m"]


kraji = {
    "Ljubljana": (46.0569, 14.5058),
    "Maribor": (46.5547, 15.6459),
}

for ime, (lat, lon) in kraji.items():
    t = trenutna_temperatura(lat, lon)
    print(f"{ime}: {t} °C")

