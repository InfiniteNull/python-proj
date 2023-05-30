import random

minRange = 1
maxRange = 10
randomRange = random.randint(minRange, maxRange)

guess = int(input("Input number between 1-10: "))

while guess != randomRange:
    if guess < randomRange:
        print("Number is too small")
    else:
        print("Number is to big")
    guess = int(input("Try Again: "))

print("Congratulations, You are correct!")
