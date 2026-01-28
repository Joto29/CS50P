def main():
    x = float(input("What's x:"))
    y = float(input("What's y:"))
    return add_num(x,y), subs_num(x,y) , mult_num(x,y) ,div_num(x,y) , square_num(x,y)

def add_num(num1, num2):
    num_sum = num1 + num2
    return print(f"The sum is:{num_sum: .2f} ")

def subs_num(num1, num2):
    num_subs = num1 - num2
    return print(f"The substraction is: {num_subs: .2f}")

def mult_num(num1, num2):
    num_mult = num1 * num2
    return print(f"The multiplication is: {num_mult: .2f}")

def div_num(num1, num2):
    num_div = num1 / num2
    return print(f"The division is:{num_div: .2f} ")

def square_num(num1, num2):
    num_square1 = num1 ** 2
    num_square2 = num2 ** 2
    return print(f"square of x is: {num_square1} and square of y is: {num_square2}")

main()