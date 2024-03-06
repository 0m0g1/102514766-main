import csv
import sys
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if sys.argv[1].split(".")[1] != "csv":
        sys.exit("Not a CSV file")
    print(table(sys.argv[1]))


def table(file):
    try:
        rows = []
        with open(file, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                rows.append(row)
            print(rows)
        return tabulate(rows, headers="firstrow", tablefmt="grid")
    except FileNotFoundError:
        sys.exit("File does not exist")


main()
