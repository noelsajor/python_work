import random


def main():
    level = get_level()
    score = game(level)
    print("Score: ", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                break
        except:
            pass
    return level

def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x,y

def round(x, y):
    tries = 1
    while tries <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                return True
            else:
                tries += 1
                print("EEE")
        except:
            tries += 1
            print("EEE")
    print(f"{x} + {y} = {x + y}")
    return False

def game(level):
    count_round = 1
    score = 0
    while count_round <= 10:
        x, y = generate_integer(level)
        response = round(x,y)
        if response == True:
            score += 1
        count_round += 1
    return score

if __name__ == "__main__":
    main()