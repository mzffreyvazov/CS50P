menu_dict = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    first = 0
    while True:
        try:
            current = calc_price()
            first += menu_dict[current]
            print(f"Total: ${first:.2f}")
        except (EOFError):
            print("\n", end="")
            break

def calc_price():

    while True:
        try:
            userinput = input("Item: ").title()
            return userinput
        except (ValueError, KeyError, TypeError):
            pass

main()