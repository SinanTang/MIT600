### Lec 9. Binary Search, Bubble and Selection Sorts

## Binary search - O(log) ##
 # take a sorted list
def bsearch(s, e, first, last, calls):
    print(first, last, calls)
    if (last - first) < 2: return s[first] == e or s[last] == e
    mid = first + (last - first)/2
    if s[mid] == e: return True
    if s[mid] > e: return bsearch(s, e, first, mid - 1, calls+1)
    return bsearch(s, e, mid + 1, last, calls + 1)


def search(s, e):
    print(bsearch(s, e, 0, len(s) - 1, 1))

s = range(1000)
# search(s, 1002) # cant use len() on int !

# generalise: - template to describe a log algorithm
    # 1. pick the midpoint
    # 2. check to see if this is answer
    # 3. if not, reduce to smaller problem and repeat
  # -> Divide and Conquer algrithm! binary search is the simplest DAC algrithm


 # unsorted list?
 # Should we sort before we search?

    # can we sort in sub-linear time (< linear time)? No!
    # can we sort in linear time? Probably no
    # How fast can we sort? -> n*logn time...

  # compare: 1. search unsorted list - linear search: n  -> in general, this is shorter
           # 2. sort + search: n*logn + logn
  # amotize the cost: k seaches of a list
           # 1. linear search: k*n
           # 2. sort + search: n*logn + k*logn -> this is gonna be better



## Selection sort ##

def selSort(L):
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        j = i + 1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j = j + 1
        temp = L[i]
        L[i] = L[minIndx]
        L[minIndx] = temp  # swapping
        print(L)

def testSelSort():
    test1 = [1,6,3,4,5,2]
    input('run selective test 1')
    selSort(test1)
    test2 = [6,1,2,3,4,5]
    input('run selective test 2')
    selSort(test2)
    test3 = [6,5,4,3,2,1]
    input('run selective test 3')
    selSort(test3)
    test4 = [1,2,3,4,5,6]
    input('run selective test 4')
    selSort(test4)

testSelSort()

# loop invariant (a property true of the structure every time through the loop)
  # list is split into a prefix and a suffix, prefix is sorted, suffix not

# complexity: O(n**2)



## Bubble Sort ##

# def bubbleSort(L):
#     for j in range(len(L)):
#         for i in range(len(L) - 1):
#             if L[i] > L[i+1]:
#                 temp = L[i]
#                 L[i] = L[i+1]
#                 L[i+1] = temp # swapping
#         print(L)
# every time, it moves the largest element to the end
# to improve, stop when there's no swap

def bubbleSort(L):
    swapped = True
    while swapped:
        swapped = False  # keeps track of
        for i in range(len(L) - 1):
            if L[i] > L[i+1]:
                temp = L[i]
                L[i] = L[i+1]
                L[i+1] = temp
                swapped = True
        print(L)

def testBubbleSort():
    test1 = [1,6,3,4,5,2]
    input('run bubble test 1')
    bubbleSort(test1)
    test2 = [6,1,2,3,4,5]
    input('run bubble test 2')
    bubbleSort(test2)
    test3 = [6,5,4,3,2,1]
    input('run bubble test 3')
    bubbleSort(test3)
    test4 = [1,2,3,4,5,6]
    input('run bubble test 4')
    bubbleSort(test4)

# testBubbleSort()

# complexity: O(n**2)


## which one is better: selection sort vs bubble sort ?
  # selection sort is better, judging from the number of swaps needed
    # selection sort swaps once in a scan, bubble sort swaps the max value one-by-one to the end in a scan

## Insertion sort ##
# O(n**2)
# better than selection sort and bubble sort
# one of the fastest algorithms for sorting very small arrays
