def calculateIdealWeight():
    height = eval(input("Enter your height: "))
    gender = input("Enter your gender (M or F): ")

    if gender == "M":
        weight = (72.7 * height) - 58
    else:
        weight = (62.1 * height) - 44.7

    print("Your ideal weight is", weight)

calculateIdealWeight()

def calculateFinalGrade():
    grade1 = eval(input("Enter your grade: "))
    grade2 = eval(input("Enter your second grade: "))

    median = 0.4 * grade1 + 0.6 * grade2
    approved = median >= 5

    message = approved and "Approved" or "Reproved"
    message += ", your final grade is " + median.__str__()

    print(message)

calculateFinalGrade()