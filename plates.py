def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    all_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    not_allowed = [".", " ", ",", ":", ";", "?", "!", "[", "]", "{", "}", "<", ">", "-", "_", "=", "(", ")", "'", '"', "#", "@", "&", "*", "$", "/"]
    
    #condition 1
    condition1 = s[0] and s[1] in all_letters

    #condition 2
    condition2 = len(s) >= 2 and len(s) <= 6

    #condition3
    condition3 = True
    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == "0":
                condition3 = False
            else:
                break
        i += 1

    #condition4
    condition4 = True
    for char in not_allowed:
        if char in s:
            condition4 = False
        else:
            break 

    #condition5
    condition5 = True
    if s[-1] in all_letters:
        condition5 = False
    else:
        pass



    is_valid = condition1 and condition2 and condition3 and condition4 and condition5

    return is_valid
    


main()