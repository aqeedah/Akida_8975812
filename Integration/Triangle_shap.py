# # Request input from the user for the length of side 'side1' and convert it to an integer
# side1 = int(input("Enter the length of side 1: "))
#
# # Request input from the user for the length of side '2' and convert it to an integer
# side2 = int(input("Enter the length of side 2: "))
#
# # Request input from the user for the length of side '3' and convert it to an integer
# side3 = int(input("Enter the length of side 3: "))



def scalene_triangle(side1, side2,side3):
    if side1 != side2 and side1 != side3 and side2 != side3:
      return "scalene Triangle"
    else:
        return None


# If at least two sides are equal, display that it's an isosceles triangle
def isosceles_triangle(side1, side2, side3):
    if side1 == side2 and side1 == side3 or side2 == side3:
      return "isosceles Triangle"
    else:
        return None


# If all sides are equal, display that it's an equilateral triangle
def equilateral_triangle(side1, side2, side3):
    if side1 == side2 or side1 == side3 and side2 == side3:
      return "Equilateral Triangle"
    else:
        return None


