# 4 * 3 * 2 = 24
def asks_factorial() -> int:
    num = eval(input("Enter a number: "))
    factorial = 1 # <-
    x = 1

    while x <= num:
        factorial *= x # <- OR factorial = factorial from the exercise
        x += 1

    return factorial

print(asks_factorial())