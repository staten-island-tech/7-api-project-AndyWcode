
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

userip = input()
response = requests.get(f"https://ip-intelligence.abstractapi.com/v1/?api_key=2583a7c56c30406c80e08a18c7db5df2&ip_address={userip}")
data = response.json()
print(data["location"]["city"])