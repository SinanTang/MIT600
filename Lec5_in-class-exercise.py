## using bisection to approximate the square root of input number
def squareRootBi(x, epsilon):
    """
    :param x: number to be squared
    :param epsilon: the precision the square root expects to be
    :return: the approximate square root of input x
    """
    assert x >= 0, "x must be non-negative, not " + str(x)
    assert epsilon > 0, "epsilon must be positive, not " + str(epsilon)
    # ? the bug: when there's a perfect square, the function doesn't give the integer. --> its not a bug
    # for i in range(x):
    #     if i**2 == x:
    #         return i
    #     else: pass

    # REAL BUG: cant compute the square root of number less than 1

#==== my solution: not very elegant
    # if x >= 1.0 :
    #     low = 0
    #     high = x
    #     guess = (low + high)/2.0
    #     count = 1
    #     while abs(guess**2 - x) > epsilon and count <= 100:
    #         print "High: ", high, ", Low: ", low, ", Guess: ", guess
    #         if guess**2 < x:
    #             low = guess
    #         else:
    #             high = guess
    #         guess = (low + high)/2.0
    #         count += 1
    # if x < 1.0 :
    #     low = x
    #     high = 1.0
    #     guess = (low + high)/2.0
    #     count = 1
    #     while abs(guess**2 - x) > epsilon and count <= 100:
    #         print "High: ", high, ", Low: ", low, ", Guess: ", guess
    #         if guess**2 < x:
    #             low = guess
    #         else:
    #             high = guess
    #         guess = (low + high)/2.0
    #         count += 1

#=== Prof's solution, much better
    low = 0
    high = max(x, 1.0)  ## when you need to evaluate
    guess = (low + high)/2.0
    count = 1
    while abs(guess**2 - x) > epsilon and count <= 100:
        # print "High: ", high, ", Low: ", low, ", Guess: ", guess
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high)/2.0
        count += 1

    assert count <= 100, "Iteration count exceeded"
    print "Bi method. Num iteration: ", count, "Estimate: ", guess
    return guess

# print squareRootBi(0.125, 0.0001), "\n", squareRootBi(16, 0.0001)

## better way to do testing - regression testing: make sure that things used to work will still work later

def testBi():
    print "squareRootBi(4, 0.0001)"
    squareRootBi(4, 0.0001)
    print "squareRootBi(8, 0.0001)"
    squareRootBi(8, 0.0001)
    print "squareRootBi(16, 0.0001)"
    squareRootBi(16, 0.0001)
    print "squareRootBi(0.25, 0.0001)"
    squareRootBi(0.25, 0.0001)

# testBi()


### Lecture 6
# speed of convergence (of bisection methods)
# Newton/Raphson method

def squareRootNR(x, epsilon):
    """Assume x >= 0 and epsilon > 0
    Return y s.t. y*y is within epsilon of x"""
    assert x>= 0, "x must be non-negative, not" + str(x)
    assert epsilon > 0, "epsilon must be positive, not" + str(epsilon)
    x = float(x)
    guess = x/2.0 # experimenting with different guesses
    # guess = 0.001
    diff = guess**2 - x
    ctr = 1
    while abs(diff) > epsilon and ctr <= 100:
        # print 'Error:', diff, 'guess:' guess
        guess = guess - diff/(2.0*guess)
        diff = guess**2 - x
        ctr += 1
    assert ctr <= 100, "Iteration count exceeded"
    print "NR method. Num. iteration:", ctr, "Estimate:", guess
    return guess

def compareMethods():
    print "squareRoot(2, 0.01)"
    squareRootBi(2, 0.01)
    squareRootNR(2, 0.01)
    raw_input()
    print "squareRoot(2, 0.001)"
    squareRootBi(2, 0.001)
    squareRootNR(2, 0.001)
    raw_input()
    print "squareRoot(2, 0.0001)"
    squareRootBi(2, 0.0001)
    squareRootNR(2, 0.0001)
    raw_input()
    print "squareRoot(123456789, 0.0001)"
    squareRootBi(123456789, 0.0001)
    squareRootNR(123456789, 0.0001)
    raw_input()
    print "squareRoot(123456789, 0.000001)"
    squareRootBi(123456789, 0.000001)
    squareRootNR(123456789, 0.000001)
    raw_input()
    print "squareRoot(2736336100, 0.0001)"
    squareRootBi(2736336100, 0.0001)
    squareRootNR(2736336100, 0.0001)
    raw_input()
# as the problem gets more complex, the difference between good and bad methods get bigger

# compareMethods()

# Answers can be WRONG: when you get an answer from the computer, ask yourself: why do I believe it


### Non-scalar types: tuples, strings -> immutable
# mutable -> Lists

Techs = ['MIT', 'Cal Tech'] # points to a list (object)
Ivys = ['Harvard', 'Yale', 'Brown']
Univs = []

Univs.append(Techs)
Univs.append(Ivys) # method
# print Univs

# for e in Univs:
#     print e
#     for c in e: print c

# Flattening the list
Univs = Techs + Ivys  # concatenation
# print Univs

Ivys.remove('Harvard') # changed the original list

print Univs