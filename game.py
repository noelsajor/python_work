import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
        else:
            print()
    except ValueError:
        print()

random_integer = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess == random_integer and guess > 0:
            print("Just right!")
            break
        elif guess < random_integer and guess > 0:
            print("Too small!")
        elif guess > random_integer and guess > 0:
            print("Too large!")
    except ValueError:
        print()
