#Ask the user for the date:
list_of_months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def main():
    while True:
        try:
            date = input("Date: ")
            if "/" in date:
                print(convert_date_a(date))
                return 
            for month in list_of_months:
                if month in date:
                    print(convert_date_b(date))
                    return
        except ValueError:
            pass


def convert_date_a(date):
    #convert the input to valid numbers 
    month, day, year = date.split("/")

    month = int(month)
    day = int(day)
    year = int(year)

    if  1 <= day <= 31 and 1 <= month <= 12 :
        return f"{year}-{month:02d}-{day}"
    else:
        raise ValueError

def convert_date_b(date):
    for month in list_of_months:
        if month in date:
            month, day, year = date.replace(",", "").split()
            month = list_of_months.index(month) + 1
            day = int(day)
            year = int(year)

            if  1 <= day <= 31 and 1 <= month <= 12 :
                return f"{year}-{month:02d}-{day}"
            else:
                raise ValueError

main()