#!Python 3

#input name
# enter use table below
#| A | B | C | D | E | F |
#| G | H | I | J | K | L |
#| M | N | O | P | Q | R |
#| S | T | U | V | W | X |
#| Y | Z |   | - | . | enter |
#output number of cursor movements 
#GPS
#15

def main():
    inputTable = [['A','B','C','D','E','F'],['G','H','I','J','K','L'],['M','N','O','P','Q','R'],['S','T','U','V','W','X'],['Y','Z',' ','-','.','\n']]
    name = (input('Enter the name of your waypoint: ') + '\n').upper()
    #print(name)
    cusor = [0,0]
    movment = 0
    for letter in name:
        #print(cusor, movment)
        for row in range(5):
            if letter in inputTable[row]:
                key = [row,inputTable[row].index(letter)]
                #print(key)
                movment = movment + abs(cusor[0] - key[0]) + abs(cusor[1] - key[1])
                cusor = key
    print(f'\n{movment} key movments to type {name}')


if __name__ == '__main__':
    main()