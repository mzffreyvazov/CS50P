def main():
    userinput = input("Input: ")
    print("Output: ", end="")
    print(shorten(userinput), end="\n")

def shorten(word):
    f_word = ""
    for j in word:
        if j.lower() in ["a", "e", "o", "i", "u"]:
            pass
        else:
            f_word = f_word + j
    return f_word

if __name__ == "__main__":
    main()
