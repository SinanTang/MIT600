## using bisection to approximate the square root of input number
def squareRootBi(x, epsilon):
    """
    :param x: number to be squared
    :param epsilon: the precision the square root expects to be
    :return: the approximate square root of input x
    """
    assert x >= 0, "x must be non-negative, not " + str(x)
    assert epsilon > 0, "epsilon must be positive, not " + str(epsilon)
    # ? the bug: when there's a perfect square, the function doesn't give the integer.
    for i in range(x):
        if i**2 == x:
            return i
        else: pass

    low = 0
    high = x
    guess = (low + high)/2.0
    count = 1
    while abs(guess**2 - x) > epsilon and count <= 100:
        print "High: ", high, ", Low: ", low, ", Guess: ", guess
        if guess**2 < x:
            low = guess
        # elif guess**2 == x:  ## doesnt give precise result either
        #     return guess
        else:
            high = guess
        guess = (low + high)/2.0
        count += 1
    assert count <= 100, "Iteration count exceeded"
    print "Bi method. Num iteration: ", count, "Estimate: ", guess
    return guess

print squareRootBi(16, 0.0001), "\n", squareRootBi(15, 0.0001)
