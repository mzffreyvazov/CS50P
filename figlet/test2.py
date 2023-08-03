def main():
    print(print_percent(convert_percent(user_input())))


def user_input():
    while True:
        try:
            x, y = map(int, input("Fraction: ").split("/"))
            return x, y
        except ValueError:
            pass


def convert_percent(x):
    while True:
        try:
            c = round(float((int(x[0])/int(x[1]))*100), 0)
            return c
        except (ZeroDivisionError):
            pass
def print_percent(c):
    if 99 <= c <= 100:
        return "F"
    elif c > 100:
        pass
    elif c <= 1:
        return "E"
    else:
        return f"{int(c)}%"


if __name__ == "__main__":
    main()
