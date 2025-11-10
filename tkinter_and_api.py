from tkinter import *
import random



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



