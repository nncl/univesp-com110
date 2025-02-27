def drawAndDefineTriangleType():
    side_a = eval(input("Enter side A: "))
    side_b = eval(input("Enter side B: "))
    side_c = eval(input("Enter side C: "))

    bigger_side = 0
    if side_a > bigger_side:
        bigger_side = side_a
    if side_b > bigger_side:
        bigger_side = side_b
    if side_c > bigger_side:
        bigger_side = side_c

    if bigger_side < side_a + side_b + side_c - bigger_side:
         print("Congratulations! It's a triangle.")

         if side_a == side_b and side_b == side_c and side_a == side_c:
             print("Equilateral")
         elif side_a != side_b and side_b != side_c and side_a != side_c:
             print("Scalene")
         else:
             print("Isosceles")
    else:
        print("It's NOT a triangle.")

drawAndDefineTriangleType()