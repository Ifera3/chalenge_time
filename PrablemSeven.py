#!python3

import random
import tkinter as tk
from tkinter import *

boatOnBord1 = []
boatOnBord2 = []
missOnBord1 = []
missOnBord2 = []
hitOnBord1 = []
hitOnBord2 = []

class square:
    hit = False
    miss = False
    boat = 0
    cords = [-1,-1]
    button = 0
    disply = "   "
    onBoard = 0

    def gogrt(self,event):
        #print(event)
        global recentcord
        recentcord = event
        #run(self.onBoard)

    def __init__(self,cord,board,window):
        self.cords = cord
        self.onBoard = board
        self.disply = StringVar(window)
        self.button = Button(window, textvariable=self.disply, command=lambda m=self.cords: self.gogrt(m))



window = tk.Tk()
window.attributes('-topmost',True)
window.title('Board')

bordlable1 = Label(window, text='Your Bord', font=('Comic sans MS', 10))
bordlable1.grid(row=1,column=5, columnspan=4)
bordlable2 = Label(window, text='Oponet Bord', font=('Comic sans MS', 10))
bordlable2.grid(row=1,column=16, columnspan=4)

instructions = StringVar(window)
instructions.set("Place boat")
instructionshow = Label(window, textvariable=instructions)
instructionshow.grid(row=13, column=1, columnspan=22)

bordOneLables = []
for i in range(10):
    bordOneLables.append(Label(window, text=f"{10-i:>2}"))
    bordOneLables[i].grid(row=2+i, column=1, padx=2)
for i in range(10):
    bordOneLables.append(Label(window, text=f"{10-i:>2}"))
    bordOneLables[i+10].grid(row=12, column=2+i, padx=2)

bordTwoLables = []
for i in range(10):
    bordTwoLables.append(Label(window, text=f"{10-i:>2}"))
    bordTwoLables[i].grid(row=2+i, column=12, padx=2)
for i in range(10):
    bordTwoLables.append(Label(window, text=f"{10-i:>2}"))
    bordTwoLables[i+10].grid(row=12, column=13+i, padx=2)


def gogrt(event):
    #print(event)
    global recentcord
    recentcord = event
    #run(1)

def gogrt2(event):
    #print(event)
    global recentcord
    recentcord = event
    #run(2)

showlist1 = []
buttonlist1 = []
count = 0
for r in range(10):
    for c in range(10):
        showlist1.append(StringVar(window))
        buttonlist1.append(Button(window, textvariable=showlist1[count], command=lambda m=[r,c]: gogrt(m)))
        count += 1

count = 0 
for r in range(10):
    for c in range(10):
        buttonlist1[count].grid(row=(11-r), column=(c+2), padx=3)
        count += 1
for i in showlist1:
    i.set('   ')

showlist2 = []
buttonlist2 = []
count = 0
for r in range(10):
    for c in range(10):
        showlist2.append(StringVar(window))
        buttonlist2.append(Button(window, textvariable=showlist2[count], command=lambda m=[r,c]: gogrt2(m)))
        count += 1

count = 0 
for i in range(1,11):
    for I in range(1,11):
        buttonlist2[count].grid(row=(12-i), column=(I+12), padx=3)
        count = count+1
for i in showlist2:
    i.set('   ')
#for i in range(len(showlist2)):
#    showlist2[i].set(i)

def updateBoard():
    for boat in boatOnBord1:
        for square in boat:
            showlist1[square[0]][square[1]].set('B')
    for square in hitOnBord2:
        showlist2[square[0]][square[1]].set('H')
    for square in missOnBord2:
        showlist2[square[0]][square[1]].set('M')
    for square in hitOnBord1:
        showlist1[square[0]][square[1]].set('H')
    for square in missOnBord1:
        showlist1[square[0]][square[1]].set('M')

def boatHere(check):
    for square in check:
        if showlist1[square[0]][square[1]].get() == 'B':
            return False
    else:
        return True

window.mainloop()