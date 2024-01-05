def main():
    grocery_items_list = {}

    try:
        while True:
            item = (input("")).lower()
            grocery_items_list[item] = grocery_items_list.get(item, 0) + 1
    except EOFError:
        pass
    print_grocery_list(grocery_items_list)

def print_grocery_list(items_list):
    for item in sorted(items_list.keys()):
        count = items_list[item]
        print(f"{count} {item.upper()}")

if __name__ == "__main__":
    main()