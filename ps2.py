## Problem 1&2
#6*2 + 9*2 + 20*1 = 50   +6=56, +6*2=62, +6*3=68, +6*4=74    
#6*7 + 9*1 + 20+1 = 51   +6=57, +6*2=63,
#6*2 + 9*0 + 20*2 = 52   +6=58, +6*2=64
#6*4 + 9*1 + 20*1 = 53   +6=59, +6*2=65
#6*9 + 9*0 + 20*0 = 54   +6=60, +6*2=66
#6*1 + 9*1 + 20*2 = 55   +6=61, +6*2=67, +6*3=73,

## Problem 3

# bestSoFar = 1
# for n in range(50):
    # for c in range(3):
        # for b in range(6):
            # for a in range(9):
                # if 6*a + 9*b + 20*c == bestSoFar:
                    # print bestSoFar, "works."  ##will print everytime there's a workable combo; return only return once
                    # #print n
    # #return bestSoFar, "doesn't work." ## not working, return statement should be within function
    # bestSoFar += 1            
#print bestSoFar   
#print "Largest number of McNuggets that cannot be bought in exact quantity: %g", %bestSoFar


# candidate = 1
# counter = 0
# def test():
    # global counter
    # for c in range(3):
        # for b in range(6):
            # for a in range(9):
                # if 6*a+9*b+20*c == candidate:
                    # counter += 1 
                    # #print counter
                    # return str(candidate) + " works. Buy "+str(a)+" 6-piece boxes "+str(b)+" 9-piece boxes " + str(c)+" 20-piece boxes."
    # counter = 0
    # return str(candidate)+ " doesn't work."
    
# for i in range(50):
    # print test()
    # if counter == 6:
        # print "Largest number of McNuggets that cannot be bought in exact quantity: ", int(candidate)-6
    # candidate += 1

    
## Problem 4
bestSoFar = 1
packages = (6,9,20)
x = packages[0]
y = packages[1]
z = packages[2]
count = 0
def test2():
    global count
    for c in range(100):
        for b in range(100):
            for a in range(100):
                if x*a+y*b+z*c == bestSoFar:
                    count += 1
                    return str(bestSoFar)+" works. Buy "+str(a)+" "+str(x)+"-piece boxes, "+str(b)+" "+str(y)+"-piece boxes, "+str(c)+" "+str(z)+"-piece boxes."
    count = 0
    return str(bestSoFar)+" doesn't work."
    
for n in range(1, 200):
    print test2()
    if count == x:
        print "Given package sizes", x, y, z,", the largest number of MuNuggets that cannot be bought in exact quantity is:", int(bestSoFar)-int(x)
        break
    bestSoFar += 1




  
    
    