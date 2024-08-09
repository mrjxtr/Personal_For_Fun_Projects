import random


def roll_dice(num):
    return random.randint(1, num)


answer = print(roll_dice(int(input("Dice face: "))))
if answer:
    print(answer)
