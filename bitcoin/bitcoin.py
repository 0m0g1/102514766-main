import sys
import requests


def main():
    if len(sys.argv) == 2:
        try:
            print(btc(float(sys.argv[1])))
            return 0
        except:
            sys.exit("Command-line argument is not valid")
    sys.exit("Missing command-line argument")


def btc(n):
    try:
        rsp = requests.get(f"https://api.coindesk.com/v1/bpi/currentprice.json")
        result = rsp.json()
        total = n * result["bpi"]["USD"]["rate_float"]
        return f"${total:,.4f}"

    except requests.ResponseException:
        return None


main()
