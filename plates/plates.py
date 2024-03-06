def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 1 and len(s) < 7:
        if s.isalpha():
            return True
        if s[0].isalpha() and s[1].isalpha():
            i = 1
            for c in s[2:]:
                if c == "0":
                    return False
                if c.isdigit():
                    if not s[2+i:].isdigit():
                        return False
                    return True
                i += 1
    return False

main()