def main():
    inp = input("Input: ")
    return convert(inp)


def convert(words):
    new_word = ""
    for word in words:
        if word not in "aeiou":
            new_word += word
    return print(f"Output: {new_word}")


main()
