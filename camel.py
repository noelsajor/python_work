camel_case = input("camelCase: ")

print("snake_case: ", end="")

for char in camel_case:
    if char.isupper():
        print(f"_{char.lower()}", end="")

    else:
        print(char, end="")

if camel_case.startswith("_"):
    snake_case = camel_case.replace("_", "")

print()

#now I'm adding a comment to this file just as a test about the functioning of git
