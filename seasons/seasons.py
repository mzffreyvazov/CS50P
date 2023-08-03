from datetime import date
import inflect
import sys

def main():
    s = input("Date Of Birth: ")
    convert(s)


def convert(s):
    try:
        year, month, day = s.split("-")
    except ValueError:
        sys.exit("Invalid date")
    now = date.today()
    birthday = date(int(year), int(month), int(day))
    diff = round(int(str(now - birthday).split(",")[0].split()[0])*1440)
    p = inflect.engine()
    def convert_number_to_words(num, andword=''):
        return p.number_to_words(num, andword=andword)

    print(convert_number_to_words(diff).capitalize(), "minutes")


if __name__ == "__main__":
    main()