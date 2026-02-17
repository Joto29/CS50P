def main():
    name = input("What's your name: ").strip().title()
    return hello(name)


def hello(to):
    return print(f"Hello, {to}")


main()
