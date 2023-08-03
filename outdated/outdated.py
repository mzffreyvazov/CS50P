month_list = [
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
    "December",
]

while True:

    try:
        date = input("Date: ")
        if date.find("/") != -1:
            mm, dd, year = date.split("/")
            if int(mm) == False:
                continue
        elif date.find("/") == -1:
            mmdd, year = date.split(",")
            mm, dd = mmdd.split(" ")
            
            if mm in month_list:
                for i, month in enumerate(month_list, start=1):
                    if month == mm:
                        mm = i
                        break
            else:
                continue

    except (EOFError, ValueError):
        print("")
        continue

    else:
        try:
            if 1 <= int(dd) <= 31 and 1 <= int(mm) <= 12:
                print(f"{year.strip()}-{int(mm):02}-{int(dd):02}")
                break
            else:
                continue
        except ValueError:
            pass

        break
