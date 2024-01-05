grocery_items_list = {}

try:
    while True:
        item = (input("")).lower()
        grocery_items_list[item] = grocery_items_list.get(item, 0) + 1
except EOFError:
    pass   

for item in sorted(grocery_items_list.keys()):
    count = grocery_items_list[item]
    print(f"{count} {item.upper()}")
