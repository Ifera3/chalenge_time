#!Python 3

#imports
import random

#global varubules and classes
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

    def getSeen(self):
        if not self.isSeen:
            self.isSeen = True
            if self.agMines == 0 and not self.ismine:
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
                if self.isFlaged:
                    return "(\033[0;31;40m!\033[0;37;40m)"
                elif self.ismine and not self.isFlaged:
                    return "(\033[0;31;40mM\033[0;37;40m)"
                else:
                    if self.agMines != 0:
                        return f"(\033[0;36;40m{self.agMines}\033[0;37;40m)"
                    else:
                        return "( )"
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
    print("  ", end="")
    for i in range(len(table[0])):
        print(f" {i+1} ", end="")
    print()
    for i in range(len(table)):
        print(f"{i+1} ", end='')
        for s in table[i]:
            s.getNum()
            print(s, end='')
        print('')

def main():
    for y in range(8):
        for x in range(8):
            table[y].append(square(x, y))
    #input()
    mines = []
    while len(mines) < 10:
        x = random.randrange(0,8)
        y = random.randrange(0,8)
        if not table[y][x].ismine:
            table[y][x].ismine = True
            mines.append([x,y])
    showMap()
    table[0][0].hasPlayer = True
    table[0][0].getSeen()
    showMap()


if __name__ == "__main__":
    print("\033[0;37;40m")
    main()