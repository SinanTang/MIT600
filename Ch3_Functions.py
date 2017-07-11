#Exercise 3.1
# def right_justify(s):
#     print " "*(70 - len(s))+str(s)
#
# right_justify("monty")

#Exercise 3.2
def do_twice(f):
    f()
    f()
# def print_spam():
#     print "spam"
def print_twice(bruce):
    print bruce
    print bruce

#do_twice(print_twice, "spam")

def do_four(f):
    do_twice(f)
    do_twice(f)
#do_four(print_twice,"span")

#Exercise 3.3.1
def draw_row1():
    print "+",("-"+" ")*3+"-",
def draw_row2():
    print "+",("-"+" ")*3+"-","+",
def draw_row():
    draw_row1()
    draw_row2()
    print

def draw_col1():
    print "|"," "*7,"|"," "*7,"|"
def draw_col2():
    print "|"," "*7,"|"," "*7,
def draw_col():
    do_four(draw_col1)

def draw_grid():
    draw_row()
    draw_col()
    draw_row()
    draw_col()
    draw_row1()
    draw_row2()
#draw_grid()

# Exercise 3.3.2
def do_three(f):
    f()
    f()
    f()
def draw_row4():
    do_three(draw_row1)
    draw_row2()
    print

def draw_col5():
    draw_col2()
    draw_col1()

def draw_grid2():
    draw_row4()
    do_four(draw_col5)
def draw_biggrid():
    do_four(draw_grid2)
    draw_row4()

#draw_biggrid()

print 
# another solution for 4*4 grid
def one_four_one(f, g, h):
    f()
    do_four(g)
    h()
def print_plus():
    print "+",
def print_dash():
    print "-",
def print_bar():
    print "|",
def print_space():
    print " ",
def print_end():
    print
def nothing():
    "do nothing"

def print1beam():
    one_four_one(nothing, print_dash, print_plus)
def print1post():
    one_four_one(nothing, print_space, print_bar)
def print4beams():
    one_four_one(print_plus, print1beam, print_end)
def print4posts():
    one_four_one(print_bar, print1post, print_end)
def print_row():
    one_four_one(nothing, print4posts, print4beams)

def print_grid():
    one_four_one(print4beams, print_row, nothing)

#print_grid()

line1= "sinan "
line2= "tang"


def cat_twice(part1, part2):
    cat = part1+part2
    print_twice(cat)
#cat_twice(line1, line2)
#print_twice(cat)  # throws NameError
