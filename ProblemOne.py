#!Python 3
#input of integer Y (0<=Y<=10 000)
#Output specification: integer D with next number with distincte units
#example 1987 into 2013 or 999 into 1023

def main():
    sYear = input('Enter a yaer as an interger from 0 to 10 000: ')
    isNum = ""
    while type(isNum) != int:
        try:
            isNum = int(sYear)
            if isNum > 10000 or isNum < 0:
                raise ValueError("no num over 10 000 or under 0")
        except:
            sYear = input('Enter a year as an interger from 0 to 10 000: ')
            isNum = ""
    for testYear in range((isNum+1),10235):
        testString = str(testYear)
        i = 0
        score = 0
        for testNum in testString:
            I = -1
            for difNum in testString:
                I = I + 1
                if i == I:
                    continue
                elif testNum == difNum:
                    break
            else:
                score = score + 1
            i = i + 1
        if score == len(testString):
            print(f"The next year after {sYear} with distincte units is {testString}")
            break
    else:
        print(f"No year in the 10 234 year limit starting at {sYear} with distincte units")

if __name__ == '__main__':
    main()