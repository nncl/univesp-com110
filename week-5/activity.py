def calculateBiggerNumber():
    number_1 = eval(input("Type the number 1: "))
    number_2 = eval(input("Type the number 2: "))
    number_3 = eval(input("Type the number 3: "))

    if (number_1 > number_2) and (number_1 > number_3) and (number_2 > number_3):
        print("The biggest is the first number: ", number_1)

    if (number_2 > number_1) and (number_2 > number_3) and (number_3 > number_1):
        print("Te biggest is the second number: ", number_2)

    if (number_3 > number_1) and (number_3 > number_2) and (number_1 > number_2):
        print("The biggest is the third number: ", number_3)

    print("End")

calculateBiggerNumber()