#!Python 3

#imports
import random

#global varubules and classes
printLater = []
squaresleft = 54
table = [[],[],[],[],[],[],[],[]]
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

    def getSeen(self):
        global squaresleft
        if not self.isSeen:
            self.isSeen = True
            squaresleft -= 1
            if self.ismine and not self.isFlaged:
                loss()
            elif self.agMines == 0 and not self.ismine:
                for i in self.check:
                    table[self.row+i[0]][self.coloum+i[1]].getSeen()

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
                if random.randrange(-1,1) == 0:
                    return "(/)"
                else:
                    return "(\)"
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
                if random.randrange(-1,1) == 0:
                    return "[/]"
                else:
                    return "[\]"

def showMap():
    print("\n   A  B  C  D  E  F  G  H ")
    for i in range(len(table)):
        print(f"{i+1} ", end='')
        for s in table[i]:
            print(s, end='')
        print('')

def loss():
    print("\033[0;31;40m")
    showMap()
    print('you lose')
    exit()

def checkLocation():
    cord = ""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    while type(cord) == str:
        cord = input("enter the cords of the square you would like to check or flage(eg. A, 2): ")
        if ',' in cord:
            cord = cord.split(',')
            for i in cord:
                i = i.strip()
                i = i.lower() 
            if cord[0] in letters:
                cord[0] = letters.index(cord[0])
                if cord[1].isdigit():
                    cord[1] = int(cord[1])
                    if 0 < cord[1] < 9:
                        cord[1] -= 1
                        if not table[cord[1]][cord[0]].isSeen:
                            table[cord[1]][cord[0]].hasPlayer = True
                            showMap()
                            flag = input("would you like to place a flage or break the square(f or b): ")
                            if flag.lower() == 'f':
                                table[cord[1]][cord[0]].isFlaged = True
                                table[cord[1]][cord[0]].getSeen()
                            elif flag.lower() == 'b':
                                table[cord[1]][cord[0]].getSeen()
                            else:
                                cord = ''
                            table[cord[1]][cord[0]].hasPlayer = False
                        else:
                            cord = ''
                    else:
                        cord = ''
                else:
                    cord = ''
            else:
                cord = ''


def main():
    for y in range(8):
        for x in range(8):
            table[y].append(square(x, y))
    #input()
    global mines
    mines = 0
    while mines < 10:
        x = random.randrange(0,8)
        y = random.randrange(0,8)
        if not table[y][x].ismine:
            table[y][x].ismine = True
            mines += 1
    for i in table:
        for s in i:
            s.getNum()
    showMap()
    #table[0][0].hasPlayer = True
    #table[7][7].getSeen()
    while squaresleft > 0:
        checkLocation()
        print(squaresleft)
        showMap()


if __name__ == "__main__":
    print("\033[0;37;40m")
    main()
    #print(printLater)