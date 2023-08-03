def convert():
    inputvar = input("camelCase: ")
    print("snake_case: ", end="")
    for i in inputvar:
        if i.isupper():
            print("_", i.lower(), end="")
        else:
            print(i, end="")
    print()

convert()
