### Lec 8: Complexity: log, linear, quadratic, exponential algorithms

## Doing exponentiation: example 1

def exp1(a,b):
    ans = 1
    while (b>0):  # step 1: comparison
        ans *= a  # step 2: multiplication
        b -= 1    # step 3: subtraction
    return ans    # loop count: b times
# in total: (2+3*b) steps -> but in the end, b is the one really matters
    ## O(b) linear

### the focus: Rate of Growth as size of the problem grows. aka asymptotic notation
### Big O notation (describes the limiting behaviour of a function when the argument
    # tends towards a certain value or infinity. )
    # -- upper limit of growth of function as input gets large
    # e.g. f(x) ∈ O(n**2)


## Doing exponentiation: example 2, recursive exponentiator

def exp2(a, b):
    if b == 1: return a
    else: return a*exp2(a, b-1)

# number of steps: f(b) = 3+f(b-1) ..= 3*k+f(b-k)  -> a recurrence relation
# finish point: (b-k) = 1 -> k = b-1
# so: 3*k + f(b-k) = 3*(b-1) + f(1) = 3*b - 3 + 2 = 3*b - 1 -> O(b) linear -> [adds a constant]


## Doing exponentiation: example 3

def exp3(a, b):
    if b == 1:
        return a
    if (b%2)*2 == b:
        return exp3(a*a, b/2)     # the even case
    else: return a*exp3(a, b-1)   # the odd case

# number of steps:
 # b is even: f(b) = 6 + f(b/2)
 # b is odd:  f(b) = 6 + f(b-1) = 6 + 6 + f((b-1)/2)
 # to generalise: f(b) = 12 + f(b/2)
                    #  = 12 +12 + f(b/4) = 12*k + f(b/(2**k))
 # finish point: b/(2**k) = 1 -> k = log2(b) ->> O(log(b))  logrithmic -> [cut in half/third]


## example 4

def g(n, m):
    x = 0
    for i in range(n):
        for j in range(m):
            x += 1
    return x

# order of complexity: O(n*m)
 # if n == m -> O(n**2) quadratic -> [double-nested loop]


## example 5 : Tower of Hanoi 汉诺塔

def Towers(size,fromStack,toStack,spareStack):
    if size == 1:
        print 'Move disk from ',fromStack, 'to ',toStack
    else:
        Towers(size-1,fromStack,spareStack,toStack)
        Towers(1,fromStack,toStack,spareStack)
        Towers(size-1,spareStack,toStack,fromStack)

# order of complexity:
 # f(n) = 1 + f(1) + 2*f(n-1) = 3 + 2*f(n-1)
                            # = 3 + 2*3 + 4*f(n-2)
                            # = 3*(1+2+4+...+2**(k-1)) + 2**k(n-k)
 # finish point: n-k = 1
# O(2**n) exponential -> [reduce problem of one size into two or more sub-problem of a smaller size]



## Search algorithms

## example 1: search a sorted list

def search(s, e):
    answer = None
    i = 0
    numCompares = 0
    while i < len(s) and answer == None:
        numCompares += 1
        if e == s[i]:
            answer = True
        elif e < s[i]:
            answer = False
        i += 1
    print(answer, numCompares)

# order of complexity: linear (measuring the worst case)

def bisearch(s, e, first, last):
    print(first, last)
    if (last - first) < 2:
        return s[first] == e or s[last] == e
        # primitive operations here are constant time
        # access time in lists is constant (random access model - as long as the location is known,
        # it takes a constant amount of time to get to that point)
    mid = first + (last - first)/2
    if s[mid] == e: return True
    if s[mid] > e: return bisearch(s, e, first, mid - 1)
    return bisearch(s, e, mid + 1, last)

def search1(s, e):
   print(bisearch(s, e, 0, len(s) - 1))
   print('Search complete')

# order of complexity: logrithmic

# be careful about whats the primitive step


## Summary: recognize different classes of algorithms and the features to identify them
 # so you can map your problem into those ranges



