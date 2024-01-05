while True:
    fraction = input("Fraction: ")
    try:
        numerator, denominator = fraction.split("/")
        percentage = int(numerator) / int(denominator)
        if percentage <= 1:
            break
    except(ValueError, ZeroDivisionError):
        pass
if percentage <= 0.1:
    print("E")
elif percentage >= 0.99:
    print("F")
else:
    print(f"{round(percentage * 100)}%")