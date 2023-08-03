def convert(time):
    x, y = time.split(":")
    hour, min = int(x), int(y)
    global converted
    converted = hour + (min/60)
    return float(converted)


def main():
    convert(input("What time is it? "))
    if 7 <= converted <=8:
        print("breakfast time")
    elif 12 <= converted <=13:
        print("lunch time")
    elif 18 <= converted <=19:
         print("dinner time")


main()