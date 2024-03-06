import csv
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if sys.argv[1].split(".")[1] != "csv" or sys.argv[2].split(".")[1] != "csv":
        sys.exit("Not a CSV file")

    people = []
    with open(sys.argv[1], "r") as f:
        reader = csv.DictReader(f)
        for person in reader:
            first, last = person["name"].split(", ")
            new_p = {}
            new_p["first"] = last
            new_p["last"] = first
            new_p["house"] = person["house"]
            people.append(new_p)

    with open(sys.argv[2], "w") as f:
        writer = csv.DictWriter(f, ["first", "last", "house"])
        writer.writeheader()
        writer.writerows(people)


main()
