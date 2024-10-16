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