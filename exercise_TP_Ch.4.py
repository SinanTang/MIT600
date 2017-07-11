# def bad_append(new_item, a_list=[]):
    # a_list.append(new_item)
    # return a_list
#print bad_append('one')
#print bad_append('two')

# def good_append(new_item, a_list=None):
    # if a_list is None:
        # a_list = []
    # a_list.append(new_item)
    # return a_list
    
#print good_append('three')
#print good_append('four')


# str = raw_input('Please type a word: ')
# num = raw_input('please type a number: ')

# print str*int(num)

# x = 15
# if (x/2)*2 == x:
    # print 'Even'
# else: print 'Odd'

# x = 15
# y = 13
# z = 11
# print x,y,z
# if x<y:
    # if x<z: print 'x is the smallest'
    # else: print 'z is the smallest'
# else: print 'y is the smallest'  # this code missed other possible path

# if x<y and x<z: print 'x is the smallest'
# elif y<z: print 'y is the smallest'
# else: print 'z is the smallest'

# squring a int
# y = 0
# x = 4
# itersLeft = x
# while (itersLeft>0):
    # y = y+x
    # itersLeft = itersLeft - 1
    
# print y


## Think Python Ch 4
# import turtle
# bob = turtle.Turtle()
# print(bob)
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)
# for i in range(4):
    # #print('Hello!')
    # bob.fd(100)
    # bob.lt(90)
# turtle.mainloop()


import math
import turtle
bob = turtle.Turtle()

# def square(t, length):
    # for i in range(4):
        # t.fd(length)
        # t.lt(90)
    
# square(bob, 150)

# def polygon(t, length, n):
    # for i in range(n):
        # t.fd(length)
        # t.lt(360.0/n)

# polygon(bob, length=15, n=30) #keyword arguments 

# def circle(t, r):
     # #polygon(t, (math.pi*r)/15, 30)
     # circumference = 2 * math.pi * r
     # n = int(circumference / 3) + 3
     # length = circumference / n
     # polygon(t, n, length)
            
# #circle(bob, 30)

# def arc(t, r, angle):
    # for i in range(30*(angle/360)):
        # circle(t, r)

# arc(bob, 30, 180)

## refactoring
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)
        
def polygon(t, n, length):
    angle = 360.0/n
    polyline(t, n, length, angle)
    
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle/360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n 
    polyline(t, n, step_length, step_angle)
    
def circle(t, r):
    arc(t, r, 360)

arc(bob, 60, 199)    
    
turtle.mainloop()

















