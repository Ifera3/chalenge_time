#!python3

import random
import tkinter as tk
from tkinter import *

def g():
    global boatDatat
    global cboat
    global ccord
    global recentcord
    global boatB1
    global hitB1
    global missB1
    global sink1
    global boatB2
    global hitB2
    global missB2
    global sink2
    boatDatat = (('tugboat',2),('sumbarine',3),('destroyer',3),('battelship',4),('carrier',5))
    cboat = 0
    ccord = None
    recentcord = None
    boatB1 = []
    hitB1 = []
    missB1 = []
    sink1 = 0
    boatB2 = []
    hitB2 = []
    missB2 = []
    sink2 = 0

    def offBoard(cheek):
        global boatDatat
        global cboat
        global ccord
        global recentcord
        global boatB1
        global hitB1
        global missB1
        global sink1
        global boatB2
        global hitB2
        global missB2
        global sink2
        for i in cheek:
            if i[0] < 0:
                return False
            elif i[0] > 9:
                return False
            elif i[1] < 0:
                return False
            elif i[1] > 9:
                return False
        else:
            return True

    def winning():
        global boatDatat
        global cboat
        global ccord
        global recentcord
        global boatB1
        global hitB1
        global missB1
        global sink1
        global boatB2
        global hitB2
        global missB2
        global sink2
        if sink2 == 5:
            #print('win player 1')
            window.destroy()
            winboard = tk.Tk()
            winboard.attributes('-topmost',True)
            winboard.title('WIN')
            labb = Label(winboard, text='You Win!', font=('Comic Sans MS', 80))
            labb.grid(row=1, column=1)
            ab = Button(winboard, text='Play agen?', font=('Comic Sans MS', 30), border=15)
            ab.grid(row=2, column=1)
            def vhuyj(l):
                winboard.destroy()
                g()
            ab.bind('<Button>', vhuyj)
            winboard.mainloop()
        if sink1 == 5:
            #print('win player 2')
            window.destroy()
            winboard = tk.Tk()
            winboard.attributes('-topmost',True)
            winboard.title('WIN')
            labb = Label(winboard, text='Oponet Wins!', font=('Comic Sans MS', 160))
            labb.grid(row=1, column=1)
            ab = Button(winboard, text='Play agen?', font=('Comic Sans MS', 30), border=15)
            ab.grid(row=2, column=1)
            def vhuyj(l):
                winboard.destroy()
                g()
            ab.bind('<Button>', vhuyj)
            winboard.mainloop()

    def fullList(ships,ocupied):
        global boatDatat
        global cboat
        global ccord
        global recentcord
        global boatB1
        global hitB1
        global missB1
        global sink1
        global boatB2
        global hitB2
        global missB2
        global sink2
        boat = ships[2]
        boatsquare = [ships[0]]
        #print(boatsquare)
        if ships[1] <= 1:
            for i in range(boatDatat[boat][1] - 1):
                #print(boatsquare)
                c = [boatsquare[-1][0],boatsquare[-1][1] + 1]
                boatsquare.append(c)
        elif ships[1] <= 2:
            for i in range(boatDatat[boat][1] - 1):
                #print(boatsquare)
                c = [boatsquare[-1][0],boatsquare[-1][1] - 1]
                boatsquare.append(c)
        elif ships[1] <= 3:
            for i in range(boatDatat[boat][1] - 1):
                #print(boatsquare)
                c = [boatsquare[-1][0] - 1,boatsquare[-1][1]]
                boatsquare.append(c)
        elif ships[1] <= 4:
            for i in range(boatDatat[boat][1] - 1):
                #print(boatsquare)
                c = [boatsquare[-1][0] + 1,boatsquare[-1][1]]
                boatsquare.append(c)
        else:
            xy = [random.randrange(10), random.randrange(10)]
            boatsquare = fullList([xy,ships[1],boat],ocupied)
        failed = False
        for i in ocupied:
            for I in i:
                if I in boatsquare:
                    failed = True
        for i in boatsquare:
            for I in i:
                if I < 0 or I > 9:
                    failed = True
        if failed:
            xy = [random.randrange(10), random.randrange(10)]
            boatsquare = fullList([xy,ships[1],boat],ocupied)
        return boatsquare

    def run(bord):
        global boatDatat
        global cboat
        global ccord
        global recentcord
        global boatB1
        global hitB1
        global missB1
        global sink1
        global boatB2
        global hitB2
        global missB2
        global sink2
        boatsquare = []
        if cboat < 5 and ccord == None and bord == 1:
            #print(ccord, recentcord)
            ccord = recentcord
        elif cboat < 5 and ccord != None and recentcord != ccord and bord == 1:
            #print(ccord, recentcord)
            for i in range(10):
                if recentcord == [ccord[0]+i,ccord[1]]:
                    #print('U')
                    for i in range(boatDatat[cboat][1]):
                        c = [ccord[0]+i,ccord[1]]
                        boatsquare.append(c)
                elif recentcord == [ccord[0],ccord[1]+i]:
                    #print('R')
                    for i in range(boatDatat[cboat][1]):
                        c = [ccord[0],ccord[1]+i]
                        boatsquare.append(c)
                elif recentcord == [ccord[0]-i,ccord[1]]:
                    #print('D')
                    for i in range(boatDatat[cboat][1]):
                        c = [ccord[0]-i,ccord[1]]
                        boatsquare.append(c)
                elif recentcord == [ccord[0],ccord[1]-i]:
                    #print('L')
                    for i in range(boatDatat[cboat][1]):
                        c = [ccord[0],ccord[1]-i]
                        boatsquare.append(c)
            #print(boatsquare)
            if boatHere(boatsquare) and boatsquare != [] and offBoard(boatsquare):
                boatB1.append(boatsquare)
                cboat = cboat + 1
            ccord = None
        elif cboat > 5 and bord == 2:
            #after creat square hit enamy bord
            for i in boatB2:
                if recentcord in i and recentcord not in hitB2:
                    i.remove(recentcord)
                    hitB2.append(recentcord)
                    for i in range(len(hitB1)):
                        k = len(hitB1) - i - 1
                        #print(k)
                        if hitB1 != []:
                            #print(hitB1)
                            aicord = [hitB1[k][0]+1,hitB1[k][1]]
                            #print(aicord)
                            if aicord in hitB1 or aicord in missB1 or aicord[0] < 0 or aicord[0] > 9 or aicord[1] < 0 or aicord[1] > 9:
                                aicord = [hitB1[k][0]-1,hitB1[k][1]]
                                #print(aicord)
                                if aicord in hitB1 or aicord in missB1 or aicord[0] < 0 or aicord[0] > 9 or aicord[1] < 0 or aicord[1] > 9:
                                    aicord = [hitB1[k][0],hitB1[k][1]+1]
                                    #print(aicord)
                                    if aicord in hitB1 or aicord in missB1 or aicord[0] < 0 or aicord[0] > 9 or aicord[1] < 0 or aicord[1] > 9:
                                        aicord = [hitB1[k][0],hitB1[k][1]-1]
                                        #print(aicord)
                        else:
                            while aicord in missB1 or aicord in hitB1 or aicord[0] < 0 or aicord[0] > 9 or aicord[1] < 0 or aicord[1] > 9:
                                #print(777)
                                aicord = [random.randrange(10), random.randrange(10)]
                        if aicord not in missB1 and aicord not in hitB1 and type(aicord) == list and -1 < aicord[0] < 10 and -1 < aicord[1] < 10:
                            #print(aicord)
                            break
                    else:
                        #print(888)
                        aicord = [random.randrange(10), random.randrange(10)]
                        while aicord in missB1 or aicord in hitB1 or aicord[0] < 0 or aicord[0] > 9 or aicord[1] < 0 or aicord[1] > 9:
                            aicord = [random.randrange(10), random.randrange(10)]
                    #print(aicord)
                    for i in boatB1:
                        if aicord in i:
                            i.remove(aicord)
                            hitB1.append(aicord)
                            break
                    else:
                        missB1.append(aicord)
                    for i in boatB1:
                        if i == []:
                            boatB1.remove([])
                            sink1 = sink1 + 1
                    for i in boatB2:
                        if i == []:
                            boatB2.remove([])
                            sink2 = sink2 + 1 
                    break
            else:
                if recentcord not in hitB2 and recentcord not in missB2:
                    missB2.append(recentcord)
                    #print(666)
                    for i in range(len(hitB1)):
                        k = len(hitB1) - i - 1
                        #print(k)
                        if hitB1 != []:
                            #print(hitB1)
                            aicord = [hitB1[k][0]+1,hitB1[k][1]]
                            #print(aicord)
                            if aicord in hitB1 or aicord in missB1 or aicord[0] < 0 or aicord[0] > 9 or aicord[1] < 0 or aicord[1] > 9:
                                aicord = [hitB1[k][0]-1,hitB1[k][1]]
                                #print(aicord)
                                if aicord in hitB1 or aicord in missB1 or aicord[0] < 0 or aicord[0] > 9 or aicord[1] < 0 or aicord[1] > 9:
                                    aicord = [hitB1[k][0],hitB1[k][1]+1]
                                    #print(aicord)
                                    if aicord in hitB1 or aicord in missB1 or aicord[0] < 0 or aicord[0] > 9 or aicord[1] < 0 or aicord[1] > 9:
                                        aicord = [hitB1[k][0],hitB1[k][1]-1]
                                        #print(aicord)
                        else:
                            while aicord in missB1 or aicord in hitB1 or aicord[0] < 0 or aicord[0] > 9 or aicord[1] < 0 or aicord[1] > 9:
                                #print(777)
                                aicord = [random.randrange(10), random.randrange(10)]
                        if aicord not in missB1 and aicord not in hitB1 and type(aicord) == list and -1 < aicord[0] < 10 and -1 < aicord[1] < 10:
                            #print(aicord)
                            break
                    else:
                        #print(888)
                        aicord = [random.randrange(10), random.randrange(10)]
                        while aicord in missB1 or aicord in hitB1 or aicord[0] < 0 or aicord[0] > 9 or aicord[1] < 0 or aicord[1] > 9:
                            aicord = [random.randrange(10), random.randrange(10)]
                    #print(aicord)
                    for i in boatB1:
                        #print(aicord)
                        if aicord in i:
                            i.remove(aicord)
                            hitB1.append(aicord)
                            break
                    else:
                        missB1.append(aicord)
                    for i in boatB1:
                        if i == []:
                            boatB1.remove([])
                            sink1 = sink1 + 1
                    for i in boatB2:
                        if i == []:
                            boatB2.remove([])
                            sink2 = sink2 + 1 
        elif cboat > 5 and bord == 1:
            #after creat square hit player bord
            #print(recentcord)
            for i in boatB1:
                if i == []:
                    boatB1.remove([])
                    sink1 = sink1 + 1
            for i in boatB2:
                if i == []:
                    boatB2.remove([])
                    sink2 = sink2 + 1        
        if cboat == 5:
            for i in range(5):
                xy = [random.randrange(10), random.randrange(10)]
                direc = random.randrange(5)
                newboat = [xy,direc,i]

                boatB2.append(fullList(newboat,boatB2))
            cboat = cboat + 1
        #print(boatB1, boatB2, sink1, sink2)
        updateBoard()
        if sink1 == 5:
            winning()
        if sink2 == 5:
            winning()

    window = tk.Tk()
    #print("die")
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

    #---------- Deju Vu land 971 lines 28% of former glory -----------------#
    l1 = Label(window, text='10')
    l2 = Label(window, text='09')
    l3 = Label(window, text='08')
    l4 = Label(window, text='07')
    l5 = Label(window, text='06')
    l6 = Label(window, text='05')
    l7 = Label(window, text='04')
    l8 = Label(window, text='03')
    l9 = Label(window, text='02')
    l10 = Label(window, text='01')
    l11 = Label(window, text=' A ')
    l12 = Label(window, text=' B ')
    l13 = Label(window, text=' C ')
    l14 = Label(window, text=' D ')
    l15 = Label(window, text=' E ')
    l16 = Label(window, text=' F ')
    l17 = Label(window, text=' G ')
    l18 = Label(window, text=' H ')
    l19 = Label(window, text=' I ')
    l20 = Label(window, text=' J ')

    ll1 = Label(window, text='10')
    ll2 = Label(window, text='09')
    ll3 = Label(window, text='08')
    ll4 = Label(window, text='07')
    ll5 = Label(window, text='06')
    ll6 = Label(window, text='05')
    ll7 = Label(window, text='04')
    ll8 = Label(window, text='03')
    ll9 = Label(window, text='02')
    ll10 = Label(window, text='01')
    ll11 = Label(window, text=' A ')
    ll12 = Label(window, text=' B ')
    ll13 = Label(window, text=' C ')
    ll14 = Label(window, text=' D ')
    ll15 = Label(window, text=' E ')
    ll16 = Label(window, text=' F ')
    ll17 = Label(window, text=' G ')
    ll18 = Label(window, text=' H ')
    ll19 = Label(window, text=' I ')
    ll20 = Label(window, text=' J ')
    
    l1.grid(row=2, column=1, padx=2)
    l2.grid(row=3, column=1, padx=2)
    l3.grid(row=4, column=1, padx=2)
    l4.grid(row=5, column=1, padx=2)
    l5.grid(row=6, column=1, padx=2)
    l6.grid(row=7, column=1, padx=2)
    l7.grid(row=8, column=1, padx=2)
    l8.grid(row=9, column=1, padx=2)
    l9.grid(row=10, column=1, padx=2)
    l10.grid(row=11, column=1, padx=2)
    l11.grid(row=12, column=2, padx=3)
    l12.grid(row=12, column=3, padx=3)
    l13.grid(row=12, column=4, padx=3)
    l14.grid(row=12, column=5, padx=3)
    l15.grid(row=12, column=6, padx=3)
    l16.grid(row=12, column=7, padx=3)
    l17.grid(row=12, column=8, padx=3)
    l18.grid(row=12, column=9, padx=3)
    l19.grid(row=12, column=10, padx=3)
    l20.grid(row=12, column=11, padx=3)
    
    ll1.grid(row=2, column=12, padx=2)
    ll2.grid(row=3, column=12, padx=2)
    ll3.grid(row=4, column=12, padx=2)
    ll4.grid(row=5, column=12, padx=2)
    ll5.grid(row=6, column=12, padx=2)
    ll6.grid(row=7, column=12, padx=2)
    ll7.grid(row=8, column=12, padx=2)
    ll8.grid(row=9, column=12, padx=2)
    ll9.grid(row=10, column=12, padx=2)
    ll10.grid(row=11, column=12, padx=2)
    ll11.grid(row=12, column=13, padx=3)
    ll12.grid(row=12, column=14, padx=3)
    ll13.grid(row=12, column=15, padx=3)
    ll14.grid(row=12, column=16, padx=3)
    ll15.grid(row=12, column=17, padx=3)
    ll16.grid(row=12, column=18, padx=3)
    ll17.grid(row=12, column=19, padx=3)
    ll18.grid(row=12, column=20, padx=3)
    ll19.grid(row=12, column=21, padx=3)
    ll20.grid(row=12, column=22, padx=3)

    #0.083% of its former glory
    def gogrt(event):
        #print(event)
        global recentcord
        recentcord = event
        run(1)

    def gogrt2(event):
        #print(event)
        global recentcord
        recentcord = event
        run(2)

    buttonlist1 = []
    showlist1 = []

    boatshow11 = StringVar(window)
    showlist1.append(boatshow11)
    boat11 = Button(window, textvariable=boatshow11, command=lambda m=[0,0]: gogrt(m))
    buttonlist1.append(boat11)
    boatshow12 = StringVar(window)
    showlist1.append(boatshow12)
    boat12 = Button(window, textvariable=boatshow12, command=lambda m=[0,1]: gogrt(m))
    buttonlist1.append(boat12)
    boatshow13 = StringVar(window)
    showlist1.append(boatshow13)
    boat13 = Button(window, textvariable=boatshow13, command=lambda m=[0,2]: gogrt(m))
    buttonlist1.append(boat13)
    boatshow14 = StringVar(window)
    showlist1.append(boatshow14)
    boat14 = Button(window, textvariable=boatshow14, command=lambda m=[0,3]: gogrt(m))
    buttonlist1.append(boat14)
    boatshow15 = StringVar(window)
    showlist1.append(boatshow15)
    boat15 = Button(window, textvariable=boatshow15, command=lambda m=[0,4]: gogrt(m))
    buttonlist1.append(boat15)
    boatshow16 = StringVar(window)
    showlist1.append(boatshow16)
    boat16 = Button(window, textvariable=boatshow16, command=lambda m=[0,5]: gogrt(m))
    buttonlist1.append(boat16)
    boatshow17 = StringVar(window)
    showlist1.append(boatshow17)
    boat17 = Button(window, textvariable=boatshow17, command=lambda m=[0,6]: gogrt(m))
    buttonlist1.append(boat17)
    boatshow18 = StringVar(window)
    showlist1.append(boatshow18)
    boat18 = Button(window, textvariable=boatshow18, command=lambda m=[0,7]: gogrt(m))
    buttonlist1.append(boat18)
    boatshow19 = StringVar(window)
    showlist1.append(boatshow19)
    boat19 = Button(window, textvariable=boatshow19, command=lambda m=[0,8]: gogrt(m))
    buttonlist1.append(boat19)
    boatshow110 = StringVar(window)
    showlist1.append(boatshow110)
    boat110 = Button(window, textvariable=boatshow110, command=lambda m=[0,9]: gogrt(m))
    buttonlist1.append(boat110)
    boatshow21 = StringVar(window)
    showlist1.append(boatshow21)
    boat21 = Button(window, textvariable=boatshow21, command=lambda m=[1,0]: gogrt(m))
    buttonlist1.append(boat21)
    boatshow22 = StringVar(window)
    showlist1.append(boatshow22)
    boat22 = Button(window, textvariable=boatshow22, command=lambda m=[1,1]: gogrt(m))
    buttonlist1.append(boat22)
    boatshow23 = StringVar(window)
    showlist1.append(boatshow23)
    boat23 = Button(window, textvariable=boatshow23, command=lambda m=[1,2]: gogrt(m))
    buttonlist1.append(boat23)
    boatshow24 = StringVar(window)
    showlist1.append(boatshow24)
    boat24 = Button(window, textvariable=boatshow24, command=lambda m=[1,3]: gogrt(m))
    buttonlist1.append(boat24)
    boatshow25 = StringVar(window)
    showlist1.append(boatshow25)
    boat25 = Button(window, textvariable=boatshow25, command=lambda m=[1,4]: gogrt(m))
    buttonlist1.append(boat25)
    boatshow26 = StringVar(window)
    showlist1.append(boatshow26)
    boat26 = Button(window, textvariable=boatshow26, command=lambda m=[1,5]: gogrt(m))
    buttonlist1.append(boat26)
    boatshow27 = StringVar(window)
    showlist1.append(boatshow27)
    boat27 = Button(window, textvariable=boatshow27, command=lambda m=[1,6]: gogrt(m))
    buttonlist1.append(boat27)
    boatshow28 = StringVar(window)
    showlist1.append(boatshow28)
    boat28 = Button(window, textvariable=boatshow28, command=lambda m=[1,7]: gogrt(m))
    buttonlist1.append(boat28)
    boatshow29 = StringVar(window)
    showlist1.append(boatshow29)
    boat29 = Button(window, textvariable=boatshow29, command=lambda m=[1,8]: gogrt(m))
    buttonlist1.append(boat29)
    boatshow210 = StringVar(window)
    showlist1.append(boatshow210)
    boat210 = Button(window, textvariable=boatshow210, command=lambda m=[1,9]: gogrt(m))
    buttonlist1.append(boat210)
    boatshow31 = StringVar(window)
    showlist1.append(boatshow31)
    boat31 = Button(window, textvariable=boatshow31, command=lambda m=[2,0]: gogrt(m))
    buttonlist1.append(boat31)
    boatshow32 = StringVar(window)
    showlist1.append(boatshow32)
    boat32 = Button(window, textvariable=boatshow32, command=lambda m=[2,1]: gogrt(m))
    buttonlist1.append(boat32)
    boatshow33 = StringVar(window)
    showlist1.append(boatshow33)
    boat33 = Button(window, textvariable=boatshow33, command=lambda m=[2,2]: gogrt(m))
    buttonlist1.append(boat33)
    boatshow34 = StringVar(window)
    showlist1.append(boatshow34)
    boat34 = Button(window, textvariable=boatshow34, command=lambda m=[2,3]: gogrt(m))
    buttonlist1.append(boat34)
    boatshow35 = StringVar(window)
    showlist1.append(boatshow35)
    boat35 = Button(window, textvariable=boatshow35, command=lambda m=[2,4]: gogrt(m))
    buttonlist1.append(boat35)
    boatshow36 = StringVar(window)
    showlist1.append(boatshow36)
    boat36 = Button(window, textvariable=boatshow36, command=lambda m=[2,5]: gogrt(m))
    buttonlist1.append(boat36)
    boatshow37 = StringVar(window)
    showlist1.append(boatshow37)
    boat37 = Button(window, textvariable=boatshow37, command=lambda m=[2,6]: gogrt(m))
    buttonlist1.append(boat37)
    boatshow38 = StringVar(window)
    showlist1.append(boatshow38)
    boat38 = Button(window, textvariable=boatshow38, command=lambda m=[2,7]: gogrt(m))
    buttonlist1.append(boat38)
    boatshow39 = StringVar(window)
    showlist1.append(boatshow39)
    boat39 = Button(window, textvariable=boatshow39, command=lambda m=[2,8]: gogrt(m))
    buttonlist1.append(boat39)
    boatshow310 = StringVar(window)
    showlist1.append(boatshow310)
    boat310 = Button(window, textvariable=boatshow310, command=lambda m=[2,9]: gogrt(m))
    buttonlist1.append(boat310)
    boatshow41 = StringVar(window)
    showlist1.append(boatshow41)
    boat41 = Button(window, textvariable=boatshow41, command=lambda m=[3,0]: gogrt(m))
    buttonlist1.append(boat41)
    boatshow42 = StringVar(window)
    showlist1.append(boatshow42)
    boat42 = Button(window, textvariable=boatshow42, command=lambda m=[3,1]: gogrt(m))
    buttonlist1.append(boat42)
    boatshow43 = StringVar(window)
    showlist1.append(boatshow43)
    boat43 = Button(window, textvariable=boatshow43, command=lambda m=[3,2]: gogrt(m))
    buttonlist1.append(boat43)
    boatshow44 = StringVar(window)
    showlist1.append(boatshow44)
    boat44 = Button(window, textvariable=boatshow44, command=lambda m=[3,3]: gogrt(m))
    buttonlist1.append(boat44)
    boatshow45 = StringVar(window)
    showlist1.append(boatshow45)
    boat45 = Button(window, textvariable=boatshow45, command=lambda m=[3,4]: gogrt(m))
    buttonlist1.append(boat45)
    boatshow46 = StringVar(window)
    showlist1.append(boatshow46)
    boat46 = Button(window, textvariable=boatshow46, command=lambda m=[3,5]: gogrt(m))
    buttonlist1.append(boat46)
    boatshow47 = StringVar(window)
    showlist1.append(boatshow47)
    boat47 = Button(window, textvariable=boatshow47, command=lambda m=[3,6]: gogrt(m))
    buttonlist1.append(boat47)
    boatshow48 = StringVar(window)
    showlist1.append(boatshow48)
    boat48 = Button(window, textvariable=boatshow48, command=lambda m=[3,7]: gogrt(m))
    buttonlist1.append(boat48)
    boatshow49 = StringVar(window)
    showlist1.append(boatshow49)
    boat49 = Button(window, textvariable=boatshow49, command=lambda m=[3,8]: gogrt(m))
    buttonlist1.append(boat49)
    boatshow410 = StringVar(window)
    showlist1.append(boatshow410)
    boat410 = Button(window, textvariable=boatshow410, command=lambda m=[3,9]: gogrt(m))
    buttonlist1.append(boat410)
    boatshow51 = StringVar(window)
    showlist1.append(boatshow51)
    boat51 = Button(window, textvariable=boatshow51, command=lambda m=[4,0]: gogrt(m))
    buttonlist1.append(boat51)
    boatshow52 = StringVar(window)
    showlist1.append(boatshow52)
    boat52 = Button(window, textvariable=boatshow52, command=lambda m=[4,1]: gogrt(m))
    buttonlist1.append(boat52)
    boatshow53 = StringVar(window)
    showlist1.append(boatshow53)
    boat53 = Button(window, textvariable=boatshow53, command=lambda m=[4,2]: gogrt(m))
    buttonlist1.append(boat53)
    boatshow54 = StringVar(window)
    showlist1.append(boatshow54)
    boat54 = Button(window, textvariable=boatshow54, command=lambda m=[4,3]: gogrt(m))
    buttonlist1.append(boat54)
    boatshow55 = StringVar(window)
    showlist1.append(boatshow55)
    boat55 = Button(window, textvariable=boatshow55, command=lambda m=[4,4]: gogrt(m))
    buttonlist1.append(boat55)
    boatshow56 = StringVar(window)
    showlist1.append(boatshow56)
    boat56 = Button(window, textvariable=boatshow56, command=lambda m=[4,5]: gogrt(m))
    buttonlist1.append(boat56)
    boatshow57 = StringVar(window)
    showlist1.append(boatshow57)
    boat57 = Button(window, textvariable=boatshow57, command=lambda m=[4,6]: gogrt(m))
    buttonlist1.append(boat57)
    boatshow58 = StringVar(window)
    showlist1.append(boatshow58)
    boat58 = Button(window, textvariable=boatshow58, command=lambda m=[4,7]: gogrt(m))
    buttonlist1.append(boat58)
    boatshow59 = StringVar(window)
    showlist1.append(boatshow59)
    boat59 = Button(window, textvariable=boatshow59, command=lambda m=[4,8]: gogrt(m))
    buttonlist1.append(boat59)
    boatshow510 = StringVar(window)
    showlist1.append(boatshow510)
    boat510 = Button(window, textvariable=boatshow510, command=lambda m=[4,9]: gogrt(m))
    buttonlist1.append(boat510)
    boatshow61 = StringVar(window)
    showlist1.append(boatshow61)
    boat61 = Button(window, textvariable=boatshow61, command=lambda m=[5,0]: gogrt(m))
    buttonlist1.append(boat61)
    boatshow62 = StringVar(window)
    showlist1.append(boatshow62)
    boat62 = Button(window, textvariable=boatshow62, command=lambda m=[5,1]: gogrt(m))
    buttonlist1.append(boat62)
    boatshow63 = StringVar(window)
    showlist1.append(boatshow63)
    boat63 = Button(window, textvariable=boatshow63, command=lambda m=[5,2]: gogrt(m))
    buttonlist1.append(boat63)
    boatshow64 = StringVar(window)
    showlist1.append(boatshow64)
    boat64 = Button(window, textvariable=boatshow64, command=lambda m=[5,3]: gogrt(m))
    buttonlist1.append(boat64)
    boatshow65 = StringVar(window)
    showlist1.append(boatshow65)
    boat65 = Button(window, textvariable=boatshow65, command=lambda m=[5,4]: gogrt(m))
    buttonlist1.append(boat65)
    boatshow66 = StringVar(window)
    showlist1.append(boatshow66)
    boat66 = Button(window, textvariable=boatshow66, command=lambda m=[5,5]: gogrt(m))
    buttonlist1.append(boat66)
    boatshow67 = StringVar(window)
    showlist1.append(boatshow67)
    boat67 = Button(window, textvariable=boatshow67, command=lambda m=[5,6]: gogrt(m))
    buttonlist1.append(boat67)
    boatshow68 = StringVar(window)
    showlist1.append(boatshow68)
    boat68 = Button(window, textvariable=boatshow68, command=lambda m=[5,7]: gogrt(m))
    buttonlist1.append(boat68)
    boatshow69 = StringVar(window)
    showlist1.append(boatshow69)
    boat69 = Button(window, textvariable=boatshow69, command=lambda m=[5,8]: gogrt(m))
    buttonlist1.append(boat69)
    boatshow610 = StringVar(window)
    showlist1.append(boatshow610)
    boat610 = Button(window, textvariable=boatshow610, command=lambda m=[5,9]: gogrt(m))
    buttonlist1.append(boat610)
    boatshow71 = StringVar(window)
    showlist1.append(boatshow71)
    boat71 = Button(window, textvariable=boatshow71, command=lambda m=[6,0]: gogrt(m))
    buttonlist1.append(boat71)
    boatshow72 = StringVar(window)
    showlist1.append(boatshow72)
    boat72 = Button(window, textvariable=boatshow72, command=lambda m=[6,1]: gogrt(m))
    buttonlist1.append(boat72)
    boatshow73 = StringVar(window)
    showlist1.append(boatshow73)
    boat73 = Button(window, textvariable=boatshow73, command=lambda m=[6,2]: gogrt(m))
    buttonlist1.append(boat73)
    boatshow74 = StringVar(window)
    showlist1.append(boatshow74)
    boat74 = Button(window, textvariable=boatshow74, command=lambda m=[6,3]: gogrt(m))
    buttonlist1.append(boat74)
    boatshow75 = StringVar(window)
    showlist1.append(boatshow75)
    boat75 = Button(window, textvariable=boatshow75, command=lambda m=[6,4]: gogrt(m))
    buttonlist1.append(boat75)
    boatshow76 = StringVar(window)
    showlist1.append(boatshow76)
    boat76 = Button(window, textvariable=boatshow76, command=lambda m=[6,5]: gogrt(m))
    buttonlist1.append(boat76)
    boatshow77 = StringVar(window)
    showlist1.append(boatshow77)
    boat77 = Button(window, textvariable=boatshow77, command=lambda m=[6,6]: gogrt(m))
    buttonlist1.append(boat77)
    boatshow78 = StringVar(window)
    showlist1.append(boatshow78)
    boat78 = Button(window, textvariable=boatshow78, command=lambda m=[6,7]: gogrt(m))
    buttonlist1.append(boat78)
    boatshow79 = StringVar(window)
    showlist1.append(boatshow79)
    boat79 = Button(window, textvariable=boatshow79, command=lambda m=[6,8]: gogrt(m))
    buttonlist1.append(boat79)
    boatshow710 = StringVar(window)
    showlist1.append(boatshow710)
    boat710 = Button(window, textvariable=boatshow710, command=lambda m=[6,9]: gogrt(m))
    buttonlist1.append(boat710)
    boatshow81 = StringVar(window)
    showlist1.append(boatshow81)
    boat81 = Button(window, textvariable=boatshow81, command=lambda m=[7,0]: gogrt(m))
    buttonlist1.append(boat81)
    boatshow82 = StringVar(window)
    showlist1.append(boatshow82)
    boat82 = Button(window, textvariable=boatshow82, command=lambda m=[7,1]: gogrt(m))
    buttonlist1.append(boat82)
    boatshow83 = StringVar(window)
    showlist1.append(boatshow83)
    boat83 = Button(window, textvariable=boatshow83, command=lambda m=[7,2]: gogrt(m))
    buttonlist1.append(boat83)
    boatshow84 = StringVar(window)
    showlist1.append(boatshow84)
    boat84 = Button(window, textvariable=boatshow84, command=lambda m=[7,3]: gogrt(m))
    buttonlist1.append(boat84)
    boatshow85 = StringVar(window)
    showlist1.append(boatshow85)
    boat85 = Button(window, textvariable=boatshow85, command=lambda m=[7,4]: gogrt(m))
    buttonlist1.append(boat85)
    boatshow86 = StringVar(window)
    showlist1.append(boatshow86)
    boat86 = Button(window, textvariable=boatshow86, command=lambda m=[7,5]: gogrt(m))
    buttonlist1.append(boat86)
    boatshow87 = StringVar(window)
    showlist1.append(boatshow87)
    boat87 = Button(window, textvariable=boatshow87, command=lambda m=[7,6]: gogrt(m))
    buttonlist1.append(boat87)
    boatshow88 = StringVar(window)
    showlist1.append(boatshow88)
    boat88 = Button(window, textvariable=boatshow88, command=lambda m=[7,7]: gogrt(m))
    buttonlist1.append(boat88)
    boatshow89 = StringVar(window)
    showlist1.append(boatshow89)
    boat89 = Button(window, textvariable=boatshow89, command=lambda m=[7,8]: gogrt(m))
    buttonlist1.append(boat89)
    boatshow810 = StringVar(window)
    showlist1.append(boatshow810)
    boat810 = Button(window, textvariable=boatshow810, command=lambda m=[7,9]: gogrt(m))
    buttonlist1.append(boat810)
    boatshow91 = StringVar(window)
    showlist1.append(boatshow91)
    boat91 = Button(window, textvariable=boatshow91, command=lambda m=[8,0]: gogrt(m))
    buttonlist1.append(boat91)
    boatshow92 = StringVar(window)
    showlist1.append(boatshow92)
    boat92 = Button(window, textvariable=boatshow92, command=lambda m=[8,1]: gogrt(m))
    buttonlist1.append(boat92)
    boatshow93 = StringVar(window)
    showlist1.append(boatshow93)
    boat93 = Button(window, textvariable=boatshow93, command=lambda m=[8,2]: gogrt(m))
    buttonlist1.append(boat93)
    boatshow94 = StringVar(window)
    showlist1.append(boatshow94)
    boat94 = Button(window, textvariable=boatshow94, command=lambda m=[8,3]: gogrt(m))
    buttonlist1.append(boat94)
    boatshow95 = StringVar(window)
    showlist1.append(boatshow95)
    boat95 = Button(window, textvariable=boatshow95, command=lambda m=[8,4]: gogrt(m))
    buttonlist1.append(boat95)
    boatshow96 = StringVar(window)
    showlist1.append(boatshow96)
    boat96 = Button(window, textvariable=boatshow96, command=lambda m=[8,5]: gogrt(m))
    buttonlist1.append(boat96)
    boatshow97 = StringVar(window)
    showlist1.append(boatshow97)
    boat97 = Button(window, textvariable=boatshow97, command=lambda m=[8,6]: gogrt(m))
    buttonlist1.append(boat97)
    boatshow98 = StringVar(window)
    showlist1.append(boatshow98)
    boat98 = Button(window, textvariable=boatshow98, command=lambda m=[8,7]: gogrt(m))
    buttonlist1.append(boat98)
    boatshow99 = StringVar(window)
    showlist1.append(boatshow99)
    boat99 = Button(window, textvariable=boatshow99, command=lambda m=[8,8]: gogrt(m))
    buttonlist1.append(boat99)
    boatshow910 = StringVar(window)
    showlist1.append(boatshow910)
    boat910 = Button(window, textvariable=boatshow910, command=lambda m=[8,9]: gogrt(m))
    buttonlist1.append(boat910)
    boatshow101 = StringVar(window)
    showlist1.append(boatshow101)
    boat101 = Button(window, textvariable=boatshow101, command=lambda m=[9,0]: gogrt(m))
    buttonlist1.append(boat101)
    boatshow102 = StringVar(window)
    showlist1.append(boatshow102)
    boat102 = Button(window, textvariable=boatshow102, command=lambda m=[9,1]: gogrt(m))
    buttonlist1.append(boat102)
    boatshow103 = StringVar(window)
    showlist1.append(boatshow103)
    boat103 = Button(window, textvariable=boatshow103, command=lambda m=[9,2]: gogrt(m))
    buttonlist1.append(boat103)
    boatshow104 = StringVar(window)
    showlist1.append(boatshow104)
    boat104 = Button(window, textvariable=boatshow104, command=lambda m=[9,3]: gogrt(m))
    buttonlist1.append(boat104)
    boatshow105 = StringVar(window)
    showlist1.append(boatshow105)
    boat105 = Button(window, textvariable=boatshow105, command=lambda m=[9,4]: gogrt(m))
    buttonlist1.append(boat105)
    boatshow106 = StringVar(window)
    showlist1.append(boatshow106)
    boat106 = Button(window, textvariable=boatshow106, command=lambda m=[9,5]: gogrt(m))
    buttonlist1.append(boat106)
    boatshow107 = StringVar(window)
    showlist1.append(boatshow107)
    boat107 = Button(window, textvariable=boatshow107, command=lambda m=[9,6]: gogrt(m))
    buttonlist1.append(boat107)
    boatshow108 = StringVar(window)
    showlist1.append(boatshow108)
    boat108 = Button(window, textvariable=boatshow108, command=lambda m=[9,7]: gogrt(m))
    buttonlist1.append(boat108)
    boatshow109 = StringVar(window)
    showlist1.append(boatshow109)
    boat109 = Button(window, textvariable=boatshow109, command=lambda m=[9,8]: gogrt(m))
    buttonlist1.append(boat109)
    boatshow1010 = StringVar(window)
    showlist1.append(boatshow1010)
    boat1010 = Button(window, textvariable=boatshow1010, command=lambda m=[9,9]: gogrt(m))
    buttonlist1.append(boat1010)

    count = 0 
    for i in range(1,11):
        for I in range(1,11):
            buttonlist1[count].grid(row=(12-i), column=(I+1), padx=3)
            count = count+1
    for i in showlist1:
        i.set('   ')
    
    buttonlist2 = []
    showlist2 = []

    boatshow112 = StringVar(window)
    showlist2.append(boatshow112)
    boat112 = Button(window, textvariable=boatshow112, command=lambda m=[0,0]: gogrt2(m))
    buttonlist2.append(boat112)
    boatshow122 = StringVar(window)
    showlist2.append(boatshow122)
    boat122 = Button(window, textvariable=boatshow122, command=lambda m=[0,1]: gogrt2(m))
    buttonlist2.append(boat122)
    boatshow132 = StringVar(window)
    showlist2.append(boatshow132)
    boat132 = Button(window, textvariable=boatshow132, command=lambda m=[0,2]: gogrt2(m))
    buttonlist2.append(boat132)
    boatshow142 = StringVar(window)
    showlist2.append(boatshow142)
    boat142 = Button(window, textvariable=boatshow142, command=lambda m=[0,3]: gogrt2(m))
    buttonlist2.append(boat142)
    boatshow152 = StringVar(window)
    showlist2.append(boatshow152)
    boat152 = Button(window, textvariable=boatshow152, command=lambda m=[0,4]: gogrt2(m))
    buttonlist2.append(boat152)
    boatshow162 = StringVar(window)
    showlist2.append(boatshow162)
    boat162 = Button(window, textvariable=boatshow162, command=lambda m=[0,5]: gogrt2(m))
    buttonlist2.append(boat162)
    boatshow172 = StringVar(window)
    showlist2.append(boatshow172)
    boat172 = Button(window, textvariable=boatshow172, command=lambda m=[0,6]: gogrt2(m))
    buttonlist2.append(boat172)
    boatshow182 = StringVar(window)
    showlist2.append(boatshow182)
    boat182 = Button(window, textvariable=boatshow182, command=lambda m=[0,7]: gogrt2(m))
    buttonlist2.append(boat182)
    boatshow192 = StringVar(window)
    showlist2.append(boatshow192)
    boat192 = Button(window, textvariable=boatshow192, command=lambda m=[0,8]: gogrt2(m))
    buttonlist2.append(boat192)
    boatshow1102 = StringVar(window)
    showlist2.append(boatshow1102)
    boat1102 = Button(window, textvariable=boatshow1102, command=lambda m=[0,9]: gogrt2(m))
    buttonlist2.append(boat1102)
    boatshow212 = StringVar(window)
    showlist2.append(boatshow212)
    boat212 = Button(window, textvariable=boatshow212, command=lambda m=[1,0]: gogrt2(m))
    buttonlist2.append(boat212)
    boatshow222 = StringVar(window)
    showlist2.append(boatshow222)
    boat222 = Button(window, textvariable=boatshow222, command=lambda m=[1,1]: gogrt2(m))
    buttonlist2.append(boat222)
    boatshow232 = StringVar(window)
    showlist2.append(boatshow232)
    boat232 = Button(window, textvariable=boatshow232, command=lambda m=[1,2]: gogrt2(m))
    buttonlist2.append(boat232)
    boatshow242 = StringVar(window)
    showlist2.append(boatshow242)
    boat242 = Button(window, textvariable=boatshow242, command=lambda m=[1,3]: gogrt2(m))
    buttonlist2.append(boat242)
    boatshow252 = StringVar(window)
    showlist2.append(boatshow252)
    boat252 = Button(window, textvariable=boatshow252, command=lambda m=[1,4]: gogrt2(m))
    buttonlist2.append(boat252)
    boatshow262 = StringVar(window)
    showlist2.append(boatshow262)
    boat262 = Button(window, textvariable=boatshow262, command=lambda m=[1,5]: gogrt2(m))
    buttonlist2.append(boat262)
    boatshow272 = StringVar(window)
    showlist2.append(boatshow272)
    boat272 = Button(window, textvariable=boatshow272, command=lambda m=[1,6]: gogrt2(m))
    buttonlist2.append(boat272)
    boatshow282 = StringVar(window)
    showlist2.append(boatshow282)
    boat282 = Button(window, textvariable=boatshow282, command=lambda m=[1,7]: gogrt2(m))
    buttonlist2.append(boat282)
    boatshow292 = StringVar(window)
    showlist2.append(boatshow292)
    boat292 = Button(window, textvariable=boatshow292, command=lambda m=[1,8]: gogrt2(m))
    buttonlist2.append(boat292)
    boatshow2102 = StringVar(window)
    showlist2.append(boatshow2102)
    boat2102 = Button(window, textvariable=boatshow2102, command=lambda m=[1,9]: gogrt2(m))
    buttonlist2.append(boat2102)
    boatshow312 = StringVar(window)
    showlist2.append(boatshow312)
    boat312 = Button(window, textvariable=boatshow312, command=lambda m=[2,0]: gogrt2(m))
    buttonlist2.append(boat312)
    boatshow322 = StringVar(window)
    showlist2.append(boatshow322)
    boat322 = Button(window, textvariable=boatshow322, command=lambda m=[2,1]: gogrt2(m))
    buttonlist2.append(boat322)
    boatshow332 = StringVar(window)
    showlist2.append(boatshow332)
    boat332 = Button(window, textvariable=boatshow332, command=lambda m=[2,2]: gogrt2(m))
    buttonlist2.append(boat332)
    boatshow342 = StringVar(window)
    showlist2.append(boatshow342)
    boat342 = Button(window, textvariable=boatshow342, command=lambda m=[2,3]: gogrt2(m))
    buttonlist2.append(boat342)
    boatshow352 = StringVar(window)
    showlist2.append(boatshow352)
    boat352 = Button(window, textvariable=boatshow352, command=lambda m=[2,4]: gogrt2(m))
    buttonlist2.append(boat352)
    boatshow362 = StringVar(window)
    showlist2.append(boatshow362)
    boat362 = Button(window, textvariable=boatshow362, command=lambda m=[2,5]: gogrt2(m))
    buttonlist2.append(boat362)
    boatshow372 = StringVar(window)
    showlist2.append(boatshow372)
    boat372 = Button(window, textvariable=boatshow372, command=lambda m=[2,6]: gogrt2(m))
    buttonlist2.append(boat372)
    boatshow382 = StringVar(window)
    showlist2.append(boatshow382)
    boat382 = Button(window, textvariable=boatshow382, command=lambda m=[2,7]: gogrt2(m))
    buttonlist2.append(boat382)
    boatshow392 = StringVar(window)
    showlist2.append(boatshow392)
    boat392 = Button(window, textvariable=boatshow392, command=lambda m=[2,8]: gogrt2(m))
    buttonlist2.append(boat392)
    boatshow3102 = StringVar(window)
    showlist2.append(boatshow3102)
    boat3102 = Button(window, textvariable=boatshow3102, command=lambda m=[2,9]: gogrt2(m))
    buttonlist2.append(boat3102)
    boatshow412 = StringVar(window)
    showlist2.append(boatshow412)
    boat412 = Button(window, textvariable=boatshow412, command=lambda m=[3,0]: gogrt2(m))
    buttonlist2.append(boat412)
    boatshow422 = StringVar(window)
    showlist2.append(boatshow422)
    boat422 = Button(window, textvariable=boatshow422, command=lambda m=[3,1]: gogrt2(m))
    buttonlist2.append(boat422)
    boatshow432 = StringVar(window)
    showlist2.append(boatshow432)
    boat432 = Button(window, textvariable=boatshow432, command=lambda m=[3,2]: gogrt2(m))
    buttonlist2.append(boat432)
    boatshow442 = StringVar(window)
    showlist2.append(boatshow442)
    boat442 = Button(window, textvariable=boatshow442, command=lambda m=[3,3]: gogrt2(m))
    buttonlist2.append(boat442)
    boatshow452 = StringVar(window)
    showlist2.append(boatshow452)
    boat452 = Button(window, textvariable=boatshow452, command=lambda m=[3,4]: gogrt2(m))
    buttonlist2.append(boat452)
    boatshow462 = StringVar(window)
    showlist2.append(boatshow462)
    boat462 = Button(window, textvariable=boatshow462, command=lambda m=[3,5]: gogrt2(m))
    buttonlist2.append(boat462)
    boatshow472 = StringVar(window)
    showlist2.append(boatshow472)
    boat472 = Button(window, textvariable=boatshow472, command=lambda m=[3,6]: gogrt2(m))
    buttonlist2.append(boat472)
    boatshow482 = StringVar(window)
    showlist2.append(boatshow482)
    boat482 = Button(window, textvariable=boatshow482, command=lambda m=[3,7]: gogrt2(m))
    buttonlist2.append(boat482)
    boatshow492 = StringVar(window)
    showlist2.append(boatshow492)
    boat492 = Button(window, textvariable=boatshow492, command=lambda m=[3,8]: gogrt2(m))
    buttonlist2.append(boat492)
    boatshow4102 = StringVar(window)
    showlist2.append(boatshow4102)
    boat4102 = Button(window, textvariable=boatshow4102, command=lambda m=[3,9]: gogrt2(m))
    buttonlist2.append(boat4102)
    boatshow512 = StringVar(window)
    showlist2.append(boatshow512)
    boat512 = Button(window, textvariable=boatshow512, command=lambda m=[4,0]: gogrt2(m))
    buttonlist2.append(boat512)
    boatshow522 = StringVar(window)
    showlist2.append(boatshow522)
    boat522 = Button(window, textvariable=boatshow522, command=lambda m=[4,1]: gogrt2(m))
    buttonlist2.append(boat522)
    boatshow532 = StringVar(window)
    showlist2.append(boatshow532)
    boat532 = Button(window, textvariable=boatshow532, command=lambda m=[4,2]: gogrt2(m))
    buttonlist2.append(boat532)
    boatshow542 = StringVar(window)
    showlist2.append(boatshow542)
    boat542 = Button(window, textvariable=boatshow542, command=lambda m=[4,3]: gogrt2(m))
    buttonlist2.append(boat542)
    boatshow552 = StringVar(window)
    showlist2.append(boatshow552)
    boat552 = Button(window, textvariable=boatshow552, command=lambda m=[4,4]: gogrt2(m))
    buttonlist2.append(boat552)
    boatshow562 = StringVar(window)
    showlist2.append(boatshow562)
    boat562 = Button(window, textvariable=boatshow562, command=lambda m=[4,5]: gogrt2(m))
    buttonlist2.append(boat562)
    boatshow572 = StringVar(window)
    showlist2.append(boatshow572)
    boat572 = Button(window, textvariable=boatshow572, command=lambda m=[4,6]: gogrt2(m))
    buttonlist2.append(boat572)
    boatshow582 = StringVar(window)
    showlist2.append(boatshow582)
    boat582 = Button(window, textvariable=boatshow582, command=lambda m=[4,7]: gogrt2(m))
    buttonlist2.append(boat582)
    boatshow592 = StringVar(window)
    showlist2.append(boatshow592)
    boat592 = Button(window, textvariable=boatshow592, command=lambda m=[4,8]: gogrt2(m))
    buttonlist2.append(boat592)
    boatshow5102 = StringVar(window)
    showlist2.append(boatshow5102)
    boat5102 = Button(window, textvariable=boatshow5102, command=lambda m=[4,9]: gogrt2(m))
    buttonlist2.append(boat5102)
    boatshow612 = StringVar(window)
    showlist2.append(boatshow612)
    boat612 = Button(window, textvariable=boatshow612, command=lambda m=[5,0]: gogrt2(m))
    buttonlist2.append(boat612)
    boatshow622 = StringVar(window)
    showlist2.append(boatshow622)
    boat622 = Button(window, textvariable=boatshow622, command=lambda m=[5,1]: gogrt2(m))
    buttonlist2.append(boat622)
    boatshow632 = StringVar(window)
    showlist2.append(boatshow632)
    boat632 = Button(window, textvariable=boatshow632, command=lambda m=[5,2]: gogrt2(m))
    buttonlist2.append(boat632)
    boatshow642 = StringVar(window)
    showlist2.append(boatshow642)
    boat642 = Button(window, textvariable=boatshow642, command=lambda m=[5,3]: gogrt2(m))
    buttonlist2.append(boat642)
    boatshow652 = StringVar(window)
    showlist2.append(boatshow652)
    boat652 = Button(window, textvariable=boatshow652, command=lambda m=[5,4]: gogrt2(m))
    buttonlist2.append(boat652)
    boatshow662 = StringVar(window)
    showlist2.append(boatshow662)
    boat662 = Button(window, textvariable=boatshow662, command=lambda m=[5,5]: gogrt2(m))
    buttonlist2.append(boat662)
    boatshow672 = StringVar(window)
    showlist2.append(boatshow672)
    boat672 = Button(window, textvariable=boatshow672, command=lambda m=[5,6]: gogrt2(m))
    buttonlist2.append(boat672)
    boatshow682 = StringVar(window)
    showlist2.append(boatshow682)
    boat682 = Button(window, textvariable=boatshow682, command=lambda m=[5,7]: gogrt2(m))
    buttonlist2.append(boat682)
    boatshow692 = StringVar(window)
    showlist2.append(boatshow692)
    boat692 = Button(window, textvariable=boatshow692, command=lambda m=[5,8]: gogrt2(m))
    buttonlist2.append(boat692)
    boatshow6102 = StringVar(window)
    showlist2.append(boatshow6102)
    boat6102 = Button(window, textvariable=boatshow6102, command=lambda m=[5,9]: gogrt2(m))
    buttonlist2.append(boat6102)
    boatshow712 = StringVar(window)
    showlist2.append(boatshow712)
    boat712 = Button(window, textvariable=boatshow712, command=lambda m=[6,0]: gogrt2(m))
    buttonlist2.append(boat712)
    boatshow722 = StringVar(window)
    showlist2.append(boatshow722)
    boat722 = Button(window, textvariable=boatshow722, command=lambda m=[6,1]: gogrt2(m))
    buttonlist2.append(boat722)
    boatshow732 = StringVar(window)
    showlist2.append(boatshow732)
    boat732 = Button(window, textvariable=boatshow732, command=lambda m=[6,2]: gogrt2(m))
    buttonlist2.append(boat732)
    boatshow742 = StringVar(window)
    showlist2.append(boatshow742)
    boat742 = Button(window, textvariable=boatshow742, command=lambda m=[6,3]: gogrt2(m))
    buttonlist2.append(boat742)
    boatshow752 = StringVar(window)
    showlist2.append(boatshow752)
    boat752 = Button(window, textvariable=boatshow752, command=lambda m=[6,4]: gogrt2(m))
    buttonlist2.append(boat752)
    boatshow762 = StringVar(window)
    showlist2.append(boatshow762)
    boat762 = Button(window, textvariable=boatshow762, command=lambda m=[6,5]: gogrt2(m))
    buttonlist2.append(boat762)
    boatshow772 = StringVar(window)
    showlist2.append(boatshow772)
    boat772 = Button(window, textvariable=boatshow772, command=lambda m=[6,6]: gogrt2(m))
    buttonlist2.append(boat772)
    boatshow782 = StringVar(window)
    showlist2.append(boatshow782)
    boat782 = Button(window, textvariable=boatshow782, command=lambda m=[6,7]: gogrt2(m))
    buttonlist2.append(boat782)
    boatshow792 = StringVar(window)
    showlist2.append(boatshow792)
    boat792 = Button(window, textvariable=boatshow792, command=lambda m=[6,8]: gogrt2(m))
    buttonlist2.append(boat792)
    boatshow7102 = StringVar(window)
    showlist2.append(boatshow7102)
    boat7102 = Button(window, textvariable=boatshow7102, command=lambda m=[6,9]: gogrt2(m))
    buttonlist2.append(boat7102)
    boatshow812 = StringVar(window)
    showlist2.append(boatshow812)
    boat812 = Button(window, textvariable=boatshow812, command=lambda m=[7,0]: gogrt2(m))
    buttonlist2.append(boat812)
    boatshow822 = StringVar(window)
    showlist2.append(boatshow822)
    boat822 = Button(window, textvariable=boatshow822, command=lambda m=[7,1]: gogrt2(m))
    buttonlist2.append(boat822)
    boatshow832 = StringVar(window)
    showlist2.append(boatshow832)
    boat832 = Button(window, textvariable=boatshow832, command=lambda m=[7,2]: gogrt2(m))
    buttonlist2.append(boat832)
    boatshow842 = StringVar(window)
    showlist2.append(boatshow842)
    boat842 = Button(window, textvariable=boatshow842, command=lambda m=[7,3]: gogrt2(m))
    buttonlist2.append(boat842)
    boatshow852 = StringVar(window)
    showlist2.append(boatshow852)
    boat852 = Button(window, textvariable=boatshow852, command=lambda m=[7,4]: gogrt2(m))
    buttonlist2.append(boat852)
    boatshow862 = StringVar(window)
    showlist2.append(boatshow862)
    boat862 = Button(window, textvariable=boatshow862, command=lambda m=[7,5]: gogrt2(m))
    buttonlist2.append(boat862)
    boatshow872 = StringVar(window)
    showlist2.append(boatshow872)
    boat872 = Button(window, textvariable=boatshow872, command=lambda m=[7,6]: gogrt2(m))
    buttonlist2.append(boat872)
    boatshow882 = StringVar(window)
    showlist2.append(boatshow882)
    boat882 = Button(window, textvariable=boatshow882, command=lambda m=[7,7]: gogrt2(m))
    buttonlist2.append(boat882)
    boatshow892 = StringVar(window)
    showlist2.append(boatshow892)
    boat892 = Button(window, textvariable=boatshow892, command=lambda m=[7,8]: gogrt2(m))
    buttonlist2.append(boat892)
    boatshow8102 = StringVar(window)
    showlist2.append(boatshow8102)
    boat8102 = Button(window, textvariable=boatshow8102, command=lambda m=[7,9]: gogrt2(m))
    buttonlist2.append(boat8102)
    boatshow912 = StringVar(window)
    showlist2.append(boatshow912)
    boat912 = Button(window, textvariable=boatshow912, command=lambda m=[8,0]: gogrt2(m))
    buttonlist2.append(boat912)
    boatshow922 = StringVar(window)
    showlist2.append(boatshow922)
    boat922 = Button(window, textvariable=boatshow922, command=lambda m=[8,1]: gogrt2(m))
    buttonlist2.append(boat922)
    boatshow932 = StringVar(window)
    showlist2.append(boatshow932)
    boat932 = Button(window, textvariable=boatshow932, command=lambda m=[8,2]: gogrt2(m))
    buttonlist2.append(boat932)
    boatshow942 = StringVar(window)
    showlist2.append(boatshow942)
    boat942 = Button(window, textvariable=boatshow942, command=lambda m=[8,3]: gogrt2(m))
    buttonlist2.append(boat942)
    boatshow952 = StringVar(window)
    showlist2.append(boatshow952)
    boat952 = Button(window, textvariable=boatshow952, command=lambda m=[8,4]: gogrt2(m))
    buttonlist2.append(boat952)
    boatshow962 = StringVar(window)
    showlist2.append(boatshow962)
    boat962 = Button(window, textvariable=boatshow962, command=lambda m=[8,5]: gogrt2(m))
    buttonlist2.append(boat962)
    boatshow972 = StringVar(window)
    showlist2.append(boatshow972)
    boat972 = Button(window, textvariable=boatshow972, command=lambda m=[8,6]: gogrt2(m))
    buttonlist2.append(boat972)
    boatshow982 = StringVar(window)
    showlist2.append(boatshow982)
    boat982 = Button(window, textvariable=boatshow982, command=lambda m=[8,7]: gogrt2(m))
    buttonlist2.append(boat982)
    boatshow992 = StringVar(window)
    showlist2.append(boatshow992)
    boat992 = Button(window, textvariable=boatshow992, command=lambda m=[8,8]: gogrt2(m))
    buttonlist2.append(boat992)
    boatshow9102 = StringVar(window)
    showlist2.append(boatshow9102)
    boat9102 = Button(window, textvariable=boatshow9102, command=lambda m=[8,9]: gogrt2(m))
    buttonlist2.append(boat9102)
    boatshow1012 = StringVar(window)
    showlist2.append(boatshow1012)
    boat1012 = Button(window, textvariable=boatshow1012, command=lambda m=[9,0]: gogrt2(m))
    buttonlist2.append(boat1012)
    boatshow1022 = StringVar(window)
    showlist2.append(boatshow1022)
    boat1022 = Button(window, textvariable=boatshow1022, command=lambda m=[9,1]: gogrt2(m))
    buttonlist2.append(boat1022)
    boatshow1032 = StringVar(window)
    showlist2.append(boatshow1032)
    boat1032 = Button(window, textvariable=boatshow1032, command=lambda m=[9,2]: gogrt2(m))
    buttonlist2.append(boat1032)
    boatshow1042 = StringVar(window)
    showlist2.append(boatshow1042)
    boat1042 = Button(window, textvariable=boatshow1042, command=lambda m=[9,3]: gogrt2(m))
    buttonlist2.append(boat1042)
    boatshow1052 = StringVar(window)
    showlist2.append(boatshow1052)
    boat1052 = Button(window, textvariable=boatshow1052, command=lambda m=[9,4]: gogrt2(m))
    buttonlist2.append(boat1052)
    boatshow1062 = StringVar(window)
    showlist2.append(boatshow1062)
    boat1062 = Button(window, textvariable=boatshow1062, command=lambda m=[9,5]: gogrt2(m))
    buttonlist2.append(boat1062)
    boatshow1072 = StringVar(window)
    showlist2.append(boatshow1072)
    boat1072 = Button(window, textvariable=boatshow1072, command=lambda m=[9,6]: gogrt2(m))
    buttonlist2.append(boat1072)
    boatshow1082 = StringVar(window)
    showlist2.append(boatshow1082)
    boat1082 = Button(window, textvariable=boatshow1082, command=lambda m=[9,7]: gogrt2(m))
    buttonlist2.append(boat1082)
    boatshow1092 = StringVar(window)
    showlist2.append(boatshow1092)
    boat1092 = Button(window, textvariable=boatshow1092, command=lambda m=[9,8]: gogrt2(m))
    buttonlist2.append(boat1092)
    boatshow10102 = StringVar(window)
    showlist2.append(boatshow10102)
    boat10102 = Button(window, textvariable=boatshow10102, command=lambda m=[9,9]: gogrt2(m))
    buttonlist2.append(boat10102)

    count = 0 
    for i in range(1,11):
        for I in range(1,11):
            buttonlist2[count].grid(row=(12-i), column=(I+12), padx=3)
            count = count+1
    for i in showlist2:
        i.set('   ')

    def updateBoard():
        for i in boatB1:
            for I in i:
                count = 0 
                for c in range(10):
                    for C in range(10):
                        if I == [c,C]:
                            showlist1[count].set('B ')
                        count = count + 1
        for I in hitB2:
            count = 0 
            for c in range(10):
                for C in range(10):
                    if I == [c,C]:
                        showlist2[count].set('H')
                    count = count + 1
        for I in missB2:
            count = 0 
            for c in range(10):
                for C in range(10):
                    if I == [c,C]:
                        showlist2[count].set('M')
                    count = count + 1
        for I in hitB1:
            count = 0 
            for c in range(10):
                for C in range(10):
                    if I == [c,C]:
                        showlist1[count].set('H')
                    count = count + 1
        for I in missB1:
            count = 0 
            for c in range(10):
                for C in range(10):
                    if I == [c,C]:
                        showlist1[count].set('M')
                    count = count + 1

    def boatHere(cheek):
        for i in cheek:
            count = 0 
            for c in range(10):
                for C in range(10):
                    if i == [c,C]:
                        if showlist1[count].get() == 'B ':
                            return False
                    count = count + 1
        else:
            return True

    window.mainloop()

if __name__ == "__main__":
    g()