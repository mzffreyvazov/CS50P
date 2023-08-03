import re

def main():
    print(count(input("Text: ").lower()))


def count(s):
    result = re.findall(r"\b(um)\b", s, re.IGNORECASE)
    return len(result)
    
if __name__ == "__main__":
    main()