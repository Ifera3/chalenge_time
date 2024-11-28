#!Python 3

# get phone number with letters and turn in numbers
#1
#2 - A, B, C
#3 - D, E, F
#4 - G, H, I
#5 - J, K, L
#6 - M, N, O
#7 - P, Q, R, S
#8 - T, U, V
#9 - W, X, Y, Z

#88-SNOW-5555
#887-669-5555

def phoneTrans(phone):
    table = [['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
    phoneNumber = ''
    digits = 0
    #print(phone)
    for i in phone:
        #print(i)
        if i == '-':
            continue
        elif i.isdigit():
            phoneNumber = phoneNumber + i
            digits = digits + 1
        elif i.isalpha():
            for nummber in range(8):
                #print(nummber, table[nummber])
                if i in table[nummber]:
                    phoneNumber = phoneNumber + str(nummber+2)
                    digits = digits + 1
                    break
        if digits == 10:
            break
        elif digits == 3 or digits == 6:
            phoneNumber = phoneNumber + '-'
    #print(phoneNumber)
    return phoneNumber

def main():
    phoneNumbers = []
    amount = input('How many phone numbers are you translating: ')
    while type(amount) == str:
        try:
            amount = int(amount)
            break
        except:
            amount = input('How many phone numbers are you translating as a number: ')
    for i in range(amount):
        phoneNumbers.append(phoneTrans((input(f'\nEnter phone number {i + 1}: ')).upper()))
    for i in range(amount):
        print(f'\nPhone number {i + 1} is {phoneNumbers[i]} as a numarical phone number.')

if __name__ == '__main__':
    main()