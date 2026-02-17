def main():
    exp_inp = input("Expression: ")

    x, y, z = exp_inp.split(" ")
    new_x = int(x)
    new_z = int(z)

    if y == "+":
        total = new_x + new_z
        print(float(total))
    elif y == "-":
        total = new_x - new_z
        print(float(total))
    elif y == "*":
        total = new_x * new_z
        print(float(total))
    else:
        total = new_x / new_z
        print(round(total, 1))


main()
