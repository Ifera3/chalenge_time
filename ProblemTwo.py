#!Python 3

# First input line is distance from the tee to the hole: 1 <= distance <= 5 280
# Second input line is number of clubs: 1 <= #ofClubs <= 32
# An input for each clubs distance: 1 <= distance <= 100.
# returns how many strokes till Roberta wins in the least strokes or if it is not posible.

def getInput():
    holeLingth = input("Enter the lingth to the hole in meters(1m to 5 280m): ")
    while type(holeLingth) != int:
        try:
            holeLingth = holeLingth.replace('m','')
            holeLingth = int(holeLingth)
            if holeLingth < 1 or holeLingth > 5280:
                print("Not bettwen 1 and 5 280")
                raise("Not bettwen 1 and 5280")
        except: 
            holeLingth = input("Please enter the lingth to the hole in meters as only a number from 1 to 5 280: ")
    numberOfClubs = input("Enter the number of clubs Roberta has(1 to 32): ")
    while type(numberOfClubs) != int:
        try:
            numberOfClubs = numberOfClubs.replace('clubs','')
            numberOfClubs = int(numberOfClubs)
            if numberOfClubs < 1 or numberOfClubs > 32:
                print("Not bettwen 1 and 32")
                raise("Not bettwen 1 and 32")
        except:
            numberOfClubs = input("Please enter the number of Roberta\'s clubs as only a number from 1 to 32: ")
    clubLingths = []
    for i in range(numberOfClubs):
        tempClubLingth = input(f"Enter the distance of club #{i+1} (1m to 100m): ")
        while type(tempClubLingth) != int:
            try:
                tempClubLingth = tempClubLingth.replace('m','')
                tempClubLingth = int(tempClubLingth)
                if tempClubLingth < 1 or tempClubLingth > 100:
                    print("Not bettwen 1 and 100")
                    raise("Not bettwen 1 and 100")
                for c in clubLingths:
                    if tempClubLingth == c:
                        print(f"A club with the lingth of {tempClubLingth}m already exists.")
                        raise("alrady exist")
            except:
                tempClubLingth = input(f"Please enter the distance of club #{i+1} as only a number from 1 to 100: ")
        else:
            clubLingths.append(tempClubLingth)
    clubLingths.sort(reverse=True)
    return holeLingth,numberOfClubs,clubLingths

def algrithmTime(holeLingth,clubLingths):
    distLeft = holeLingth
    numberOfStrokes = [0]
    tempNumberOfStrokes = 0
    for i in clubLingths:
        while i <= distLeft:
            distLeft = distLeft - i
            tempNumberOfStrokes = tempNumberOfStrokes + 1
    if distLeft != 0:
        return 0
    elif distLeft == 0:
        numberOfStrokes.append(tempNumberOfStrokes)
    else:
        return numberOfStrokes

def main():
    holeLingth,numberOfClubs,clubLingths = getInput()
    numberOfStrokes = algrithmTime(holeLingth,clubLingths)
    if numberOfStrokes == 0:
        print("Roberta accepts defeat")
    else:
        print(f"Roberta wins in {numberOfStrokes} strokes.")

if __name__ == '__main__':
    main()