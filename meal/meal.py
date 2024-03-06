def main():
    time = convert(input("What is the time? ").strip())
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")
    return

def convert(time):
    hr, mins = time.split(":")
    return (float(hr)+float(mins)*(1/60))


if __name__ == "__main__":
    main()