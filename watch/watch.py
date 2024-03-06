import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if link := re.search(r'embed([^"]*)', s):
        return f"https://youtu.be/{link.group(0).replace('embed/','')}"
    else:
        return None


if __name__ == "__main__":
    main()
