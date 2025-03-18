N = int(input("N:"))

for _ in range(N):
    text = input("Text:")

    msg = ""
    word = ""

    for character in text:
        if character == " ":
            if word != "":
                msg += word[0]
                word = ""
        else:
            word += character

    if word != "":
        msg += word[0]

    print(msg)