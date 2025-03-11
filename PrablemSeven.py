#!python3

import random
import tkinter as tk
from tkinter import *

boatsOnBord1 = []
boatsOnBord2 = []
missOnBord1 = []
missOnBord2 = []
hitOnBord1 = []
hitOnBord2 = []
boatData = (('tugboat',2),('sumbarine',3),('destroyer',3),('battelship',4),('carrier',5)) #info on each boat type
tempararyCord1 = [] #place for storing cords for boat placement
placedBoats = 0

class square:
    hit = False
    miss = False
    boat = 0
    cords = [-1,-1]
    button = None
    disply = None
    onBoard = 0

    def gogrt(self,event):
        #print(event)
        global recentcord
        recentcord = event
        run(self.onBoard, self.cords)

    def __init__(self,cord,board,window):
        self.cords = cord
        self.onBoard = board
        #creates button on the game board
        self.disply = StringVar(window)
        self.button = Button(window, textvariable=self.disply, command=lambda m=self.cords: self.gogrt(m))
        if self.onBoard == 1:
            self.button.grid(column=(2+self.cords[0]), row=(11-self.cords[1]), padx=3)
        elif self.onBoard == 2:
            self.button.grid(column=(13+self.cords[0]), row=(11-self.cords[1]), padx=3)
        self.disply.set('   ')

def addBoat(cords):
    global tempararyCord1
    global placedBoats
    newBoat = []
    #print(cords[0]*10+cords[1],cords)
    #checks that not being placed on already exsisting boat to start
    if tempararyCord1 == [] and buttonlist1[cords[0]*10+cords[1]].disply.get() == '   ':
        tempararyCord1 = cords
        buttonlist1[tempararyCord1[0]*10+tempararyCord1[1]].disply.set("T")
    else:
        buttonlist1[tempararyCord1[0]*10+tempararyCord1[1]].disply.set("   ")
        #print('fail')
        #checks for direction of boat being placed
        if cords[0] > tempararyCord1[0] and cords[1] == tempararyCord1[1]:
            for newX in range(boatData[placedBoats][1]):
                #checks that boat being placed is on the board
                if -1 < tempararyCord1[0] + newX < 10:
                    #checks that not being placed on already exsisting boat
                    if buttonlist1[(tempararyCord1[0] + newX)*10 + tempararyCord1[1]].disply.get() == '   ':
                        newBoat.append([tempararyCord1[0] + newX, tempararyCord1[1]])
                    else:
                        tempararyCord1 = []
                        return
                else:
                    tempararyCord1 = []
                    return
        elif cords[0] < tempararyCord1[0] and cords[1] == tempararyCord1[1]:
            for newX in range(boatData[placedBoats][1]):
                #checks that boat being placed is on the board
                if -1 < tempararyCord1[0] - newX < 10:
                    #checks that not being placed on already exsisting boat
                    if buttonlist1[(tempararyCord1[0] - newX)*10 + tempararyCord1[1]].disply.get() == '   ':
                        newBoat.append([tempararyCord1[0] - newX, tempararyCord1[1]])
                    else:
                        tempararyCord1 = []
                        return
                else:
                    tempararyCord1 = []
                    return
        elif cords[0] == tempararyCord1[0] and cords[1] > tempararyCord1[1]:
            for newY in range(boatData[placedBoats][1]):
                #checks that boat being placed is on the board
                if -1 < tempararyCord1[1] + newY < 10:
                    #checks that not being placed on already exsisting boat
                    if buttonlist1[tempararyCord1[0]*10 + (tempararyCord1[1] + newY)].disply.get() == '   ':
                        newBoat.append([tempararyCord1[0], tempararyCord1[1] + newY])
                    else:
                        tempararyCord1 = []
                        return
                else:
                    tempararyCord1 = []
                    return
        elif cords[0] == tempararyCord1[0] and cords[1] < tempararyCord1[1]:
            for newY in range(boatData[placedBoats][1]):
                #checks that boat being placed is on the board
                if -1 < tempararyCord1[1] - newY < 10:
                    #checks that not being placed on already exsisting boat
                    if buttonlist1[tempararyCord1[0]*10 + (tempararyCord1[1] - newY)].disply.get() == '   ':
                        newBoat.append([tempararyCord1[0], tempararyCord1[1] - newY])
                    else:
                        tempararyCord1 = []
                        return
                else:
                    tempararyCord1 = []
                    return
        #adds the boat to the list of placed boats and updated the visuals of the board
        boatsOnBord1.append(newBoat)
        tempararyCord1 = []
        placedBoats += 1
    updateBoard()

def aiPlaceBoats():
    aiBoats = 0 # how many boats the ai has placed
    while aiBoats < 5:
        #random starting point
        cords = [random.randrange(10), random.randrange(10)]
        #randomly selects the direction by creating a positive or negitive constant iin the incremented direction wile the other direction is set to 0 to make it not change
        if random.randrange(1) == 1:
            modX = random.choice([1,-1])
            modY = 0
        else:
            modY = random.choice([1,-1])
            modX = 0
        newBoat = [] #list for new boat points
        for i in range(boatData[aiBoats][1]):
            #check if still on the board
            if -1 < cords[0] + (i*modX) < 10 and -1 < cords[1] + (i*modY) < 10:
                #print(aiBoats,cords,i,(i*modX),(i*modY),(cords[0] + (i*modX))*10 + (cords[1] + (i*modY)),[cords[0] + (i*modX), cords[1] + (i*modY)])
                #makes sure it dosen't place ontop of other boats
                if buttonlist2[(cords[0] + (i*modX))*10 + (cords[1] + (i*modY))].disply.get() == '   ':
                    newBoat.append([cords[0] + (i*modX), cords[1] + (i*modY)])
                else:
                    break
            else:
                break
            #updateBoard()
        else: #only runs if all point for the boat where placed corectly
            boatsOnBord2.append(newBoat)
            aiBoats += 1
            updateBoard()



def run(bord,cords):
    #gets run when a button is pushed
    #print(boatsOnBord1,len(boatsOnBord1))
    if bord == 1 and len(boatsOnBord1) < 5:
        addBoat(cords)
    elif bord == 2:
        shoot()
    if len(boatsOnBord1) == 5 and len(boatsOnBord2) == 0:
        aiPlaceBoats()

#creats the window and forces it to be on top of all other windows
window = tk.Tk()
window.attributes('-topmost',True)
window.title('Board')

#creats the labes for the boards
bordOneLable = Label(window, text='Your Bord', font=('Comic sans MS', 10))
bordOneLable.grid(row=1,column=5, columnspan=4)
bordTwoLable2 = Label(window, text='Oponet Bord', font=('Comic sans MS', 10))
bordTwoLable2.grid(row=1,column=16, columnspan=4)

#creats the instructions for the player as a label with a varuble text
instructions = StringVar(window) 
instructionLabel = Label(window, textvariable=instructions)
instructionLabel.grid(row=13, column=1, columnspan=22)

#Creats the labes for board one
bordOneLables = []
for i in range(10):
    bordOneLables.append(Label(window, text=f"{10-i:>2}"))
    bordOneLables[i].grid(row=2+i, column=1, padx=2)
for i in range(10):
    bordOneLables.append(Label(window, text=f"{10-i:>2}"))
    bordOneLables[i+10].grid(row=12, column=2+i, padx=2)

#Creats the labes for board two
bordTwoLables = []
for i in range(10):
    bordTwoLables.append(Label(window, text=f"{10-i:>2}"))
    bordTwoLables[i].grid(row=2+i, column=12, padx=2)
for i in range(10):
    bordTwoLables.append(Label(window, text=f"{10-i:>2}"))
    bordTwoLables[i+10].grid(row=12, column=13+i, padx=2)

#adds the squares as objects that have all their info such as cords, board, and their varuble text
buttonlist1 = []
buttonlist2 = []
for c in range(10):
    for r in range(10):
        buttonlist1.append(square([c,r],1,window))
for c in range(10):
    for r in range(10):
        buttonlist2.append(square([c,r],2,window))
        #print(buttonlist2[-1].cords, buttonlist2.index(buttonlist2[-1]),r*10+c)

def updateBoard():
    #Updates what is being disblaed on the board
    for boat in boatsOnBord1:
        for square in boat:
            #print(square,'place',square[0]*10+square[1])
            buttonlist1[square[0]*10+square[1]].disply.set('B')
    for square in hitOnBord1:
        buttonlist1[square[0]*10+square[1]].disply.set('H')
    for square in missOnBord1:
        buttonlist1[square[0]*10+square[1]].disply.set('M')
    '''for boat in boatsOnBord2:
        for square in boat:
            #print(square,'place',square[0]*10+square[1])
            buttonlist2[square[0]*10+square[1]].disply.set('B')'''
    for square in hitOnBord2:
        buttonlist2[square[0]*10+square[1]].disply.set('H')
    for square in missOnBord2:
        buttonlist2[square[0]*10+square[1]].disply.set('M')

window.mainloop()