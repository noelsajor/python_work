def main():
    user_input = input("IPv4 Address: ")
    print(validate(user_input))

def validate(ip):
    address = ip.split(".")
    if len(address) == 4:
        for _ in address:
            if int(_) < 0 int(_) > 255:
                return False
        else:
            return True
    


if __name__ == "__main__":
    main()
