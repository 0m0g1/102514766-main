def main():
    print(gauge(convert(input("Fraction: "))))


def convert(fraction):
    try:
        x, y = fraction.split("/")
        if int(x) > int(y):
            raise ValueError
        if int(y) == 0:
            raise ZeroDivisionError
        return round((int(x) / int(y)) * 100)
    except:
        return None

def gauge(percentage):
    try:
        if percentage <= 1:
            return "E"
        elif percentage >= 99:
            return "F"
        else:
            return str(percentage) + "%"
    except:
        pass


if __name__ == "__main__":
    main()