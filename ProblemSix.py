#!Python 3

#imports
import random

#global varubules and classes
#printLater = []
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
table = []
mines = []
falseFlagedSquares = []
flaged = 0
width = 7
hight = 7
totalMines = int((width * hight)/4.9)
squaresleft = (width * hight) - totalMines
class square:
    ismine = False
    isSeen = False
    isFlaged = False
    hasPlayer = False
    check = []
    agMines = 0

    def getNum(self):
        if not self.ismine:
            for i in self.check:
                if table[self.row+i[0]][self.coloum+i[1]].ismine:
                    self.agMines += 1
                    #printLater.append((i, self.agMines))

    def forceDestroy(self):
        agFlags = 0
        if not self.ismine and not self.isFlaged and self.isSeen:
            for i in self.check:
                if table[self.row+i[0]][self.coloum+i[1]].isFlaged:
                    agFlags += 1
            if agFlags == self.agMines:
                for i in self.check:
                    table[self.row+i[0]][self.coloum+i[1]].getSeen()

    def getSeen(self):
        global squaresleft
        if not self.isSeen:
            self.isSeen = True
            if not self.isFlaged:
                squaresleft -= 1
            if self.ismine and not self.isFlaged:
                loss()
            elif self.agMines == 0 and not self.ismine and not self.isFlaged:
                for i in self.check:
                    table[self.row+i[0]][self.coloum+i[1]].getSeen()

    def __init__(self, x, y):
        #print(x, y)
        self.coloum = x
        self.row = y
        if self.row == 0 and self.coloum == 0:
            self.check = [[0,1],[1,0],[1,1]]
        elif self.row == 0 and self.coloum == (width-1):
            self.check = [[0,-1],[1,-1],[1,0]]
        elif self.row == (hight-1) and self.coloum == 0:
            self.check = [[-1,0],[-1,1],[0,1]]
        elif self.row == (hight-1) and self.coloum == (width-1):
            self.check = [[-1,-1],[-1,0],[0,-1]]
        elif self.row == 0 and self.coloum != 0 and self.coloum != (width-1):
            self.check = [[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        elif self.row == (hight-1) and self.coloum != 0 and self.coloum != (width-1):
            self.check = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1]]
        elif self.coloum == 0 and self.row != 0 and self.row != (hight-1):
            self.check = [[-1,0],[-1,1],[0,1],[1,0],[1,1]]
        elif self.coloum == (width-1) and self.row != 0 and self.row != (hight-1):
            self.check = [[-1,-1],[-1,0],[0,-1],[1,-1],[1,0]]
        else:
            self.check = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        #print(self.check)
    
    def __str__(self):
        if self.hasPlayer:
            if self.isSeen:
                if self.ismine and not self.isFlaged:
                    return "(\033[0;31;40mM\033[0;37;40m)"
                else:
                    if self.agMines != 0:
                        return f"(\033[0;36;40m{self.agMines}\033[0;37;40m)"
                    else:
                        return "( )"
            elif self.isFlaged:
                    return "(\033[0;31;40m!\033[0;37;40m)"
            else:
                if random.randrange(0,2) == 0:
                    return "\033[0;32;40m(/)\033[0;37;40m"
                else:
                    return "\033[0;32;40m(\)\033[0;37;40m"
        else:
            if self.isSeen:
                if self.isFlaged:
                    return "[\033[0;31;40m!\033[0;37;40m]"
                elif self.ismine and not self.isFlaged:
                    return "[\033[0;31;40mM\033[0;37;40m]"
                else:
                    if self.agMines != 0:
                        return f"[\033[0;36;40m{self.agMines}\033[0;37;40m]"
                    else:
                        return "[ ]"
            else:
                if random.randrange(0,2) == 0:
                    return "[/]"
                else:
                    return "[\]"


#functions
def showMap():
    #shows the board
    #creates lables by itrating throgh the size table[0]
    #prints squares by printing their __str__ method
    print('   ', end='')
    for i in range(width):
        print(f" {letters[i]} ", end='')
    print()
    for i in range(len(table)):
        print(f"{i+1:<2} ", end='')
        for s in table[i]:
            print(s, end='')
        print('')

def loss():
    #shows all mines and what flages were wrong
    #print("\033[0;31;40m")
    for i in mines:
        table[i[0]][i[1]].isFlaged = False
        table[i[0]][i[1]].getSeen()
    #print(falseFlagedSquares)
    for i in falseFlagedSquares:
        table[i[0]][i[1]] = "\033[0;33;40m[X]\033[0;37;40m"
        #print(table[i[0]][i[1]])
    showMap()
    print('\n\033[0;31;40mYOU LOSE\033[0;37;40m\n')
    exit()

def checkLocation():
    global flaged
    cord = ""
    while type(cord) == str:
        cord = input("enter the cords of the square you would like to check or flage(eg. A, 2): ")
        if ',' in cord:
            cord = cord.split(',')
            for i in range(2):
                cord[i] = cord[i].strip()
                #cord[i] = cord[i].lower()
                #print(cord[i]) 
            if cord[0] in letters:
                cord[0] = letters.index(cord[0])
                #print(cord[0])
                if 0 <= cord[0] < width:
                    if cord[1].isdigit():
                        cord[1] = int(cord[1])
                        if 0 < cord[1] <= hight:
                            cord[1] -= 1
                            activesquare = table[cord[1]][cord[0]]
                            if activesquare.isSeen:
                                if activesquare.isFlaged:
                                    flag = input("Would you like to remove the flag?(y or n): ")
                                    if flag.lower() == 'y':
                                        activesquare.isFlaged = False
                                        activesquare.isSeen = False
                                        flaged -= 1
                                        if [cord[1],cord[0]] in falseFlagedSquares:
                                            falseFlagedSquares.remove([cord[1],cord[0]])
                                elif activesquare.agMines != 0:
                                    activesquare.forceDestroy()
                            else:
                                activesquare.hasPlayer = True
                                showMap()
                                flag = input("Would you like to place a flage or break the square?(f or b): ")
                                if flag.lower() == 'f':
                                    activesquare.isFlaged = True
                                    flaged += 1
                                    #print(activesquare.ismine)
                                    if not activesquare.ismine:
                                        falseFlagedSquares.append([cord[1],cord[0]])
                                    activesquare.getSeen()
                                elif flag.lower() == 'b':
                                    activesquare.getSeen()
                                else:
                                    cord = ''
                                activesquare.hasPlayer = False
                        else:
                            cord = ''
                    else:
                        cord = ''
                else:
                    cord = ''
            else:
                cord = ''


def main():
    for y in range(hight):
        table.append([])
        for x in range(width):
            table[y].append(square(x, y))
    #input()
    global mines
    while len(mines) < totalMines:
        x = random.randrange(0,width)
        y = random.randrange(0,hight)
        if not table[y][x].ismine:
            table[y][x].ismine = True
            mines.append([y,x])
    for i in table:
        for s in i:
            s.getNum()
    #table[0][0].hasPlayer = True
    #table[7][7].getSeen()
    while squaresleft > 0:
        print(f"{flaged} / {totalMines}")
        showMap()
        checkLocation()
    print(f"{flaged} / {totalMines}")
    showMap()


if __name__ == "__main__":
    print("\033[0;37;40m")
    main()
    #print(printLater)