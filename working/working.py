import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    regex = "(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
    match = re.search(r"^" + regex + " to " + regex + "$", s)
    if match:
        start = hr24(match.group(1), match.group(2), match.group(3))
        fin = hr24(match.group(4), match.group(5), match.group(6))
        return f"{start} to {fin}"
    else:
        raise ValueError


def hr24(hr=0, min=0, x="AM"):
    if min == None:
        min = 0
    hr = int(hr)
    min = int(min)
    if hr != 12 and x == "PM":
        hr += 12
    if hr == 12 and x == "AM":
        hr = 0
    return f"{hr:02}:{min:02}"


if __name__ == "__main__":
    main()