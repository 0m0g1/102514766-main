from random import randint


def main():
    lv = get_level()
    score = 0
    for i in range(10):
        qn = f"{generate_integer(lv)} + {generate_integer(lv)} = "
        ans = eval(qn.replace(" ", "").replace("=", ""))
        tries = 0
        for j in range(4):
            if tries == 3:
                print(ans)
                break
            try:
                if int(input(qn)) == ans:
                    score += 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("EEE")
                tries += 1
                continue
    print(f"Score: {score}")


def get_level():
    level = input("Level: ").strip()
    try:
        if int(level) in [1, 2, 3]:
            return int(level)
        else:
            raise ValueError
    except ValueError:
        main()


def generate_integer(level):
    if level == 1:
        return randint(0, 9)
    elif level == 2:
        return randint(10, 99)
    elif level == 3:
        return randint(100, 999)


if __name__ == "__main__":
    main()
