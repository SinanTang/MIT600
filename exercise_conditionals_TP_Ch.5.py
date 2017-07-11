#Ch. 4 Conditionals & Recursion (4.1-4.8)

# #floor division
# quotient = 7/3
# # quotient = 7//3 in Python 3
# print quotient

# remainder = 7%3
# print remainder

# #boolean expressions
# print 5==5
# print 6<=7
# print type(True), type (False)

#logical operators
# print 42 and True #any nonzero number is interpreted as 'true'
# x = 5
# print x and 1, 1 and x #1,5 -> if x is false, then y, else x
# print 6 or False, 7 or True #6,7 -> if x is false, then x, else y 

# x = int(raw_input("please enter a number: "))
# if x < 0:
    # pass # as a place keeper for future codes
# else:
    # print 'x>=o'
    
# def printParity(x):
    # if x%2 == 0:
        # print x, "is even"
    # else:
        # print x, "is odd"
# printParity(5), printParity(-7), printParity(0)

# def compare(x, y):
    # if x < y:
        # print x, "is less than", y
    # elif x > y:
        # print x, "is greater than", y
    # else:
        # print x, "and",y, "are equal"
# compare(0, -6)

#x = int(raw_input("please enter a number: "))
# if 0 < x < 10:
    # print x, "is a positive single-digit number."
    
import math
def printLogarithm(x):
    if x <= 0:
        print "positive number only, plz."
        return #exit immediately
    result = math.log(x)
    print "The log of", x, "is", result
x = int(raw_input("please enter a number: "))
printLogarithm(x)