### Lec15 Abstract Data Types, Classes and Methods

# Example:
  # points on plane, list
   # Cartesian form: p1 = [1, 2]
   # polar form: p2 = [2, pi/2]

import math
from functools import total_ordering

## points as lists

def addPoints(p1, p2):
    r = []
    r.append(p1[0]+p2[0])
    r.append(p1[1]+p2[1])
    return r

p = [1,2]
q = [3,1]
r = addPoints(p, q)
# print(r)

## points as classes - class as template for creating instances of an object

class cartesianPoint:
    pass

# call class like a function
# cp1, cp2 - instances of this type/class
cp1 = cartesianPoint()
cp2 = cartesianPoint()
# instance has some internal attributes
cp1.x = 1.0
cp1.y = 2.0
cp2.x = 1.0
cp2.y = 3.0

# Shallow Equality (Object Equality) vs Deep Equality (Value Equality)
cp3 = cartesianPoint()
cp3.x = 1.0
cp3.y = 2.0

  # testing Shallow Equality - are the two variables points to the same location in memory
print(cp1 is cp3) # False


def samePoint(p1, p2):
    return (p1.x == p2.x) and (p1.y == p2.y)

  # testing Deep Equality - we can define
print(samePoint(cp1, cp3)) # True

cp3 = cp1
print(cp1 is cp3) # True


def printPoint(p):
    print('('+str(p.x)+','+str(p.y)+')')


class polarPoint:
    pass

pp1 = polarPoint()
pp2 = polarPoint()
pp1.radius = 1.0
pp1.angle = 0
pp2.radius = 2.0
pp2.angle = math.pi / 4.0

class cPoint:
    def __init__(self, x, y):
        # when calling cPoint definition, it calls __init__
        # __init__ () defines the arguments the object takes
        # __init__' creates an instance, use 'self' to refer to that instance (like a pointer)
        self.x = x
        self.y = y
        self.radius = math.sqrt(self.x*self.x + self.y*self.y)
        self.angle = math.atan2(self.y, self.x)
    def cartesian(self):
        # define internal method - can access values of the specific instance
        # p.cartesian() - is a kind of accessor
# ? Data Hiding: one can only access instance values through defined methods
    # Python doesn't do it!
        return (self.x, self.y)
    def polar(self):
        return (self.radius, self.angle)
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'
    def __cmp__(self, other):
        return (self.x > other.x) and (self.y > other.y)


## traditional methods for classes: ##
  # __init__ : create instance
  # __str__ : how to print it out (printed representation)
  # __cmp__ : doing comparisons
  # __eq__ : same

 # operator overloading
# dir(p1)

## Instance - attributes:
    # - methods
    # - fields

class pPoint:
    def __init__(self, r, a):
        self.radius = r
        self.angle = a
        self.x = r * math.cos(a)
        self.y = r * math.sin(a)
    def cartesian(self):
        return (self.x, self.y)
    def polar(self):
        return (self.radius, self.angle)
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'
    def __cmp__(self, other):
        return (self.x > other.x) and (self.y > other.y)


class Segment:
    def __init__(self, start, end):
        # start/end are instances of points
        self.start = start
        self.end = end
    def length(self):
        return math.sqrt( ( (self.start.x - self.end.x) *  # what is x? y?
                            (self.start.x - self.end.x))  # not very hygenic
                        + ( (self.start.y - self.end.y) *
                            (self.start.y - self.end.y)) )

p1 = cPoint(3.0, 4.0)
p2 = cPoint(5.0, 7.0)
s1 = Segment(p1, p2)
print(s1.length())

class Rectangle:
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner

def findCenter(box):
    p = cPoint(box.corner.x + box.width/2.0,
               box.corner.y - box.height/2.0)
    return p

box = Rectangle(100, 200, p1)
print(findCenter(box))

# if the class defines one + __eq__ ordering methods, total_ordering will supply the rest
@total_ordering
class newPoint:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)
    def __add__(self, other):
        return newPoint(self.x + other.x, self.y + other.y)
    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

origin = newPoint()
p1 = newPoint(3.0, 4.0)
p2 = newPoint()
p3 = p1 + p2
print(p3)

# __cmp__ in Python2.7
# throws TypeError in Python 3.6
  # TypeError: '<' not supported between instances of 'newPoint' and 'newPoint'
# __lt__ in Python3.6

print(p1 != p2)
print(dir(p1))





