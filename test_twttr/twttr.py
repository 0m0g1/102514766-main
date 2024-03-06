def main():
    print("Output: ", shorten(input("Input: ").strip()))


def shorten(word):
    for c in ["a", "e", "i", "o", "u"]:
        word = word.replace(c, "")
    return word


if __name__ == "__main__":
    main()
