count = 3
n = 0
#m = 2

inp = int(raw_input("Which prime number do you want to know?" ))

while count < inp:
    m = 2 
    n = n + 1
    oddnum = 2*n + 1 # all the odd integers
    
    while m < n : # try each oddnum to see if it is a prime number
        #m = m + 1 #too early here!
        if m == n - 1 and oddnum%m != 0:
            count = count + 1
            #print count, oddnum
            break #
        elif m < (n-1) and oddnum%m != 0: #remainder = 0, move to the next
            m = m + 1
            continue
        else: break
    #if count == 10: break
    
print count, oddnum
    