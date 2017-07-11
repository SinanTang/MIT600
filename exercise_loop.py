# a = 0
# while a < 5:
    # a += 1 #same as a=a+1
    # #print a
# print a 


# a = 1
# s = 0
# print 'Enter Numbers to add to the sum.'
# print 'Enter 0 to quit.'
# while a != 0:
    # print 'Current Sum: ', s
    # a = float(raw_input('Number? '))
    # s += a
# print 'Total Sum = ',s


# while 1 == 1:
    # print "Help, I'm stuck in a loop." #terminate the loop with "Ctrl + C"
    

#This program calculates the Fibonacci sequence
# a = 0
# b = 1
# count = 0
# max_count = 20
# while count < max_count:
    # count = count + 1
    # #we need to keep track of 'a' since we change it
    # old_a = a
    # old_b = b
    # a = old_b
    # b = old_a + old_b
    # print (old_a), #Notice that the ',' at the end of a print statement keeps it from switching to a new line
 
 
#password.py    
# password = "foobar"
# while password != "unicorn":
    # password = raw_input("Password: ")
# print ("Welcome in")


#FOR loop
# onetoten = range(1,11)
# for count in onetoten:
    # print count

    
# demolist = ['life',42, 'the universe', 6,'and',7,'everything']
# for item in demolist:
    # print "The Current item is: %s" % item
    
    
# list = [2,4,6,8]
# sum = 0
# for num in list:
    # sum = sum + num
# print "The sum is: %s" %sum


##find the duplicate in a list using FOR loop
# list = [4, 5, 7, 8, 9, 1, 0, 7, 10]
# list.sort()
# #print "\tl:", list
# prev = list[0]
# #print prev
# del list[0] #delete the first item so it is not incorrectly thought to be a duplicate
# #print list
# for item in list:
    # if prev == item:
        # print "Duplicate of ",prev," Found"
    # prev = item
    # #print prev
    
    
##using FOR loop to do something a certain number of time
#the first 9 numbers of the Fibonacci series
# a = 0
# b = 1
# for c in range(1,10):
    # print a
    # n = a + b
    # a = b
    # b = n
# print "" #??


#Exercise 2  number guessing game
# print "Welcome to the number guesser! Please pick up a number between 1 to 100."
# #s = 100
# n1 = 50
# #n = 0
# for i in range(2,9):
    # print "This is Guess No.",i-1
    # print "Is your number ", n1, "?"
    # line = "If my guess is correct, press [e]; \nIf your number is higher, press [h]; \nIf your number is lower, press [l]."
    # ans = raw_input(line)
    # if ans == "e": 
        # print "I guess your number is ", n1
        # break
    # elif ans == "h":
        # n1 = n1 + 100/(2**i)  ##here stops at 97, couldn't go bigger
        
    # else:
        # n1 = n1 - 100/(2**i)  ##here stops at 3, couldn't go smaller
    
# print "Game finished!"



##solution
print "\nIn your head, pick a number between 1 and 100, \ni'll guess it with some hints:\n"
letsstart = raw_input("ready? input anything...\n")
uppers = 100
lowers = 0
guess = 50
boom = 0
for c in range(1,10):
	if boom == 0:
		print "guess: ",guess
		answer = raw_input("Was that\na. too low\nb. too high\nc.  thats right!\n")
		if answer == "c":
			print "I got it!  Thanks for playing.\n"
			boom = 1
		elif answer == "a":
			lowers = guess
			blah = int((uppers-guess)/2)
			guess = guess + blah
		elif answer == "b":
			uppers = guess
			blash = int((guess-lowers)/2)
			guess = guess-blash