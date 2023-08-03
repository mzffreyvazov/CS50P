def main():
    while True:
        fraction = input("Enter fuel level as a fraction (e.g. 1/2): ")
        try:
            percentage = convert(fraction)
            gauge_str = gauge(percentage)
            print(gauge_str)
            break
        except ValueError:
            print("Invalid input. Please enter a fraction in X/Y format where X and Y are integers and X <= Y.")
        except ZeroDivisionError:
            print("Invalid input. Y cannot be zero.")

def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if x > y:
        raise ValueError("X cannot be greater than Y")
    percentage = round(x / y * 100)
    return percentage

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
