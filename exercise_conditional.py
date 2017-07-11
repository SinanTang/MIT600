# n = raw_input("Integer? ")
# n = int(n)
# if n < 0:
    # print "The absolute value of",n,"is",-n
# else:
    # print "The absolute value of",n,"is",n
    
# a = 0
# while a < 10:
    # a = a + 1
    # if a > 5:
        # print a,">",5
    # elif a <= 7:
        # print a,"<=",7
    # else:
        # print "Neither test was true"
      
      
# answer = 23
# question = 'What number am I thinking of?  '
# print 'Let\'s play the guessing game!'

# while True:
    # inp = raw_input(question)
    # try:
        # guess = int(inp)
    # except: #ValueError: not sure how this phrase works
        # print "Your guess should be a number"
    # else: #the else-clause will run if no exceptions occur, and won't run if exceptions occur.
        # if guess < answer:
            # print 'Little higher'
        # elif guess > answer:
            # print 'Little lower'
        # else: # guess == answer
            # print 'MINDREADER!!!'
            # break
        
        
#Asks for a number.
#Prints if it is even or odd

# print ("Input [x] for exit.")

# while True:
	# inp = raw_input("Tell me a number: ")
	# if inp == 'x':
		# break
	# # catch any resulting ValueError during the conversion to float
	# try:
		# number = float(inp)
	# except: #ValueError:
		# print 'I said: Tell me a NUMBER!'
	# else:
		# test = number % 2
		# if test == 0:
			# print int(number),"is even."
		# elif test == 1:
			# print int(number),"is odd."
		# else:
			# print number,"is very strange."
            
            
#Prints the average value.
 
# print "Welcome to the average calculator program"
# print "NOTE- THIS PROGRAM ONLY CALCULATES AVERAGES FOR 3 NUMBERS"
# x = int(raw_input("Please enter the first number "))
# y = int(raw_input("Please enter the second number "))
# z = int(raw_input("Please enter the third number "))
# str = x+y+z
# print float(str/3.0)


#keeps asking for numbers until count have been entered.
#Prints the average value.

# sum = 0.0

# print "This program will take several numbers, then average them."
# count = int(raw_input("How many numbers would you like to sum:  "))
# current_count = 0
 
# while current_count < count:
	# print "Number",current_count + 1
	# number = float(raw_input("Enter a number:  "))
	# sum = sum + number
	# current_count += 1
 
# print "The average was:",sum/count


#Continuously updates the average as new numbers are entered.

# print "Welcome to the Average Calculator, please insert a number"
# currentaverage = 0
# numofnums = 0
# while True:
    # newnumber = int(raw_input("New number "))
    # numofnums = numofnums + 1
    # currentaverage = round((((currentaverage * (numofnums - 1)) + newnumber) / numofnums), 3)
    # print "The current average is ", round(currentaverage, 3)
    
    
# IF exercise 1 a password guessing program

#pw = "1234"
# count = 0
# while True:
    # count = count + 1 # count += 1
    # inp = raw_input("Please enter your password: ")
    # if inp == pw: 
        # print "You have successfully logged in."
        # break
    # elif count <= 3:
        # print "Your have entered the wrong password. Please try again."
        # continue
    # else:
        # print "You have been denied access."
        # break
        
  #another example to prompt the user for the password      
# import time
# import getpass

# password = getpass.getpass("Please enter your password: ")

# print "Waiting for 3 seconds"
# time.sleep(3)
# got_it_right = False
# for number_of_tries in range(1,4):
    # reenter_password = getpass.getpass("Please reenter your password: ")
    # if password == reenter_password:
        # print "You are Logged in! Welcome User :)"
        # got_it_right = True
        # break

# if not got_it_right:
    # print "Access Denied!!"
    
        
#IF exercise 2 sum of 2 input numbers

# num1 = raw_input("Please enter the first number: ")
# num2 = raw_input("Please enter the second number:")

# try:
    # n1 = float(num1)
    # n2 = float(num2)
# except:
    # print "You didn'r enter numbers!"
    # exit()
# else:
    # if n1 + n2 > 100:
        # print "That is a big number!"
        # exit()
    # else: exit()
    
    
#IF exercise 3 asking for names
# myname = "Sinan"
# name = raw_input("Please enter your name: ")
# if name == myname:
    # print "That is a nice name."
# elif name == "John":
    # print "You have a cheesy name, John."
# elif name == "Michael":
    # print "I like your name."
# else:
    # print "You have a nice name."
# exit()


# number = int(raw_input("Enter a number to get its absolute value:"))
# res = (-number, number)[number > 0]
# print res

# number = int(raw_input("Enter a number to get its absolute value:"))
# res = (lambda: number, lambda: -number)[number < 0]()
# print res

# number = int(raw_input("Enter a number to get its absolute value:"))
# res = -number if number < 0 else number
# print res

##switch realised in Python
# x = 1
# def hello():
    # print "Hello"
# def bye():
    # print "Bye"
# def hola():
    # print "Spanish Hello"
# def adios():
    # print "Spanish Bye"
    
# menu = [hello, bye, hola, adios]
# menu[3]() # no Print here
# menu[x]()


# go = "y"
# x = 0
# def hello():
  # print "Hello"
# def bye():
  # print "Bye"
# def hola():
  # print "Hola is Spanish for Hello"
# def adios():
  # print "Adios is Spanish for Bye"

# menu = [hello, bye, hola, adios]
 
# while x < len(menu) :
    # print "function", menu[x].__name__, ", press " , "[" + str(x) + "]"
    # x += 1
    
# while go != "n":
    # c = int(raw_input("Select Function: "))
    # menu[c]()
    # go = raw_input("Try again? [y/n]: ")

# print "\nBye!"


## dont understand this bit
result = {
  'a': lambda x: x * 5,
  'b': lambda x: x + 7,
  'c': lambda x: x - 2
}[value](x)
