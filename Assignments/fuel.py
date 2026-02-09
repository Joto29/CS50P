def main():
    print(get_fuel("Fraction: "))

def get_fuel(prompt):
    while True:
        try:
            word = input(prompt)
            x, z = word.split("/")
            x = int(x)
            z = int(z)

            if x > z:
                raise ValueError

            percent = round((x / z) * 100)

            if percent <= 1:
                return "E"
            elif percent >= 99:
                return "F"
            else:
                return f"{percent}%"

        except (ZeroDivisionError, ValueError):
            pass

main()
