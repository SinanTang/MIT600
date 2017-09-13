# 1. what' the computational complexity of fact0?
def fact0(i):
    assert type(i) == int and i >= 0
    if i == 0 or i == 1:
        return 1
    return i*fact0(i-1)

# fact0() calculates the n! of i.
# O(N) because each recursive call adds one more step to the computation


# 2. what' the computational complexity of fact1?
def fact1(i):
    assert type(i) == int and i >= 0
    res = 1
    while i > 1:
        res = res * i
        i -= 1
    return res

# O(N), each loop adds constant steps, N loops for i == N


# 3. what' the computational complexity of makeSet?
def makeSet(s):
    assert type(s) == str
    res = ''
    for c in s:
        if not c in res:
            res = res + c
    return res

# O(N), concatenates all the unique letters in s into a string


# 4. what' the computational complexity of intersect?
def intersect(s1, s2):
    assert type(s1) == str and type(s2) == str
    s1 = makeSet(s1)
    s2 = makeSet(s2)
    res = ''
    for e in s1:
        if e in s2:
            res = res + e
    return res

# O(N). makeSet() is linear, the length of s1/s2 is maximally 26, res is maximally 26 too


# 5. present a hand stimulation of the code below. Describe the value to which each identifier is bound after each step of the computation.
  # note that 's1'and 's2' exist in more than one scope.

def swap0(s1, s2):
    # assert type(s1) == list and type(s2) == list
    tmp = s1[:]
    # print(s1, s2, tmp)
    s1 = s2[:]
    # print(s1, s2, tmp)
    s2 = tmp
    # s2.append(5)
    # print(s1, s2, tmp)
    return
    # return s1, s2

s1 = [1]
s2 = [2]
# print(swap0(s1, s2))
swap0(s1, s2)
# s1, s2 = swap0(s1, s2)
print(s1, s2)

# before swap0(): s1, s2 = [1], [2]
# at the end of swap0(): s1, s2 = [2], [1]
# out of the scope of swap0(): s1, s2 = [1], [2]

# the global s1/s2 are not altered by the local s1/s2, change the parameters into s0/s00 makes it clearer


# 6. present a hand stimulation of the following code:

def swap1(s1, s2):
    assert type(s1) == list and type(s2) == list
    return s2, s1

# s1, s2 = swap1(s1,s2)
# swap1(s1,s2)
# print(s1, s2)

# before swap1(): s1, s2 = [1], [2]
# at the end of swap1(): s1, s2 = [2], [1]
# out of swap1(): s1, s2 = [2], [1]

# the global value of s1/s2 is changed as a result of the assignment operation


# 7. present a hand stimulation of the following code:

def rev(s):
    # assert type(s) == list

    for i in range(len(s)//2):
        tmp = s[i]
        s[i] = s[-(i+1)]
        s[-(i+1)] = tmp
    # print(s)

ss = [1, 2, 3, 4]
rev(ss)
print(ss)

# before rev(): s = [1,2,3]
# at the end of rev(): s = [3,2,1]

## global vs local ?
# in #7 the parameter s is altered inside the function, and the global s is changed too

## #7 vs #5
#5 creates local variable with the same name as s1/s2
#7 directly modifies the global variable s