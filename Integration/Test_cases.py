#  Test the triangle is scalene or not?


import Triangle_shap
...


def test_is_scalene_triangle():
    assert Triangle_shap.scalene_triangle(30, 50, 20) == "scalene Triangle"
    #print("The triangle is scalene.")


def test_is_isosceles_triangle():
   assert Triangle_shap.isosceles_triangle(30, 50, 30) == "isosceles Triangle"
   #print("The triangle is isosceles.")


def test_is_equilateral_triangle():
  assert Triangle_shap.equilateral_triangle(50, 50, 50) == "Equilateral Triangle"
  #print("The triangle is Equilateral.")


# Call the test functions
# is_scalene_triangle()
# is_isosceles_triangle()
# is_equilateral_triangle()