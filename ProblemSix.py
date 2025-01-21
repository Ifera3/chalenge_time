#!Python 3

#imports
import random

#global varubules and classes
table = [[],[],[],[],[],[],[],[]]
class square:
    ismine = False
    isSeen = True
    check = []
    agMines = 0

    def getNum(self):
        if not self.ismine:
            for i in self.check:
                if table[self.row+i[0]][self.coloum+i[1]].ismine:
                    self.agMines += 1

    def __init__(self, x, y):
        #print(x, y)
        self.coloum = x
        self.row = y
        if self.row == 0 and self.coloum == 0:
            self.check = [[0,1],[1,0],[1,1]]
        elif self.row == 0 and self.coloum == 7:
            self.check = [[0,-1],[1,-1],[1,0]]
        elif self.row == 7 and self.coloum == 0:
            self.check = [[-1,0],[-1,1],[0,1]]
        elif self.row == 7 and self.coloum == 7:
            self.check = [[-1,-1],[-1,0],[0,-1]]
        elif self.row == 0 and self.coloum != 0 and self.coloum != 7:
            self.check = [[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        elif self.row == 7 and self.coloum != 0 and self.coloum != 7:
            self.check = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1]]
        elif self.coloum == 0 and self.row != 0 and self.row != 7:
            self.check = [[-1,0],[-1,1],[0,1],[1,0],[1,1]]
        elif self.coloum == 7 and self.row != 0 and self.row != 7:
            self.check = [[-1,-1],[-1,0],[0,-1],[1,-1],[1,0]]
        else:
            self.check = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        #print(self.check)
    
    def __str__(self):
        if self.isSeen:
            if self.ismine:
                return "[\033[0;31;40mM\033[0;37;40m]"
            else:
                return f"[{self.agMines}]"
        else:
            return f"[ ]"

def showMap():
    for i in table:
        for s in i:
            s.getNum()
            print(s, end='')
        print('')

def main():
    for y in range(8):
        for x in range(8):
            table[y].append(square(x, y))
    #input()
    mines = 0
    while mines < 10:
        x = random.randrange(0,8)
        y = random.randrange(0,8)
        if not table[y][x].ismine:
            table[y][x].ismine = True
            mines += 1
    showMap() #


if __name__ == "__main__":
    print("\033[0;37;40m")
    main()