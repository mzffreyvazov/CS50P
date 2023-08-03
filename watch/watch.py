import re

def main():
    print("The link is:", parse(input("HTML: ")))


def parse(s):
    try:
        parts = re.search(r'<iframe.+(https?[^"]+).+<\/iframe>', s)
        if "youtube" not in parts.group(1):
            return None
        else:
            link = re.sub(r"https?:\/\/(?:www\.)?youtube.+/embed", "https://youtu.be", parts.group(1))
        return link
    except:
        return None

if __name__ == "__main__":
    main()