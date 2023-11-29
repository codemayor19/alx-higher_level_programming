#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = -98
if number < 0:
    numb = number * -1
num = number % 10
if number < 0:
    num = num * -1
    numb *= -1
if (num > 5):
    print(f"Last digit of {numb} is {num} and is greater than 5")
elif (num == 0):
    print(f"Last digit of {numb} is {num} and is 0")
else:
    print(f"Last digit of {numb} is {num} and is less than \
6 and not 0")
