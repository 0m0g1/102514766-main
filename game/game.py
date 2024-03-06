from random import randint

while True:
    try:
        lv = int(input("Level: "))
        x = randint(1, lv)
        guess = int(input("Guess: "))
        if guess < 0:
            raise ValueError
        if guess < x:
            print("Too small!")
        elif guess > x:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
    except EOFError:
        break
