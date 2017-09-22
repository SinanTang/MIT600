### Think Python 2 Ch.15 Classes and Objects

# Exerxise 15.1

import math
import turtle
from shapely.geometry import box

class Point:
    def __init__(self, x, y):
        Point.x = x
        Point.y = y

def print_point(p):
    print('({}, {})'.format(p.x, p.y))

class Circle:
    def __init__(self, x, y, radius):
        Circle.x = x
        Circle.y = y
        # Circle.center = Point(x, y)
        Circle.radius = radius
    def center(self):
        return (self.x, self.y)

cir = Circle(150, 100, 50)
# print(cir.center())
# print(cir.radius)


def point_in_circle(p, circle):
    """
    returns True if the point lies in ot on the bundary of the circle
    :param p: Point object
    :param circle: Circle object
    """
    distance = math.sqrt((p.x - circle.x)**2 + (p.y - circle.y)**2)
    # print(distance)
    if distance <= circle.radius:
        # print(distance, circle.radius)
        return True
    else: return False

p = Point(99, 100)

# print(point_in_circle(p, cir))


class Rectangle:
    def __init__(self, x, y, width, height):
        Rectangle.x = x
        Rectangle.y = y
        Rectangle.width = width
        Rectangle.height = height
    def corner(self):
        return (self.x, self.y)


def rect_in_circle(rect, circle):
    """
    returns True if the rectangle lies entirely or on the boundary of the circle; otherwise False
    :param rect: Rectangle object
    :param circle: Circle object
    :return: Bool
    """
    p1 = Point(rect.x, rect.y)
    p2 = Point(rect.x+rect.width, rect.y)
    p3 = Point(rect.x+rect.width, rect.y+rect.height)
    p4 = Point(rect.x, rect.y+rect.height)

    return point_in_circle(p1, circle) and point_in_circle(p2, circle) and point_in_circle(p3, circle) and point_in_circle(p4, circle)

box = Rectangle(130,90,50,100)

# print(rect_in_circle(box, cir))


def rect_circle_overlap(rect, circle):
    """
    returns True if any of the corners of the rectangle fall inside the circle; False otherwise
    :param rect:
    :param circle:
    :return:
    """
    p1 = Point(rect.x, rect.y)
    p2 = Point(rect.x + rect.width, rect.y)
    p3 = Point(rect.x + rect.width, rect.y + rect.height)
    p4 = Point(rect.x, rect.y + rect.height)

    return point_in_circle(p1, circle) or point_in_circle(p2, circle) \
           or point_in_circle(p3, circle) or point_in_circle(p4, circle)

def rect_circle_overlap2(rect, circle):
    """
    returns True if any part of the rectangle falls inside the circle; False otherwise
    :param rect:
    :param circle:
    :return:
    """
    if rect_in_circle(rect, circle): return True

    rect_center_x = (rect.x + rect.width)/2
    rect_center_y = (rect.y + rect.height)/2
    distance = math.sqrt((rect_center_x - circle.x)**2 + (rect_center_y - circle.y)**2)
    if distance < circle.radius + min((rect.width)/2, (rect.height)/2):
        return True


# using shapely
# rect.intersect(circle)



# Exercise 15.2

bob = turtle.Turtle()

def draw_rect(rect, t):
    t.penup()
    t.setx(rect.x)
    t.sety(rect.y)
    t.pendown()
    t.fd(rect.width)
    t.lt(90)
    t.fd(rect.height)
    t.lt(90)
    t.fd(rect.width)
    t.lt(90)
    t.fd(rect.height)

# print(draw_rect(box, bob))

def arc(t, r, angle):
    circum = 2*r*math.pi*(angle/360)
    for n in range(200):
        t.fd(circum/200)
        t.lt(angle/200)

# print(arc(bob, 30, 360))

def draw_circle(circle, t):
    t.penup()
    t.setx(circle.x)
    t.sety(circle.y)
    t.pendown()
    arc(t, circle.radius, 360)

# print(draw_circle(cir, bob))

turtle.mainloop()