import emoji


# ask the user for input
def main():
    inp = input("Input: ")
    print(convert_inp(inp))


# convert the input
def convert_inp(inp):
    return emoji.emojize(f"Output: {inp}", language="alias", variant="text_type")


main()
