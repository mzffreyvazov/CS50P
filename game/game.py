from random import *
import sys
while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except ValueError:
        pass
number = randint(1, n)

while True:
    try:
        try:
            answer = int(input("Guess: "))
        except:
            sys.exit("\n")
        if answer > 0:
            if answer == number:
                print("Just right!", end="")
                break
            elif answer > number:
                print("Too large!")
            else:
                print("Too small!")
    except:
        pass