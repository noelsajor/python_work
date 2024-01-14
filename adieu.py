import inflect

names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print()
        break

p = inflect.engine()    
mylist = p.join(names)
print("Adieu, adieu, to " + mylist)