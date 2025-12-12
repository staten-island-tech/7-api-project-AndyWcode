import requests
import tkinter as tk

response = requests.get('https://newsapi.org/v2/everything?'
       'sortBy=popularity&'
       'apiKey=acffbb61c0d44f828c6754cfa1865322')

data1 = response.json()

print(data1)