glist = {}
while True:
    try:
        new = input("").upper().strip()
        if new in glist:
            glist[new] += 1
        else:
            glist[new] = 1
    except EOFError:
        for item in dict(sorted(list(glist.items()))):
            print(f"{glist[item]} {item}")
        break
    except KeyError:
        break
