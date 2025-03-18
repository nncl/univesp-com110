N = int(input("N:"))

for _ in range(N):
    text = input("Text:")

    msg = ""
    word = ""

    for character in text.replace(" ", ""):
        word += character

    if word != "":
        msg += word[0]

    print(msg)