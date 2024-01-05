calc = input("Expression: ")
x, y, z = calc.split(" ", 2)

if y == "+":
    print(float(int(x) + int(z)))

elif y == "-":
    print(float(int(x) - int(z)))

elif y == "*":
    print(float(int(x) * int(z)))

elif y == "/":
    print(float(int(x) / int(z)))