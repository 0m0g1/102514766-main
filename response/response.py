import validators


def main():
    if validators.email(input("What's your email address? ")) == True:
        print("Valid")
    else:
        print("Invalid")


main()
