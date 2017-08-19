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

testBi()
