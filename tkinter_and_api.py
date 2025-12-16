
import time


""" rank = [{"Rank":"loser", "buffs": 1},
        {"Rank":"geek", "buffs": 3},
        {"Rank":"normal", "buffs": 5},
        {"Rank":"cool", "buffs": 8},
        {"Rank":"amazing", "buffs": 11},
        {"Rank":"Peak", "buffs": 15}]


window = Tk()
window.geometry("600x600")
window.title("Clicker Game!")


number = 0 
level = 0
rebirth = rank[level]["buffs"]
multiplyer = 50*rebirth
def clicker():
    global number
    number += 1 * multiplyer
    infoshower.config(text = number)
def upgrade():
    global number
    global multiplyer
    if number >= 100 *2*multiplyer:
        multiplyer += 1
        number = 0
    
    multiplyershower.config(text=multiplyer)
def rankup():
    def maxlevel():
        print("you are max rank goodjob")
    global multiplyer
    global number
    global level
    global rebirth
    if multiplyer >= 10*(level+1):
        if level == len(rank)-1:
            maxlevel()
        else:
            level +=1
            multiplyer = 1 * rank[level]["buffs"]
            number = 0
            rankupbutton.config(text=rank[level]["Rank"])
            multiplyershower.config(text=multiplyer)
            infoshower.config(text = number)




#clicker
clickingbutton = Button(window,text="click!", padx=50, pady=50, bg="gold", font=("Arial, 22"), command=clicker)

#shows the number they have at the moment
infoshower = Label(window,text=number, padx =100, pady = 100, font="Arial, 30")

#shows their click multi
multiplyershower = Label(window,text = multiplyer, padx=25, pady = 25, font="Arial, 30",bg = "gold")

#upgrade button 
upgradebutton = Button(window, text = "Upgrade!", padx = 25, pady = 25, font =("Arial,15"), command = upgrade)

#rankup button
rankupbutton = Button(window, text = rank[level]["Rank"], padx=10, pady = 10, font = "Arial, 10", command=rankup)

infoshower.pack()
multiplyershower.pack()
clickingbutton.pack()
upgradebutton.pack()
rankupbutton.pack()
window.mainloop() """

import tkinter 
from tkinter import *
import requests



# enter stuff
""" enterpokemon = Entry(window,font = "Arial, 15")


def enterbutton():
    pokemonentered = enterpokemon.get()
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemonentered.lower()}")
    if response.status_code != 200:
        labelerror = True
        if labelerror == True:
            Label(window, text = "ERROR, CHECK UR SPELLING",padx=15,pady=15,font="Arial,20", bg="Red").grid(row=10,column=10)
            window.after(2)
        
        return
    elif pokemonentered == "":
        return
    data = response.json()
    all_stuff = {
        "name": data["name"],
        "height": data["height"],
        "weight": f"{data["weight"]}lbs",
        "types": [t["type"]["name"] for t in data["types"]]
        }
    row = 7
    labelerror = False
    for key, stuff in all_stuff.items():
        Label(window, text = f"{key}: {stuff}",padx = 5, pady=5, font= "Arial, 15",bg ="Light Blue" ).grid(row=row, column=3)
        row += 5
    



# sumbit and do it
sumbitbutton = Button(window, text = "Enter", command=enterbutton, padx = 5, pady=5)
enterpokemon.grid(row = 4, column=5)
sumbitbutton.grid(row=4,column = 6)

window.mainloop() """

# enter stuff


# favorites = []


# def get_fact():
#     response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
#     data = response.json()  
#     text1 = data["text"]
#     Label(text =data["text"], font = ("Comic Sans MS", 15)).pack()
#     def favoriteing():
#         global favorites
#         favorites.append(data["text"])
#     favorite = Button(text= 'I like this', font="Arial, 10",command=favoriteing).pack()

# def showfavorites():
#     favoriteswindow = Tk()
#     favoriteswindow.geometry("300x300")
#     Label(favoriteswindow, text = "Your favorites", font = ("Times New Roman", 15), bg = "red").pack()
#     for fact in favorites:
#         makefact = Label(favoriteswindow, text =fact, font = "Arial, 12").pack()


# Getfactbutton = Button(text = "get fact", command = get_fact,padx=50, pady= 10, font = "Arial,10").pack()
# Favbutton = Button(text = "Show ur favorite facts",command = showfavorites, padx = 10, pady = 10, font="Arial, 15").pack()
from PIL import Image, ImageTk


signs = [
{ "matchup":"-", "meaning":"PRETTY BAD", "bg":"red"},
{ "matchup":"--","meaning":"DO NOT PICK AGAINST","bg": "dark red" },
{ "matchup":"+", "meaning":"WONT HURT PICKING IT", "bg": "green"},
{ "matchup":"++","meaning":"MUST PICK AGAINST", "bg":"lime green"}]

pictures_heros = [
    {"name": "Ana", "image": "C:\\Users\\andyw68\\Pictures\\Ana.webp"},
    {"name": "Ashe", "image": "C:\\Users\\andyw68\\Pictures\\Ashe.webp"},
    {"name": "Baptiste", "image": "C:\\Users\\andyw68\\Pictures\\Baptiste.webp"},
    {"name": "Bastion", "image": "C:\\Users\\andyw68\\Pictures\\Bastion.jpg"},
    {"name": "Brigitte", "image": "C:\\Users\\andyw68\\Pictures\\Brigitte.webp"},
    {"name": "Cassidy", "image": "C:\\Users\\andyw68\\Pictures\\Cassidy.webp"},
    {"name": "D.Va", "image": "C:\\Users\\andyw68\\Pictures\\DVa.webp"},
    {"name": "Doomfist", "image": "C:\\Users\\andyw68\\Pictures\\Doomfist.jpg"},
    {"name": "Echo", "image": "C:\\Users\\andyw68\\Pictures\\Echo.webp"},
    {"name": "Genji", "image": "C:\\Users\\andyw68\\Pictures\\Genji.webp"},
    {"name": "Hanzo", "image": "C:\\Users\\andyw68\\Pictures\\Hanzo.webp"},
    {"name": "Illari", "image": "C:\\Users\\andyw68\\Pictures\\Illari.webp"},
    {"name": "Junker Queen", "image": "C:\\Users\\andyw68\\Pictures\\JunkerQueen.webp"},
    {"name": "Junkrat", "image": "C:\\Users\\andyw68\\Pictures\\Junkrat.webp"},
    {"name": "Kiriko", "image": "C:\\Users\\andyw68\\Pictures\\Kiriko.webp"},
    {"name": "Lifeweaver", "image": "C:\\Users\\andyw68\\Pictures\\Lifeweaver.webp"},
    {"name": "Lucio", "image": "C:\\Users\\andyw68\\Pictures\\Lucio.webp"},
    {"name": "Mauga", "image": "C:\\Users\\andyw68\\Pictures\\Mauga.webp"},
    {"name": "Mei", "image": "C:\\Users\\andyw68\\Pictures\\Mei.webp"},
    {"name": "Mercy", "image": "C:\\Users\\andyw68\\Pictures\\Mercy.png"},
    {"name": "Moira", "image": "C:\\Users\\andyw68\\Pictures\\Moira.webp"},
    {"name": "Orisa", "image": "C:\\Users\\andyw68\\Pictures\\Orisa.webp"},
    {"name": "Pharah", "image": "C:\\Users\\andyw68\\Pictures\\Pharah.webp"},
    {"name": "Ramattra", "image": "C:\\Users\\andyw68\\Pictures\\rammatra.webp"},
    {"name": "Reaper", "image": "C:\\Users\\andyw68\\Pictures\\Reaper.webp"},
    {"name": "Reinhardt", "image": "C:\\Users\\andyw68\\Pictures\\Reinhardt.webp"},
    {"name": "Roadhog", "image": "C:\\Users\\andyw68\\Pictures\\Roadhog.webp"},
    {"name": "Sigma", "image": "C:\\Users\\andyw68\\Pictures\\Sigma.webp"},
    {"name": "Sojourn", "image": "C:\\Users\\andyw68\\Pictures\\Sojourn.webp"},
    {"name": "Soldier: 76", "image": "C:\\Users\\andyw68\\Pictures\\Soldier76.webp"},
    {"name": "Sombra", "image": "C:\\Users\\andyw68\\Pictures\\Sombra.webp"},
    {"name": "Symmetra", "image": "C:\\Users\\andyw68\\Pictures\\Symmetra.webp"},
    {"name": "Torbjorn", "image": "C:\\Users\\andyw68\\Pictures\\Torbjorn.webp"},
    {"name": "Tracer", "image": "C:\\Users\\andyw68\\Pictures\\Tracer.webp"},
    {"name": "Venture", "image": "C:\\Users\\andyw68\\Pictures\\Venture.webp"},
    {"name": "Widowmaker", "image": "C:\\Users\\andyw68\\Pictures\\Widowmaker.webp"},
    {"name": "Winston", "image": "C:\\Users\\andyw68\\Pictures\\Winston.webp"},
    {"name": "Wrecking Ball", "image": "C:\\Users\\andyw68\\Pictures\\WreckingBall.webp"},
    {"name": "Zarya", "image": "C:\\Users\\andyw68\\Pictures\\Zarya.webp"},
    {"name": "Zenyatta", "image": "C:\\Users\\andyw68\\Pictures\\Zenyatta.webp"}
]


window = Tk()
window.geometry("1200x1200")
window.configure(bg = "grey")
overwatchlabel = Label(window, text = "Input hero:", bg = "white", font = ("Times",15), fg ="black" ).grid(row =4, column =1)
Inputhero = Entry(window, font = "Arial, 20")
deletelabelfunction = []

listofheros = requests.get(f"https://hero-matchups-api.netlify.app/.netlify/functions/api/heroes/")
heroes = listofheros.json()


def suplist():
    Label(window, text = "SUPPORT", font = "Times, 15", fg = "Pink").grid(row = 3, column = 20)
    r0w = 5
    for hero in heroes:
        if hero["type"] == "support":
            h1 = Label(window, text = hero["name"])
            h1.grid(row = r0w, column = 20)
            r0w += 1
def tanklist():
    Label(window, text = "TANKS", font = "Times, 15", fg = "green").grid(row = 3, column = 21)
    r0w = 5
    for hero in heroes:
        if hero["type"] == "tank":
            h1 = Label(window, text = hero["name"])
            h1.grid(row = r0w, column = 21)
            r0w += 1
def damage():
    Label(window, text = "DAMAGE", font = "Times, 15", fg = "red").grid(row = 3, column = 22)
    r0w = 5
    for hero in heroes:
        if hero["type"] == "damage":
            h1 = Label(window, text = hero["name"])
            h1.grid(row = r0w, column = 22)
            r0w += 1


suplist()
tanklist()
damage()

def searchhero():
    
    #  dis is to delete stuff whenever somethign else is searched so its not messy
    
    if len(deletelabelfunction) >=1:
        for label in deletelabelfunction:
            label.destroy()
        deletelabelfunction.clear()
        
    
    # test userinput for the try
    try:
        enteredhero = Inputhero.get()
        response = requests.get(f"https://hero-matchups-api.netlify.app/.netlify/functions/api/heroes/")
        
        if response.status_code != 200:
            raise Exception #<--- yea idk what this does i admit this was ai
        data = response.json()
        for info in data:
            if info["name"] == enteredhero.title():
                heroindex = (data.index(info))
        
        important_info = {
                "Name":data[heroindex]["name"],
                "Type":data[heroindex]["type"],
                "Archetype":data[heroindex]["archetype"],
                "Quote": data[heroindex]["quotes"]
                }
        counters = data[heroindex]["counters"]

        for pictures in pictures_heros:
                if pictures["name"] == enteredhero.title():
                    pictureindex = pictures_heros.index(pictures)
                    img = Image.open(pictures_heros[pictureindex]["image"])
                    img = img.resize((450,450),Image.LANCZOS)
                    photo = ImageTk.PhotoImage(img)
                    photolabel = Label(window, image = photo)
                    deletelabelfunction.append(photolabel)
                    photolabel.grid(column = 4, row = 10, rowspan=20)
                    photolabel.image = photo

        #give user response
        row2 =3
        for key, info in important_info.items():
                labels = Label(text =f"{key}:{info}", font = "Times 15", fg = "yellow", bg = "grey")
                labels.grid(row = row2, column = 4)
                row2 +=1
                deletelabelfunction.append(labels)

        matchuplabel = Label(text = "MATCHUPS", font = ("Arial", 20, "bold"), bg = "grey")
        matchuplabel.grid(row =10, column= 1)
        deletelabelfunction.append(matchuplabel)

        # converts the -, --, +, ++ into text so reader knows wat they mean
        row1= 8
        for matchups, info in counters.items():
            for matchup in  signs:
                if info == matchup["matchup"]:
                    info = matchup["meaning"]
                    labelss = Label(window, text=f"{matchups}:{info}", font = "Times, 15", fg = matchup["bg"], bg = "grey")
                    labelss.grid(row = row1, column= 1)
                    row1 += 1
                    deletelabelfunction.append(labelss)
            
        
    except:
                
        errorlabel = Label(window, text =  "Please check ur spelling and capitlization!", font = "Arial, 10")
        errorlabel.grid(row = 10, column = 10)
        deletelabelfunction.append(errorlabel)









Inputhero.grid(row = 5, column = 1)
enterbutton = Button(window, padx = 50, pady = 5, font = "Times, 15", text = "Search", command=searchhero, bg = "white", fg = "black").grid(row = 6, column = 1)


window.mainloop()