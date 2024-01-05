text = input("Input: ")

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ''.join(char for char in text if char not in vowels)
    return result


result = remove_vowels(text)
print(f"Output: {result} ")
