import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    return bool(re.search(r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$", ip))


if __name__ == "__main__":
    main()
