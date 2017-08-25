## Ch.7 Strings
# fruit = 'pineapple'
# letter = fruit[2]
# print letter
# i = 1
# print fruit[i],fruit[i+3]
# print len(fruit)
# last = fruit[len(fruit)-1]
# print last
# print fruit[-2] #, fruit[-10] out of range 

# index = len(fruit) - 1
# while index < len(fruit) and index >= 0:
    # letter = fruit[index]
    # print letter,
    # index = index - 1 #backward output
    
# for i in fruit:
    # print i, 
    
# prefixes = 'JKLMNOPQ'
# suffix = 'ack'

# for letter in prefixes:
    # if letter == 'O' or letter == 'Q':
        # print letter + 'u' + suffix
    # else:
        # print letter + suffix 

##slicing        
# fruit = 'pineapple'
# print fruit[0:4], fruit[:4],fruit[4:], fruit[:]

##string comparison
# word = raw_input('Which fruit do you want?')
# word = word.lower() # b/c all uppercase letters come before all the lowercase letters
# if word < 'banana':
    # print 'Your fruit, ' + word + ', comes before banana.'
# elif word > 'banana':
    # print 'Your fruit, ' + word + ', comes after banana.'
# else:
    # print 'Oh, we\'ve got no bananas.' 
    
##strings are immutable
# greet = "Hello, Sinan!"
# newGreet = greet[:7] + "Lynn!"
# print newGreet

# def find(str, ch, p): #p = where it should start looking
    # index = p
    # while index < len(str):
        # if str[index] == ch:
            # return index
        # index = index + 1
    # return -1

# fruit = 'pineapple'
# print find(fruit, 'p', 2)

# def countLetters(str, l):
    # count = 0
    # for char in str:
        # if char == l:
            # count = count + 1
    # return count 

# fruit = 'pineapple'        
# print countLetters(fruit, 'p')

# #count the number of a letter in a string from a given position
# def countLetters(str, l, p):
    # count = 0
    # index = p
    # while index < len(str):
        # if str[index] == l:
            # count = count + 1
        # index = index + 1
    # return count
    
# fruit = 'pineapple'        
# print countLetters(fruit, 'e', 2)
    
# import string
# fruit = 'pineapple'
# index = string.find(fruit, 'p', 2, 4)
# print index 

# print string.lowercase #constants
# print string.uppercase
# print string.digits

#print string.find(string.lowercase, 'z')    

# def isLower(ch):
    # return string.find(string.lowercase, ch) != -1 
    
# def isLower(ch):
        # return ch in string.lowercase

# def isLower(ch):
    # return 'a' <= ch <= 'z'

# print isLower('Yz')    
    
# print string.whitespace   

# print fruit.find('p', 2, 8)
    
# print 'b' in 'apple'   

# def in_both(w1, w2):
    # for letter in w1:
        # if letter in w2:
            # print letter
            
# in_both("sinantang", "stephanschur") #will print common letters which appear multiple times in w1

#Exercises Think Python Ch 8
#8.2
# a = "banana"
# print a.count('a')

#8.3 one-line version of is_palindrome...
# word = raw_input("enter a word: ")
# if word == word[::-1]: print True
# else: print False

#8.4 a function to check whether a string contains any lowercase letters. which are wrong?
# def any_lowercase1(s):
    # for c in s:
        # if c.islower():
            # return True
        # else:
            # return False 

# # print any_lowercase1("absx") # incorrect, to check if all the letters are lowercase
            
# def any_lowercase2(s):
    # for c in s:
        # if 'c'.islower():
            # return 'True'
        # else:
            # return 'False'

# # print any_lowercase2("ABC") # incorrect, forever true..           
            
# def any_lowercase3(s):
    # for c in s:
        # flag = c.islower()
    # return flag

# print any_lowercase3("AbdD") # incorrect, forever testing the final letter
    
# def any_lowercase4(s):
    # flag = False
    # for c in s:
        # flag = flag or c.islower() ##??
    # return flag

# print any_lowercase4("abbb") #CORRECT! 
    
# def any_lowercase5(s):
    # for c in s:
        # if not c.islower():
            # return False 
    # return True 

# print any_lowercase5("aBc") # incorrect, texting if all the letters are lowercase

#8.5 a Caesar cypher
# def rotate_word(s, i):
    # for letter in s:
        # newLetter = chr(int(ord(letter) + i)) 
        # s = s.replace(letter, newLetter)
    # print s

# rotate_word("IbM", -1)    



# string methods - return a titlecased version of a string, following linguistic rules
import re
def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?", lambda mo: mo.group(0)[0].upper() + mo.group(0)[1:].lower(), s)
print titlecase("they're not friend's at all.")
    
    

    