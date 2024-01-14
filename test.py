import random

while True:
    try:
        level = int(input("Level: "))
        if 0 < level < 4:
            break
        else:
            print()
    except ValueError:
        print()