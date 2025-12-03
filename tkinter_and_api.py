
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


signs = [
{ "matchup":"-", "meaning":"PRETTY BAD", "bg":"red"},
{ "matchup":"--","meaning":"DO NOT PICK AGAINST","bg": "dark red" },
{ "matchup":"+", "meaning":"WONT HURT PICKING IT", "bg": "green"},
{ "matchup":"++","meaning":"MUST PICK AGAINST", "bg":"lime green"}]

window = Tk()
window.geometry("600x600")
overwatchlabel = Label(window, text = "Input what hero:").pack()
Inputhero = Entry(window, font = "Arial, 20")
deletelabelfunction = []


def searchhero():
    
    #  dis is to delete stuff whenever somethign else is searched
    enteredhero = Inputhero.get()
    if len(deletelabelfunction) >=1:
        print(deletelabelfunction)
        for label in deletelabelfunction:
            label.destroy()
        deletelabelfunction.clear()
        
    
    # test userinput
    try:
        response = requests.get(f"https://hero-matchups-api.netlify.app/.netlify/functions/api/heroes/{enteredhero.title()}")

        if response.status_code == 200:
            data = response.json()
            for hero in requests.get("https://hero-matchups-api.netlify.app/.netlify/functions/api/heroes"):
                if enteredhero.title() == hero["name"]:

                    important_info = {
                        "name":data[hero["name"]]["name"],
                        "type":data[hero["name"]]["type"],
                        "archetype":data[hero["name"]]["archetype"]}
                
            counters = data[hero["name"]]["counters"]
                        
            #give user response
            for key, info in important_info.items():
                labels = Label(text =f"{key}:{info}", font = "Arial 10")
                labels.pack()
                deletelabelfunction.append(labels)

            matchuplabel = Label(text = "MATCHUPS", font = ("Arial", 20, "bold"))
            matchuplabel.pack()
            deletelabelfunction.append(matchuplabel)

                # converts the -, --, +, ++ into text so reader knows wat they mean
            for matchups, info in counters.items():
                for matchup in  signs:
                    if info == matchup["matchup"]:
                        info = matchup["meaning"]
                        labelss = Label(window, text=f"{matchups}:{info}", font = "Arial, 10", bg = matchup["bg"])
                        labelss.pack()
                        deletelabelfunction.append(labelss)
    except:
            errorlabel = Label(window, text =  "Please check ur spelling", font = "Arial, 10")
            errorlabel.pack()
            deletelabelfunction.append(errorlabel)
    
    

Inputhero.pack()

enterbutton = Button(window, padx = 10, pady = 10, font = "Arial, 15", text = "Search", command=searchhero).pack()



window.mainloop()