def main():
    text = input("")
    return playback(text)


def playback(word):
    return print(word.replace(" ", "...").strip())


main()
