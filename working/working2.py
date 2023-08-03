import re

def main():
    print(convert(input("Hours: ").lower()))


def convert(s):

    #parts = re.search(r"([0-9]):?([0-9].)? (.+) to ([0-9]):?([0-9].)? (.+)", s)
    parts = re.search(r"(\d+)(?::(\d+))?\s(am|pm)\sto\s(\d+)(?::(\d+))?\s(am|pm)", s)
    try:
        #check if the minutes are correct
        if parts.group(2) and parts.group(5):
            if int(parts.group(2)) >= 60 or int(parts.group(5)) > 60:
                raise ValueError("incorrect minutes")

        if parts.group(3) == "am":
            if len(parts.group(1)) == 1:
                hour1 = f"0{parts.group(1)}"
            else:
                hour1 = parts.group(1)
        else:
            hour1 = str(int(parts.group(1)) + 12)

        if parts.group(6) == "am":
            if len(parts.group(4)) == 1:
                hour2 = f"0{parts.group(4)}"
            else:
                hour2 = parts.group(4)
        else:
            hour2 = str(int(parts.group(4)) + 12)

        if parts.group(2):
            return hour1 + f":{parts.group(2)}" + " to " + hour2 + f":{parts.group(5)}"
        else:
            return hour1 + ":00" + " to " + hour2 + ":00"


    except AttributeError:
        print("ValueError")

if __name__ == "__main__":
    main()