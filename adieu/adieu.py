import inflect

names = []

while True:
    try:
        names.append(input("Name: ").title().strip())
    except EOFError:
        print("\nAdieu, adieu, to " + inflect.engine().join(names))
        break
