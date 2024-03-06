import re

print(bool(re.search(r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$", (input("IPv4 Address: ")))))
