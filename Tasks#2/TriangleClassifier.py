sideA = int(input("Enter the side A of the triangle \n"))
sideB = int(input("Enter the side B of the triangle \n"))
sideC = int(input("Enter the side C of the triangle \n"))

if sideA <= 0 or sideB <= 0 or sideC <= 0:
    print("Invalid sides of the triangle")
elif sideA == sideB == sideC:
    print("Given sides of a triangle is an EQUILATERAL triangle")
elif sideA == sideB or sideA == sideC or sideB == sideC:
    print("Given sides of a triangle is an ISOSCELES triangle")
else:
    print("Given sides of a triangle is an SCALENE triangle")
