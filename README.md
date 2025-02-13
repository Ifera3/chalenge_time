# Chalenge Time

# Problems From [dmoj.ca](https://dmoj.ca/problems/)

* most text in this doc are copy and pasted from origanole chalange webpage
* liks are included to origanole webpage

## First problem https://dmoj.ca/problem/ccc13s1

You might be surprised to know that 2013 is the first year since 1987 with distinct digits. The years 2014, 2015, 2016, 2017, 2018, 2019 each have distinct digits. 2012 does not have distinct digits, since the digit 2 is repeated.

### Input specification

input of integer Y (0<=Y<=10 000)

### Output specification

integer D with next number with distincte units

### Example

1987 into 2013
999 into 1023

## Second Problem https://dmoj.ca/problem/ccc00s4
## Golf

### Description

Roberta the Robot plays a perfect game of golf. When she hits the golf ball it always goes directly towards the hole on the green, and she always hits exactly the distance that is specified for the club. Each such action is known as a stroke, and the object of golf is to hit the ball from the tee to the hole in the fewest number of strokes. Roberta needs a program to select the best combination of clubs to reach the hole in the fewest strokes. She also needs to decide if the task is impossible, in which case she graciously acknowledges the loss. Roberta can carry up to 32 clubs, and the total distance from the tee to the hole does not exceed 5 280 metres.

### Input

First input line is distance from the tee to the hole: 1 <= distance <= 5 280.
Second input line is number of clubs: 1 <= #ofClubs <= 32.
An input for each clubs distance: 1 <= distance <= 100.

### Output

Returns how many strokes till Roberta wins in the least strokes or if it is not posible.

### Example

input
```
100
3
33
66
1
```

output
```
Roberta wins in 3 strokes.
```

## Third problem https://dmoj.ca/problem/ccc08j3
## GPS menu key

### description

To enter a name you must move the cursor in the table starting at ```A```. Goal is to find out how many key inputs are required to enter a given name. 

```
| A | B | C | D | E | F |
| G | H | I | J | K | L |
| M | N | O | P | Q | R |
| S | T | U | V | W | X |
| Y | Z |   | - | . | enter |
```

### example one

input
```
GPS
```

output
```
15
```

### example two

input
```
ECHO ROCK
```

output
```
29
```

## Problem Four https://dmoj.ca/problem/ccc05s1
## phone nymber translator

### Description

Get a phone number such as ```416-BUY-More``` and turn it into the number ```416-289-6673```. For phone numbers with more then 10 digits are reduces to only 10 digits

```
1
2 - A, B, C
3 - D, E, F
4 - H, I, J
5 - K, L, M
6 - N, O, P
7 - Q, R, S
8 - T, U, V
9 - W, X, Y, Z

```

### Input

how many phone numbers

What each phone number is

```
5
88-SNOW-5555
519-888-4567
BUY-MORE-POP
416-PIZZA-BOX
5059381123
```

### Output

Numbers for each of the phone numbers

```
887-669-5555
519-888-4567
289-667-3767
416-749-9226
505-938-1123
```

## Problem Five 
## Mary's Game

### Description

Card game played with one deck without 2s and jokers for 3 or 4 players and two decks for 5 to 7 players

You get delt one card face up that decides how many cards you get

Dealers face up card is the wild card for that round

you play sets of three cards 

cards played are point to you cards in your hand are points aganst you

3 - 8 is 5 points, 9 - king is 10 points, Ace and Wild are 100 points

## Problem Six
## Minesweeper

### Description

create table of 8 x 8 with 10 mines

intracted squares explod if mine or show number of mines agasent to them

