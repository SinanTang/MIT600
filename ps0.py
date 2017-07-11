Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 20:32:19) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> lname = raw_input("Enter your last name: ")
Enter your last name: Tang
>>> fname = raw_input("Enter your first name: ")
Enter your first name: Sinan
>>> print fname + "/n" + lname
Sinan/nTang
>>> print fname + /n + lname
SyntaxError: invalid syntax
>>> print fname /n lname
SyntaxError: invalid syntax
>>> print fname+" "+lname
Sinan Tang
>>> 
