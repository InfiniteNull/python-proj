import random

def introRoll():
    print("==========[D i c e [ 0 ] R o l l]==========")
    print("1. Roll the Dice")
    print("2. Exit")
    print("==========[D i c e [ 0 ] R o l l]==========")
    diceRoll()

def diceRoll():
    player = input("Choose and type (1, 2): ")
    while True:
        if player == '1':
            dice = random.randint(1, 6)
            print("==========[D i c e", "[", dice, "]", "R o l l]==========")
            print("Your dice number is:", dice)
            print("==========[D i c e", "[", dice, "]", "R o l l]==========")
            tryAgain()
        elif player == '2':
            exit()
        else:
            print("-There is only two option (1, 2)-")
        player = input("Choose and type (1, 2): ")

def tryAgain():
    print("Do yo want to roll the dice again? (Y/N)")
    tryAgain = str(input(""))
    while True:
        if tryAgain == 'Y':
            diceRoll()
        elif tryAgain == 'N':
            exit()
        else:
            print("-There is only two option (Y/N)-")
        tryAgain = str(input(""))

introRoll()
