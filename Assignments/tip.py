def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip: .2f}")

def dollars_to_float(d):
    new_d = d.replace("$","") 
    new_val = float(new_d)
    return new_val

def percent_to_float(p):
    new_p = p.replace("%", "")
    new_val = float(new_p) / 100
    return new_val

main()