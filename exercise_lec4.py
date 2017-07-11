# farmyard problem

##================ my version
#x = 20 #heads
#y = 56 #legs

# def farm(x, y):
    # a = 0 #pigs
    # while a <= x:
        # if not a*4 + 2*(x-a) == y:
            # a = a + 1
            # #return None
        # else:
            # return a
# print "There are",farm(20,56),"pigs, and", 20 - farm(20,56),"chickens in the farm!"

#=============== Prof's solution
# def solve(numLegs, numHeads):
	# for numChicks in range(0, numHeads+1):
		# numPigs = numHeads - numChicks
		# totLegs = 4*numPigs + 2*numChicks
		# if totLegs == numLegs:
			# return (numPigs, numChicks)  # tule or list, seems like same outputs...
# #in *almost* all the places where you can use tuples, you can use lists. But there are some situations where only tuples are expected.
# #tuples: immutable; lists: mutable           
	# return (None, None)

# def barnYard():
	# heads = int(raw_input("Enter number of heads: "))
	# legs = int(raw_input("Enter number of legs: "))
	# pigs, chickens = solve(legs, heads)
	# if pigs == None:
		# print "There is no solution."
	# else:
		# print "Number of pigs:", pigs
		# print "Number of chickens:", chickens
        
# barnYard()

# + spiders
# def solve2(numLegs, numHeads):
    # for numChicks in range(0, numHeads+1):
        # for numPigs in range(0, numHeads - numChicks +1):
            # numSpiders = numHeads - numChicks - numPigs
            # totLegs = 4*numPigs + 2*numChicks + 8*numSpiders
            # if totLegs == numLegs:
                # return (numPigs, numChicks, numSpiders)      
    # return (None, None, None)

# def barnYard2():
	# heads = int(raw_input("Enter number of heads: "))
	# legs = int(raw_input("Enter number of legs: "))
	# pigs, chickens, spiders = solve2(legs, heads)
	# if pigs == None:
		# print "There is no solution."
	# else:
		# print "Number of pigs:", pigs
		# print "Number of chickens:", chickens
        # print "Number of spiders:", spiders        
# barnYard2()

# Capturing all the solutions
# def solve3(numLegs, numHeads):
    # solutionFound = False
    # for numSpiders in range(0, numHeads + 1):
        # for numChicks in range(0, numHeads - numSpiders + 1):
            # numPigs = numHeads - numChicks - numSpiders
            # totLegs = 4*numPigs + 2*numChicks + 8*numSpiders
            # if totLegs == numLegs:
                # print "Number of pigs: " + str(numPigs) + ",",
                # print "Number of chickens: " + str(numChicks)+ ",",
                # print "Number of spiders:", numSpiders
                # solutionFound = True
    # if not solutionFound: print "There is no solution."
    

# the Palindrome problem
#======================my version
# r 1a 2c 3e 4c 5a 6r, len = 7
# def isPalindrome(word):
    # ans = False
    # while len(word) >= 0:
        # if len(word) == 1 or len(word) == 0:
            # ans = True
            # return "Input is a palindrome!"
        # elif word[0] == word[len(word) - 1]:
            # word = word[1:len(word)-1]
        # else: return "Input is not a palindrome..."
        
# print isPalindrome("raceecar")

#=================Prof's version
# def isPalindrome(s):
    # """returns True if s is a palindrome and False otherwise"""
    # if len(s) <= 1: return True
    # else: return s[0] == s[-1] and isPalindrome(s[1:-1])

## to see how the recursion is done***
def isPalindrome1(s, indent):
    print indent, "isPalindrome1 called with", s
    if len(s) <= 1:
        print indent, "About to return True from base cases"
        return True
    else:
        ans = s[0] == s[-1] and isPalindrome1(s[1:-1], indent+indent)
        print indent, "About to return", ans
        return ans
#isPalindrome1("abcddcba","  ")

## Fibonacci numbers
def fib(x):
    """return fibnacci of x, where x is a non-negative int"""
    if x == 0 or x == 1: return 1
    else: return fib(x-1) + fib(x-2)
print fib(10)


