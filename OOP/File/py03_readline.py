file = open("readme.md")
while True:
    text = file.readline()
    if not text:
        break

    print(text, end="")
file.close()
