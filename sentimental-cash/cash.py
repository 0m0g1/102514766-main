# get change
def main():
    # try if the code runs rerun the function if there is an error
    try:
        change = (float(input("What is the change?")) * 100)
        coins = 0

        # check if the input is less than 0
        if change < 0:
            main()

        # gets change
        while change > 24:
            change -= 25
            coins += 1
        while change > 9:
            change -= 10
            coins += 1
        while change > 4:
            change -= 5
            coins += 1
        while change > 0:
            change -= 1
            coins += 1
        print(coins)

    # if any error occurred re-prompt the user
    except:
        main()


main()