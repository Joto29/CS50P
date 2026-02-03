def main():
    #prompt the user
    greeting = input("Greeting: ")

    #check conditionals
    if greeting.startswith("Hello") or greeting == "hello":
        print("$0")
    elif greeting.startswith("H") or greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

main()