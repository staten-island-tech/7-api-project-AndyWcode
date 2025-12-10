from PIL import Image, ImageTk
import tkinter
from tkinter import *

window = Tk()
window.geometry("1000x1000")


pictures_heros = [
    {"name": "Ana", "img": "C:\\Users\\andyw68\\Pictures\\Ana.webp"},
    {"name": "Ashe", "img": "C:\\Users\\andyw68\\Pictures\\Ashe.webp"},
    {"name": "Baptiste", "img": "C:\\Users\\andyw68\\Pictures\\Baptiste.webp"},
    {"name": "Bastion", "img": "C:\\Users\\andyw68\\Pictures\\Bastion.jpg"},
    {"name": "Brigitte", "img": "C:\\Users\\andyw68\\Pictures\\Brigitte.webp"},
    {"name": "Cassidy", "img": "C:\\Users\\andyw68\\Pictures\\Cassidy.webp"},
    {"name": "D.Va", "img": "C:\\Users\\andyw68\\Pictures\\DVa.webp"},
    {"name": "Doomfist", "img": "C:\\Users\\andyw68\\Pictures\\Doomfist.webp"},
    {"name": "Echo", "img": "C:\\Users\\andyw68\\Pictures\\Echo.webp"},
    {"name": "Genji", "img": "C:\\Users\\andyw68\\Pictures\\Genji.webp"},
    {"name": "Hanzo", "img": "C:\\Users\\andyw68\\Pictures\\Hanzo.webp"},
    {"name": "Illari", "img": "C:\\Users\\andyw68\\Pictures\\Illari.webp"},
    {"name": "Junker Queen", "img": "C:\\Users\\andyw68\\Pictures\\JunkerQueen.webp"},
    {"name": "Junkrat", "img": "C:\\Users\\andyw68\\Pictures\\Junkrat.webp"},
    {"name": "Kirishima (Kiriko)", "img": "C:\\Users\\andyw68\\Pictures\\Kiriko.webp"},
    {"name": "Lifeweaver", "img": "C:\\Users\\andyw68\\Pictures\\Lifeweaver.webp"},
    {"name": "Lucio", "img": "C:\\Users\\andyw68\\Pictures\\Lucio.webp"},
    {"name": "Mauga", "img": "C:\\Users\\andyw68\\Pictures\\Mauga.webp"},
    {"name": "Mei", "img": "C:\\Users\\andyw68\\Pictures\\Mei.webp"},
    {"name": "Mercy", "img": "C:\\Users\\andyw68\\Pictures\\Mercy.png"},
    {"name": "Moira", "img": "C:\\Users\\andyw68\\Pictures\\Moira.webp"},
    {"name": "Orisa", "img": "C:\\Users\\andyw68\\Pictures\\Orisa.webp"},
    {"name": "Pharah", "img": "C:\\Users\\andyw68\\Pictures\\Pharah.webp"},
    {"name": "Ramattra", "img": "C:\\Users\\andyw68\\Pictures\\Ramattra.webp"},
    {"name": "Reaper", "img": "C:\\Users\\andyw68\\Pictures\\Reaper.webp"},
    {"name": "Reinhardt", "img": "C:\\Users\\andyw68\\Pictures\\Reinhardt.webp"},
    {"name": "Roadhog", "img": "C:\\Users\\andyw68\\Pictures\\Roadhog.webp"},
    {"name": "Sigma", "img": "C:\\Users\\andyw68\\Pictures\\Sigma.webp"},
    {"name": "Sojourn", "img": "C:\\Users\\andyw68\\Pictures\\Sojourn.webp"},
    {"name": "Soldier: 76", "img": "C:\\Users\\andyw68\\Pictures\\Soldier76.webp"},
    {"name": "Sombra", "img": "C:\\Users\\andyw68\\Pictures\\Sombra.webp"},
    {"name": "Symmetra", "img": "C:\\Users\\andyw68\\Pictures\\Symmetra.webp"},
    {"name": "Torbjörn", "img": "C:\\Users\\andyw68\\Pictures\\Torbjorn.webp"},
    {"name": "Tracer", "img": "C:\\Users\\andyw68\\Pictures\\Tracer.webp"},
    {"name": "Venture", "img": "C:\\Users\\andyw68\\Pictures\\Venture.webp"},
    {"name": "Widowmaker", "img": "C:\\Users\\andyw68\\Pictures\\Widowmaker.webp"},
    {"name": "Winston", "img": "C:\\Users\\andyw68\\Pictures\\Winston.webp"},
    {"name": "Wrecking Ball", "img": "C:\\Users\\andyw68\\Pictures\\WreckingBall.webp"},
    {"name": "Zarya", "img": "C:\\Users\\andyw68\\Pictures\\Zarya.webp"},
    {"name": "Zenyatta", "img": "C:\\Users\\andyw68\\Pictures\\Zenyatta.webp"}
]

img1 = Image.open(pictures_heros[1]["img"])
photo = ImageTk.PhotoImage(img1)

photolabel = Label(window, image = photo)
photolabel.grid(column = 10, row = 20)
photolabel.image = photo

window.mainloop()