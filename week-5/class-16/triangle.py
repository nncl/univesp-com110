def drawAndDefineTriangleType():
    side_a = eval(input("Enter side A: "))
    side_b = eval(input("Enter side B: "))
    side_c = eval(input("Enter side C: "))

    bigger_side = max(side_a, side_b, side_c)

    if bigger_side >= side_a + side_b + side_c - bigger_side:
        return print("It's NOT a triangle.")

    print("Congratulations! It's a triangle.")

    if side_a == side_b and side_b == side_c and side_a == side_c:
        return print("Equilateral")

    if side_a != side_b and side_b != side_c and side_a != side_c:
        return print("Scalene")

    return print("Isosceles")


drawAndDefineTriangleType()

def temperature(temp: float):
    if temp > 86:
        print("Hot")
    elif temp > 32:
        print("Cold")
    else:
        print("Freaking cold")

temperature(20)