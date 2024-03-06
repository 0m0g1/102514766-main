camel = input("Camel: ")
for c in camel:
    if c.islower():
        print(c, end="")
    elif c.isupper():
        print("_",c.lower(),end="",sep="")
print("")