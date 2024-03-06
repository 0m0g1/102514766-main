def main():
    print(get_fraction("Fraction: "))


def get_fraction(prompt):
    while True:
        try:
            x, y = input(prompt).split("/")
            z = round((int(x)/int(y))*100)
            if int(x) > int(y):
                raise ValueError
            if z <= 1:
                return("E")
            elif z >= 99:
                return("F")
            else:
                return str(z) + "%"
        except (ValueError, ZeroDivisionError):
            pass


main()