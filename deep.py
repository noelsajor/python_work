great_answer = (input("What is the answer to the Great Question of Life, the Universe and Everything? ")).lower().strip()

if great_answer == ("42"):
    print("Yes")

elif great_answer == ("forty-two"):
    print("Yes")

elif great_answer == ("forty two"):
    print("Yes")

else:
    print("No")