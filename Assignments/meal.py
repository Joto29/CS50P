def main():
    #prompt the user
    inp = input("What time is it? ")
    result = convert(inp)
    
    if result is not None:
        print(result)

def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)/ 60
    converted_time = float(hours + minutes)
    return meal_time(converted_time)

def meal_time(meal_hours):
    if meal_hours >= 7.0 and meal_hours <= 8.0:
        return print("Breakfast Time")
    elif meal_hours >= 12.0 and meal_hours <= 13.0:
        return print("Lunch Time")
    elif meal_hours >= 18.0 and meal_hours <= 19.0:
        return print("Dinner Time")
    else:
        return None

main()
