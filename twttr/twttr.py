print("Output: ", end="")
for c in input("Input: "):
    if c.lower() not in ["a","e","i","o","u"]:
        print(c, end="")
print("")