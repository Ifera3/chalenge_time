#!Python 3

import random

for i in range(100):
    if i == 24:
        print(i)
        raise Exception("hi")