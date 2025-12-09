
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
    {"name":"Mercy", "image":"C:\\Users\\andyw68\\Pictures\\mercy.png"},
    {"name":"Genji", "image":"C:\\Users\\andyw68\\Pictures\\Genji.webp"},
    {"name":"Orisa", "image":"C:\\Users\\andyw68\\Pictures\\Orisa.webp"},
    {"name":"Tracer"       , "image":                                      },
    {"name":"Juno"     , "image":                                      },
    {"name":"Reinhart"   , "image":                                      },
    {"name":"Winston"       , "image":                                      },
    {"name":"Roadhog"       , "image":                                      },
    {"name":"D.va"       , "image":                                      },
    {"name":"Ramattra"       , "image":                                      },
    {"name":"Ashe"      , "image":                                      },
    {"name":"Echo"       , "image":                                      },
    {"name":"Hanzo"       , "image":                                      },
    {"name":"Junkrat"       , "image":                                      },
    {"name":"Ana"       , "image":                                      },
    {"name":"Wuyang"      , "image":                                      },
    {"name":"Lucio"           ,"image":                                     ,}
    {"name":"Life Weaver"            ,"image":                                     ,}
    {"name":              ,"image":                                     ,}
    {"name":              ,"image":                                     ,}
    {"name":              ,"image":                                     ,}
    {"name":              ,"image":                                     ,}
    {"name":              ,"image":                                     ,}
    {"name":              ,"image":                                     ,}
    {"name":              ,"image":                                     ,}
    {"name":              ,"image":                                     ,}
    {"name":              ,"image":                                     ,}
    {"name":              ,"image":                                     ,}
    {"name":              ,"image":                                     ,}
    {"name":              ,"image":                                     ,}
    {"name":              ,"image":                                     ,}
    {"name":              ,"image":                                     ,}
    {"name":              ,"image":                                     ,}
    {"name":              ,"image":                                     ,}
    {"name":              ,"image":                                     ,}
    {"name":              ,"image":                                     ,}
    {"name":              ,"image":                                     ,}

]


window = Tk()
window.geometry("800x800")
window.configure(bg = "grey")
overwatchlabel = Label(window, text = "Input hero:", bg = "white", font = ("Times",15), fg ="black" ).grid(row =4, column =1)
Inputhero = Entry(window, font = "Arial, 20")
deletelabelfunction = []


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
                "Quote": data[heroindex]["quotes"]}
                
        counters = data[heroindex]["counters"]
         
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
        row1= 11
        for matchups, info in counters.items():
            for matchup in  signs:
                if info == matchup["matchup"]:
                    info = matchup["meaning"]
                    labelss = Label(window, text=f"{matchups}:{info}", font = "Times, 15", fg = matchup["bg"], bg = "grey")
                    labelss.grid(row = row1, column= 1)
                    row1 += 2
                    deletelabelfunction.append(labelss)
       
    except:
            
            errorlabel = Label(window, text =  "Please check ur spelling", font = "Arial, 10")
            errorlabel.grid(row = 10, column = 10)
            deletelabelfunction.append(errorlabel)




response = requests.get(f"https://hero-matchups-api.netlify.app/.netlify/functions/api/heroes/")
data1 = response.json()

for hero in data1:
    print(hero["name"])

img = Image.open("C:\\Users\\andyw68\\Pictures\\mercy.png")
photo = ImageTk.PhotoImage(img)

photolabel = Label(window, image = photo)
photolabel.grid(column = 10, row = 20)
photolabel.image = photo
Inputhero.grid(row = 5, column = 1)

enterbutton = Button(window, padx = 50, pady = 5, font = "Times, 15", text = "Search", command=searchhero, bg = "white", fg = "black").grid(row = 6, column = 1)


window.mainloop()