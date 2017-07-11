# x = raw_input("What is your name? ")
# print "Your name is " + x

# x = input("What are the first 10 perfect squares? ")
# # user input: map(lambda x: x*x, range(10)) # map(function, iterable,...), returns a list of  the result
# print x 

# x = None
# while not x:
    # try:
        # x = int(raw_input("Enter a number: "))
    # except ValueError:
        # print "Invalid number!"
        

#f = file("words.txt", "r")

# f = open("words.txt", "r")
# for line in f:
    # print line[0]
# f.close()

# with open("words.txt", "r") as txt:
    # for line in txt:
        # print line
#advantage: no need to close the file

# c = f.read(1)
# while len(c) > 0:
    # if len(c.strip()) > 0: print c,
    # c = f.read(1)
    
# f.seek(0)  # move the marker back to the beginning of the file 


#import sys
# for line in sys.stdin.read():
    # print line,  # print the user input after Ctrl+Z then 'enter'...

# for arg in sys.argv[1:]:
    # print arg, #the current script file has to have contents to be printed out
    
# option_f = False
# option_p = False
# option_p_argument = ""
# i = 1
# while i < len(sys.argv):
  # if sys.argv[i] == "-f":
    # option_f = True
    # sys.argv.pop(i)
  # elif sys.argv[i] == "-p":
    # option_p = True
    # sys.argv.pop(i)
    # option_p_argument = sys.argv.pop(i)
  # else:
    # i += 1
#not sure what are these codes for    
    
# import sys
# print 1,2,0xff,0777,(10+5j),-0.999,map,sys
# '0x' -> to denote the beginning of a hexadecimal number. ff(hexa) = 255 

# for i in range(10):
    # print i,
# #print   #adding a newline here
# for i in range(10,20):
    # print i,

# print >> f, "Hello, world!"

# import sys
# print str(1)+str(2)+str(0xff)+str(0777)+str(10+5j)+str(-0.999)+str(map)+str(sys)
# #to avoid spaces 
# #NameError: name 'sys' not defined? -> need to import sys first

# import sys
# write = sys.stdout.write
# write("20")
# write("05\n")
# the write function to avoid spaces

#print "Hello"+3 # TypeError

# import sys
# sys.stdout.write("Hello")  # printing without a newline
# sys.stdout.flush() #in order to display immediately on the user's screen
# sys.stdout.write("Sinan\n")


#short example for buffer & flush()
# import time
# import sys
# for i in range(6):
    # sys.stdout.write("%d"%i)
    # #sys.stdout.flush()
    # time.sleep(1)

    
# print >> sys.stderr, "An error occurred."  #prints to stderr stream
# sys.stderr.write("Hello\n") #prints to stderr stream


# sum = 2+3; print "The sum: %i" %sum

# formatted_string = "The sum: %i" %(2+4); print formatted_string

# print "Float: %8.3f" % 1.23456789 #The number 3 after the period specifies the number of decimal digits after the period to be displayed; 6 before the period specifies the total number of characters the displayed number should take, to be padded with spaces if needed.

# print "%s is %i years old." %("Sinan", 24) # passes 2 arguments

# from __future__ import print_function
# print ("Hello","world")
# print ("Hello world", end="") #without the ending newline
# print ("Hello", "world", sep="-") #separated with a dash


# file1 = open("words.txt", "w") # overwriting
# file1 = open("words.txt", "a") # appending
# for i in range(1,20+1):
    # print >>file1, i  # ">>file" sends the output to a file rather than stdout
# file1.close()    


# file1 = open("words.txt", "w")
# for i in range(1,10+1):
    # if i>1:
        # file1.write("-") #numbers separated with a dash
    # file1.write(str(i))
# file1.close()
#will eliminate all the existing contents first, then overwrite...


