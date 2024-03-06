import sys
import inflect
from datetime import date, datetime


def main():
    try:
        dob = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid date")
    print(totext(calc_difference(dob)))


def calc_difference(days):
    today = date.today()
    dif = today - days
    return dif.days * 1440


def totext(text):
    text = inflect.engine().number_to_words(text, andword="")
    return text.capitalize() + " minutes"


if __name__ == "__main__":
    main()
