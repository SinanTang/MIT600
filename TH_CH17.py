### Think Python2 ch.17 Classes and Methods

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
    def __str__(self):
        return '{:02d}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second)
    def print_time(self):
        print('{:02d}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second))
    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds
    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)
    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()
    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)
    def __radd__(self, other):
    # right-sided add
        return self.__add__(other)
    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

start = Time()
start.hour = 9
start.minute = 45
start.second = 00

# using function syntax, call print_time with dot notation
# Time.print_time(start)

# using method syntax, more common & concise
# start.print_time()
# print(start.time_to_int())

end = start.increment(1337)
# end.print_time()

# print(end.is_after(start))

# time = Time(6,33)
# time.print_time()


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return '({}, {})'.format(self.x, self.y)
    def __add__(self, other):
        if isinstance(other, Point):
            return self.add_point(other)
        else:
            return self.add_tuple(other)
    def __radd__(self, other):
        return self.__add__(other)
    def add_tuple(self, other):
        return Point(self.x + other[0], self.y + other[1])
    def add_point(self, other):
        return Point(self.x + other.x, self.y + other.y)


# p1 = Point(1,2)
# p2 = Point(2,4)
# print(p1+p2)
# p3 = (3,9)
# print(p3+p1)

start = Time(9, 45)
duration = Time(1, 35)
# print(start + duration)
# print(1337+start)


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else: d[c] += 1
    return d

# total = sum([start, duration, time])
# print(total)

# print(vars(start))

def print_attributes(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr))

# print_attributes(start)



## Exercise 17.1
# in Time2.py


## Exercise 17.2

class Kangaroo:
    # def __init__(self, name, contents = []):

## problem: the default value for contents!
## when __init__ is defined, [] gets evaluated and contents gets a reference to an empty list.
## after that, every kangaroo that gets the default value gets a reference to THE SAME List.

## in general, avoid using a mutable object as a default value.

    #     self.name = name
    #     self.pouch_contents = contents

    def __init__(self, name, contents=None):
        self.name = name
        if contents == None:
            contents = []
        self.pouch_contents = contents
    def put_in_pouch(self, other):
        self.pouch_contents.append(other)
        # print(self.pouch_contents)
    def __str__(self):
        # contents = ''
        # for i in self.pouch_contents:
        #     # print(i)
        #     contents += str(i)+' '
        # return str(self.name)+' has '+contents+'in its pouch!'
        t = [self.name+' has pouch contents:']
        for obj in self.pouch_contents:
            s = ' '+ object.__str__(obj)
            t.append(s)
        return '\n'.join(t)



kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')
kanga.put_in_pouch('money')
kanga.put_in_pouch('dollar')
kanga.put_in_pouch(roo)
roo.put_in_pouch('euro')

print(kanga)

print(roo)

