##find the square root of a perfect square
# script 1
# x = 16
# ans = 0
# while ans*ans <= x: # bug here
	# ans = ans + 1
# print ans

# script 2
# inp = raw_input("Please enter a perfect square: ")
# x = int(inp)
# ans = 0
# if x >= 0:
	# while ans*ans < x:
		# ans = ans + 1
		# print "ans = ",ans
	# if ans*ans != x:
		# print x, " is not a perfect square"
	# else: print ans
# else: print x, " is a negative number"


## exhaustive enumeration
# x = 10
# i = 1
# while i<x:
	# if x%i == 0:
		# print "divisor ",i
	# i = i + 1

#FOR loop
# x = 10
# for i in range(1, x):
	# if x%i == 0:
		# print "divisor ",i
        
#collecting elements with tuple in FOR loop
# x = 100
# divisors = ()
# for i in range(1, x):
	# if x%i == 0:
		# divisors = divisors + (i,) #converting int into tuple
# print divisors

sumDigits = 0
for c in str(1952):
	sumDigits += int(c)
print sumDigits


