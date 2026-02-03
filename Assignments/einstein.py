def main():
    mass = int(input("m: "))
    print(convert_e(mass))

def convert_e(mass, c = 300000000):
    e = mass * (c**2)
    return e

main()
