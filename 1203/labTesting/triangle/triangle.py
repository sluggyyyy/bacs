# This is a 

import math  # for acos

def triangleType(a, b, c):

    ttype = ""
    
    # Can only be a triangle if 2 of the sides are greater or equal to the other side
    if a+b<c or a+c<b or b+c<a:
        return "Not Triangle"
    
    # We know have a valid triangle
    
    # We can determine if it is Equilateral, Isosceles, or Scalane
    #   based only on the sides
    if a == b == c:
        ttype = "Equilateral"
    elif a == b or a == c or b == c:
        ttype = "Isosceles"
    else:
        ttype = "Scalene"

    # law of cosines to solve for the angles
    C = math.degrees(math.acos((a**2 + b**2 - c**2)/(2*a*b)))
    A = math.degrees(math.acos((b**2 + c**2 - a**2)/(2*b*c)))
    # To avoid numerical percision issues we solve for the other to get 180
    B = 180.0 - A - C

    # acute - all angles < 90
    # right - one angle 90 (the others 45)
    # obtuse - one angle > 90 (meaning the others < 90)
    tol = 0.000001
    if math.fabs(A-90)<tol or math.fabs(B-90)<tol or math.fabs(C-90)<tol:
        ttype += " Right"
    elif A>90 or B>90 or C>90:
        ttype += " Obtuse"
    else:
        ttype += " Acute"

    return ttype
