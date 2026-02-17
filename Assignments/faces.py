def main():
    # ask for input
    word = input()
    print(convert(word))


def convert(new_word):
    # convert icon
    new_word = new_word.replace(":)", "🙂")
    new_word = new_word.replace(":(", "🙁")
    return new_word


main()
