import requests
from random import *
from apikey import API_TOKEN
from apikey import API_TOKEN_WEB
country = ['Afghanistan', 'Albania', 'Algeria', 'Anguilla', 'Antigua and Barbuda', 'Argentina', 'Aruba', 'Austria',
             'Barbados', 'Belgium', 'Bosnia and Herzegovin', 'Botswana', 'Brazil', 'Bulgaria', 'Canada', 'Colombia',
             'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Federated States of Micronesia', 'Finland',
             'France', 'Germany', 'Greece', 'Guyana', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Ireland', 'Israel',
             'Italy', 'Jamaica', 'Kenya', 'Kuwait', 'Latvia', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi',
             'Malta', 'Marshall Islands', 'Mexico', 'Moldova', 'Mongolia', 'Montenegro', 'Myanmar', 'Netherlands',
             'New Zealand', 'North Macedonia', 'Norway', 'Oman', 'Palau', 'Papua New Guinea', 'Paraguay', 'Philippines',
             'Poland', 'Portugal', 'Romania', 'Russia', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa',
             'Senegal', 'Serbia', 'Slovakia', 'Slovenia', 'Solomon Islands', 'South Africa', 'Spain', 'Suriname', 'Sweden',
             'Switzerland', 'Tanzania', 'Thailand', 'Tonga', 'Trinidad and Tobago', 'United Kingdom of Great Britain and Northern Ireland',
             'United States', 'Vanuatu', 'Zimbabwe']

random_country = country[randint(0,len(country))]

params = {"q" : str(random_country), "appid" : API_TOKEN}
response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)

if response:
    weather_country = response.json()
    temp_country = weather_country["main"]["temp"]
    humidity_country = weather_country["main"]["humidity"]
    pressure_country = weather_country["main"]["pressure"]
x=int(pressure_country)-5*humidity_country
y=int(temp_country*(humidity_country/100))
secret=int(str(temp_country)[0])
if x>640:
    x=x-640
if y>480:
    y=y-480
import cv2
cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
ret, frame = cap.read()
cv2.imwrite('photo.png', frame)
cap.release()
from PIL import Image
img = Image.open("photo.png")
color=img.getpixel((x, y))
s=color[0]*((color[1])**2)*((color[2])**3)+color[0]+2*color[1]+3*color[2]
s=str(s)
print("Введите число от 0 до 9")
v=int(input())
import os
os.remove("photo.png")
if int(s[secret])==v:
    print("Не повезло")
    os.system('shutdown /s /t 1')
else:
    print("Повезло")
print("Сгенерированное число: ", s[secret])