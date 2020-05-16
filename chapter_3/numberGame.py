from random import randint

def numberGame():
    #choose a random number
    #between 1 and 100
    number = randint(1, 100)

    print("I'm thinking of a number between 1 and 100.")
    guess = int(input("What's your guess? "))

    while guess:
        if number == guess:
            print("That's correct! The number was ", number)
            break
        elif number > guess:
            print("Nope. Guess higher.")
        else:
            print("Nope. Guess lower.")
        guess = int(input("What's your guess? "))

def greet():
    name = input("What's your name: ")
    print("Hello,", name)

def adv_greet():
    name = input("What's your name: ")
    if name == "Peter":
        print("That’s my name, too!")
    else:
        print("Hello,", name)

numberGame()