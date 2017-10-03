# 6.00 Problem Set 9
#


from string import *


class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")


class Square(Shape):
    def __init__(self, h=1):
        """
        h: length of side of the square
        """
        self.side = float(h)

    def area(self):
        """
        Returns area of the square
        """
        return self.side ** 2

    def __str__(self):
        return 'Square with side ' + str(self.side)

    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side


class Circle(Shape):
    def __init__(self, radius=1):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)

    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159 * (self.radius ** 2)

    def __str__(self):
        return 'Circle with radius ' + str(self.radius)

    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius


#
# Problem 1: Create the Triangle class
#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.
class Triangle(Shape):
    def __init__(self, h=1, base=1):
        self.h = float(h)
        self.base = float(base)

    def __str__(self):
        return "Triangle with base {:.1f} and height {:.1f}".format(self.base, self.h)

    def area(self):
        return 0.5 * self.h * self.base

    def __eq__(self, other):
        return type(other) == Triangle and self.base == other.base and self.h == other.h


# print(type(tri)==Triangle)
# print(str(tri))

#
# Problem 2: Create the ShapeSet class
#

class ShapeSet:
    def __init__(self):
        """
        Initialize any needed variables
        self.members: {val:'Square',}
        """
        self.members = []
        # self.types = []
        self.place = None

    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        # if type(sh) != (Triangle or Square or Circle): raise TypeError('not a shape')
        # for member in self.members:
        #     if sh == member: raise ValueError('duplicate shape')
        if sh not in self.members:
            self.members.append(sh)

    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        self.place = 0
        return self

    def __next__(self):
        if self.place >= len(self.members):
            raise StopIteration
        self.place += 1
        return self.members[self.place-1]

    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        # self.members.sort()
        mystring = ''
        mystring += self.print_type(Circle)
        mystring += self.print_type(Square)
        mystring += self.print_type(Triangle)

        return mystring

    def print_type(self, tp):
        mystring = ''
        for member in self.members:
            if type(member) == tp:
                mystring += str(member) + '\n'
        return mystring



shapeset = ShapeSet()
cir = Circle()
cir2 = Circle(2)
sq = Square()
sq2 = Square(2)
tri = Triangle(5,40)
tri2 = Triangle(40,5)
shapeset.addShape(tri)
shapeset.addShape(tri2)
shapeset.addShape(cir)
shapeset.addShape(cir2)
shapeset.addShape(sq)
shapeset.addShape(sq2)

# print(cir2.area())
# print(shapeset)
# print()
# for shape in shapeset:
#     print(str(shape)+'\n')


#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    # i think this is a better solution
    """
    areas = {}
    for shape in shapes:
         areas[str(shape)] = shape.area()

    largest = 0
    result = []
    for area in areas:
        if areas[area] > largest:
            largest = areas[area]

    for key, val in areas.items():
        if val == largest:
            result.append(key)
    return tuple(result)

# print(findLargest(shapeset))

# large = findLargest(shapeset)
# for i in large:
#     print(i)



#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    ss = ShapeSet()

    with open(filename) as f:
        for line in f.readlines():
            shape = line.rstrip().split(',')
            if shape[0] == 'circle':
                cir = Circle(float(shape[1]))
                ss.addShape(cir)
            elif shape[0] == 'square':
                sq = Square(float(shape[1]))
                ss.addShape(sq)
            elif shape[0] == 'triangle':
                tri = Triangle(float(shape[1]), float(shape[2]))
                ss.addShape(tri)

    return ss

ss = readShapesFromFile('shapes.txt')
print(ss)
