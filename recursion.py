# from __future__ import division
import time
import turtle
## 5.9
def print_n(s,n):
    if n <= 0:
        return
    print(s)
    print_n(s,n-1)
# print_n("hello",2)
def do_n(f,n):
    if n <= 0:  # the base case
        return
    f("hello",2)
    do_n(f, n-1)
# do_n(print_n, 3)

## 5.10
#floor division
# print 5/2, 5//2, 5.0/2, 5.0//2

# Exercise 5.1
# the epoch: January 1, 1970 - Jan 1 2017 - Apr 25 2017 [Greenwich mean time]
# print time.time()
jan17insec = time.time() - ((2017-1970)*365+11)*24*60*60
# print jan17insec
apr27inhour = (jan17insec - (31+28+31+27)*24*60*60)/3600.0
# print apr27inhour

def tell_me_time():
    second_since_epoch = time.time()
    hours = second_since_epoch/3600
    while hours > 24:
        hours = hours - 24
    print("the current time is", int(hours), "in hours", int(hours*60), "in minutes", int(hours*60*60), "in seconds")
    days_since_epoch = int(second_since_epoch)//(3600*24)
    print("It is", days_since_epoch, "days since the epoch!")

# tell_me_time()

# Exercise 5.2 - Fermat's Last Theorem
def check_fermat(a,b,c,n):
    while n > 2:
        if a**n + b**n == c**n:
            return "Holy smokes, Fermat was wrong!"
        else: return "No, that doesn't work."

def user_fermat():
    a = int(input("Please enter the first integer: "))
    b = int(input("Please enter the second integer: "))
    c = int(input("Please enter the third integer: "))
    n = int(input("Please enter the exponent as integer: "))
    return check_fermat(a,b,c,n)

# print(user_fermat())  #only checks for user-provided input

# Exercise 5.3 - test whether 3 lengths can form a triangle
def is_triangle(a,b,c):
    if a>b+c or b>a+c or c>a+b:
        return "No"
    else: return "Yes"
def user_triangle():
    a = int(input("Please enter the first length: "))
    b = int(input("Please enter the second length: "))
    c = int(input("Please enter the third length: "))
    return is_triangle(a, b, c)

# print(user_triangle())

# Exercise 5.4
def recurse(n, s):
    """returns the the sum of n from 1+2+3+...+n plus s, n needs to be positive or 0""" #triple quote needs to be indented too
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)
# recurse(2, 2)
# recurse(3, 2)
# recurse(4, 2)
# recurse(5, 2)
# recurse(6, 2)
# recurse(7, 2)
# recurse(8, 2)

# Exercise 5.5
def draw(t, length, n):
    # print("draw called with", n)
    if n==0:
        # print("about to return from base case")
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t,length, n-1)
    t.rt(2*angle)
    draw(t,length, n-1)
    t.lt(angle)
    t.bk(length*n)

# t = turtle.Turtle()
# t.color("blue")
# draw(t, 20, 2)

# Exercise 5.6 a Koch curve
def koch(t, length):
    angle = 60
    if length < 3:
        return t.fd(length)
        # t.fd(length)
        # t.lt(angle)
        # t.fd(length)
        # t.rt(angle * 2)
        # t.fd(length)
        # t.lt(angle)
        # t.fd(length)
    else:
        koch(t, length/3)
        t.lt(angle)
        koch(t, length/3)
        t.rt(angle*2)
        koch(t, length/3)
        t.lt(angle)
        koch(t, length/3)

# koch(t, 180)
# sc = turtle.Screen()
def snowflake(t, len):
    koch(t, len)
    t.rt(120)
    koch(t, len)
    t.rt(120)
    koch(t, len)

# snowflake(t, 200)
# turtle.mainloop()

## 6.5
# define factorial function
def factorial(n):
    if n == 0:
        return 1
    else:
        # result = n*factorial(n-1)
        return n*factorial(n-1)

#print factorial(4)

## 6.7
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(10))

## 6.8 checking types
def factorial2(n):
    if not isinstance(n, int):            # guardian
        print('Factorial2 is only defined for integers.')
        return None
    elif n < 0:                           # guardian
        print('Factorial is not defined for negative integers.')
        return None
    elif n == 0:
        return 1
    else:
        return n*factorial2(n-1)

# print(factorial2(5))
# print(factorial2(-4))
# print(factorial2(2.5))

### Think Python Ch. 6 exercises
# Exercise 6.1 draw stack diagram
def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod
def a(x, y):
    x = x + 1
    return x * y
def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

x = 1
y = x+1
# print(c(x, y+3, x+y))

# Exercise 6.2 The Ackermann function
def ack(m, n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    elif m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))
    else:
        return None

# print(ack(3,0))

# Exercise 6.3 palindrome
def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]

# print(middle('mem'))
# print(middle('me'))
# print(middle('m'))

def is_palindrome(word):
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and is_palindrome(word[1:-1])

# print(is_palindrome('afddfa'))
# print(is_palindrome('abcba'))
# print(is_palindrome('abc'))

# Exercise 6.4
def is_power(a, b):
    if b == 0:
        return 'b should be a non-zero number.'
    elif a == 1:
        return True
    else:
        return a % b == 0 and is_power(a/b, b)

# print(is_power(16, -2))

# Exercise 6.5 the greatest common divisor GCD
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# print(gcd(28,96))
# print(8%12)