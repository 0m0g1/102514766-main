import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if sys.argv[1].split(".")[1] != "py":
        sys.exit("Not a Python file")
    try:
        lines = 0
        with open(sys.argv[1], "r") as f:
            for line in f:
                if not (line.strip() == "" or line.strip().startswith("#")):
                    lines += 1
            print(lines)
    except FileNotFoundError:
        sys.exit("File does not exist")
    except:
        sys.exit("Error oppening file")


main()
