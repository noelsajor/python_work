def main():
    text = (input("Input: ")).lower()
    result = shorten(text)
    return f"Output: {result}"


def shorten(word):
    vowels = "aeiouAEIOU"
    result = ''.join(char for char in word if char not in vowels)
    return result


if __name__ == "__main__":
    main()