## the sum of the logarithms of all the primes less than n is less than n 
##and that as n grows, the ratio of this sum to n gets close to 1.

from math import*

count = 3
n = 0
s0 = log(2)+log(3)+log(5)
sum = 0

inp = raw_input("Please choose a order of a prime number: ")
n0 = int(inp)
if n0 == 1: print log(2), 2, log(2)/2
if n0 == 2: print log(2)+log(3), 3, (log(2)+log(3))/3
if n0 == 3: print log(2)+log(3)+log(5), 5, (log(2)+log(3)+log(5))/5

if n0 > 3:
    while count < n0:
        m = 2 
        n = n + 1
        oddnum = 2*n + 1 
        while m < n : 
            if m == n - 1 and oddnum%m != 0:
                count = count + 1
                sum = sum + log(oddnum)
            #print count, oddnum
                break
            elif m < (n-1) and oddnum%m != 0: 
                m = m + 1
                continue
            else: break
    
    print count, oddnum, sum

    totalsum = s0 + sum
    print totalsum, oddnum, totalsum/oddnum
    