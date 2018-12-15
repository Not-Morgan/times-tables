#!/usr/bin/python
import sys
import argparse
import random

parser = argparse.ArgumentParser(description="practice your times tables in any base")
parser.add_argument("base", type=int)
parser.add_argument("-m", "--max", type=int)
args = vars(parser.parse_args())

# string of all acceptable numerals in increasing order
numerals = "0123456789abcdefghijklmnopqrstuvwxyz"

# get the base
if args["base"] is not None:
    base = args["base"]
else:
    base = 10
# if max isn't given use the base
if args["max"] is not None:
    max = args["max"] + 1
else:
    max = base + 1

random.seed()

def toStr(num, base):
    """convert a number to a string of any base"""
    return ((num == 0) and numerals[0]) or (toStr(num // base, base).lstrip(numerals[0]) + numerals[num % base])
    
    
def main():
    total = 0
    correct = 0
    
    try:
        while(True):
            # pick 2 numbers and ask for their product
            a = random.randrange(1, max)
            b = random.randrange(1, max)
            answer = input(f"what is {toStr(a, base)} * {toStr(b, base)}?\n")
            
            # check if the answer is made of characters of that base and if it's correct
            if (answer and all(c in numerals[:base] for c in answer) and int(answer, base=base) == a * b):
                print("correct!")
                correct += 1
            else:
                print(f"incorrect it's {toStr(a * b, base)}")
            total += 1

    except KeyboardInterrupt:
        print(f"\nyou got {correct} out of {total} correct!")


if __name__ == "__main__":
    main()

