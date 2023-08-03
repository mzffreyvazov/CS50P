import emoji
def main():
    asciiemoji = convert(input)
    print("Output: ", emoji.emojize(asciiemoji))
def convert(userinput):
    userinput = input("Input: ")
    #print(f"Output: {emoji.emojize(userinput)}")
    return userinput
main()