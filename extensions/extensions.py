file = input("File name: ").lower().strip().split(".")

if file[-1] in ["png","gif"]:
    print(f'image/{file[-1]}')
elif file[-1] in ["jpeg","jpg"]:
    print("image/jpeg")
elif file[-1] in ["pdf","zip"]:
    print(f'application/{file[-1]}')
elif file[-1] == "txt":
    print("text/plain")
else:
    print("application/octet-stream")