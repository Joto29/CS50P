def main():
    # prompt the user
    user_prompt = input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything? "
    ).lower()

    if not (
        user_prompt == "42" or user_prompt == "forty-two" or user_prompt == "forty two"
    ):
        print("No")
    else:
        print("Yes")


main()
