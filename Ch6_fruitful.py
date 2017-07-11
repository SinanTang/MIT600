#6.1
import math

def area(radius):
    a = math.pi * radius**2
    return a # "return immediately from this function and use the following expression as a return value"

def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x

def compare(x, y):
    if x > y:
        return 1
    if x == y:
        return 0
    if x < y:
        return -1

# print compare(4,5)
# print compare(5,5)
# print compare(-3,-10)

#6.2
def distance(x1, y1, x2, y2):
    a = (x1-x2)**2
    b = (y1-y2)**2
    c = math.sqrt(a+b)
    return float(c) # or c, both the same
#print distance(1,1,2,2)

def hypotenuse(a,b):
    c = math.sqrt(a**2+b**2)
    return c
#print hypotenuse(3,4)

# 6.3
def circle_area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result
# composing the function call
def circle_area2(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))
#print circle_area2(1,1,4,4)

# 6.4
def is_divisible(x,y):
    return x%y == 0
#print is_divisible(9,4)
# if is_divisible(2,1):
#     print "x is divisible by y"

def is_between(x,y,z):
    if x<= y and y<= z:
        return True
    else: return False
# print is_between(5,4,6)