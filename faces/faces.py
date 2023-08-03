def convert():
    userInput = str(input("Type some text!\n"))
    return userInput.replace(":)", "🙂").replace(":(", "🙁")

def main():
    print(convert())

main()