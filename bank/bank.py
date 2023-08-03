def main():
    grt = input("Hey! ").strip(" .,-_").lower().replace("-", "").replace("_", "").replace(" ", "")
    print(f"${value(grt)}")


def value(greeting):
    if greeting.find("hello", 0) == 0:
        return 0
    elif greeting.find("h", 0) == 0:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()