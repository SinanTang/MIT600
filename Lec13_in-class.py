### Dynamic Programming, overlapping subproblems, optimal substructures

## Memoization, Table lookup
def fastFib(n, memo):
    global numCalls
    numCalls += 1
    # print('fib1 called with', n)
    if not n in memo:
        memo[n] = fastFib(n-1, memo) + fastFib(n-2, memo)
    return memo[n]

def fib1(n):
    memo = {0:1, 1:1}
    return fastFib(n, memo)

# numCalls = 0
# n = 6
# res = fib1(n)
# print('fib of', n, '=', res, 'numCalls =', numCalls)



## Optimal substructures - global optimal solution can be constituted from optimal solutions to sub-problems
  # not applicable to all problems

# Decision Tree

# visualisation of the knapsack problem
  # depth first, left first
  # back track strategy
  # O(2^n)

def maxVal(w, v, i, aW):
    """
    computes the maximal value in a knapsack problem
    :param w: list of weights of i items
    :param v: list of values of i items
    :param i: index of current item
    :param aW: available weight
    :return: maximal value
    """
    # print('maxVal called with:', i, aW)
    global numCalls
    numCalls += 1

    if i == 0:
        # looking at the last element now
        if w[i] <= aW: return v[i]
        else: return 0

    # the 'don' take' branch
    without_i = maxVal(w, v, i-1, aW)
    if w[i] > aW: return without_i
    else: with_i = v[i] + maxVal(w, v, i-1, aW - w[i]) # the right branch
    return max(with_i, without_i)

weights = [1, 5, 3, 4]
vals = [15, 10, 9, 5]
# numCalls = 0
# res = maxVal(weights, vals, len(vals)-1, 8)
# print('max Val =', res, 'number of calls =', numCalls)

# weights = [1, 1, 5, 5, 3, 3, 4, 4]
# vals = [15, 15, 10, 10, 9, 9, 5, 5]
# numCalls = 0
# res = maxVal(weights, vals, len(vals)-1, 8)
# print('max Val =', res, 'number of calls =', numCalls)

# exponential growth...

def fastMaxVal(w, v, i, aW, m):
    global numCalls
    numCalls += 1
    try: return m[(i, aW)]
    except KeyError:
        if i == 0:
            if w[i] <= aW:
                m[(i, aW)] = v[i]
                return v[i]
            else:
                m[(i, aW)] = 0
                return 0
        without_i = fastMaxVal(w, v, i-1, aW, m)
        if w[i] > aW:
            m[(i, aW)] = without_i
            return without_i
        else: with_i = v[i] + fastMaxVal(w, v, i-1, aW-w[i], m)
        res = max(with_i, without_i)
        m[(i, aW)] = res
        return res

def maxVal0(w, v, i, aW):
    m = {}
    return fastMaxVal(w, v, i, aW, m)

weights = [1, 1, 5, 5, 3, 3, 4, 4]
vals = [15, 15, 10, 10, 9, 9, 5, 5]
numCalls = 0
res = maxVal0(weights, vals, len(vals)-1, 8)
print('max Val =', res, 'number of calls =', numCalls)

## the number of calls reduce dramatically when number of elements increases
  ## as compared to the original solution
## magic of *dynamic programming*


## Lec14, more on Dynamic Programming (DP)

# 1. we trade time for space in DP
# 2. don't be intimidated by exponential problem
# 3. DP is broadly useful - when you see recursive structure, overlapping subproblem
# 4. the notion of problem reduction: can I transform this to a known problem?
