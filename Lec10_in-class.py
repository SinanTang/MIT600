### Divide-and-Conquer Methods, Merge Sort, Exceptions

## Divide-and-Conquer algorithm ##
 # 1. split the problem into several sub-problem of the same type
 # 2. solve them independently
 # 3. combine those solutions


## Mergesort ##

  # original idea: merge two sorted lists - O(n)

def merge(left, right):
    """Assumes left and right are sorted lists.
    Returns a new sorted list containing the same elements
    as (left + right) would contain."""
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    while i < len(left):
        result.append(left[i])
        i = i + 1
    while j < len(right):
        result.append(right[j])
        j = j + 1
    return result


  # take the method of Divide-and-Conquer,
    # 1. divide the list in half,
    # 2. continue until we have singleton lists
    # 3. merge the sublists

def mergesort(L):
    """Returns a new sorted list with the same elements as L"""
    print(L)
    if len(L) < 2:
       return L[:]
    else:
        middle = len(L) / 2
        left = mergesort(L[:middle])
        right = mergesort(L[middle:])
        together = merge(left,right)
        print('merged', together)
        return(together)

test = [1, 4, 3, 6, 5, 2, 8, 7]
# print(mergesort(test))

 # complexity: n*logn



## Hashing ##

 # e.g. collection of integers

def create(smallest, largest):
    intSet = []
    for i in range(smallest, largest+1): intSet.append(None)
    return intSet

def insert(intSet, e):
    intSet[e] = 1

def member(intSet, e):
    return intSet[e] == 1
 # complexity: constant, O(1)


 # e.g. collection of characters

def hashChar(c):
    # c is a char
    # function returns a different integer in the range 0-255
    # for each possible value of c
    return ord(c)

def cSetCreate():
    cSet = []
    for i in range(0, 255): cSet.append(None)
    return cSet

def cSetInsert(cSet, e):
    cSet[hashChar(e)] = 1

def cSetMember(cSet, e):
    return cSet[hashChar(e)] == 1
 # complexity: constant, constant time access

# Tradeoff of Constant Time Access: we traded space for time

# hard to create a good hash function
    # difficulty: even distribution (for complex input)



### Exceptions

# unhandled exceptions
# handled exceptions

  # e.g. try/except block
def readFloat(requestMsg, errorMsg):
    while True:
        val = input(requestMsg)
        try:
            val = float(val)
            return val
        except:
            print(errorMsg)

# print(readFloat('Enter float: ', 'Not a float.'))

# a polymorphic example (function allows variables of different types at different times)

def readVal(valType, requestMsg, errorMsg):
    while True:
        val = input(requestMsg)
        try:
            val = valType(val)
            return val
        except:
            print(errorMsg)

print(readVal(int, 'Enter int: ', 'Not an int.'))
     # in terms of this integer check, float can pass thro too...

# Standard way of 'give me the input'
# have it in a separate input.py, and import it into every file
 # which needs this procedure


def getGrades(fname):
    try:
        gradesFile = open(fname, 'r')
    except IOError:  # expect this error
        print('Could not open', fname)
        raise 'GetGradesError'  # otherwise, raise this for any other errors
    grades = []
    for line in gradesFile: grades.append(float(line))
    return grades

try:
    grades = getGrades('xx.txt')
    grades.sort()
    median = grades[len(grades)/2]
    print('Median grade is', median)
except 'GetGradesError':
    print('Whoops')


## Exception VS assert?
 # assert: user input must satisfy some pre-conditions, only then the function will go through the post-condition
     # assert statement allows debugging at testing time, message for the user
 # exception: user can input anything, exceptions try to handle unexpected issues themselves

# why use exceptions?
  # easy debugging: to easily identify where a bug is coming from
  # discipline coding


# Coercion: implicit conversion of data type
# Casting: explict...
