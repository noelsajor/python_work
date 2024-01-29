def main():
    user_input = input("Please type a greeting: ").lower().strip()
    result = value(user_input)
    print(f"${result}")


def value(greeting):
    greeting_values = {
        "hello": 0,
        "h": 20,
    }

    for key, value in greeting_values.items():
        if greeting.startswith(key):
            return value
    return 100


if __name__ == "__main__":
    main()