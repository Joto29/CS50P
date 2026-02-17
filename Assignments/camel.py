def main():
    camel_word = input("caseCamel: ")
    return convert(camel_word)


def convert(s):
    new_string = ""
    for c in s:
        if c.isupper():
            new_string += "_"
            new_string += c.lower()
        else:
            new_string += c
    return print(f"snake_case: {new_string}")


main()
