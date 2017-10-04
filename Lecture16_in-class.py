### Lec16. Encapsulation, Inheritance, Shadowing

# class - template for data type
     #  - cluster data & method - modularity/abstraction
     #  - data hiding (a version of encapsulation) - only access parts through a method
         # python doesnt enforce
     #  - class is used for instances - attributes

# OOP good for modelling a set of units which are associated to one another

from functools import total_ordering

@total_ordering
class Person(object):
## inherits from the base object in Python
# the hierachy
    def __init__(self, family_name, first_name):
        self.family_name = family_name
        self.first_name = first_name
    def familyName(self):
        return self.family_name
    def firstName(self):
        return self.first_name
    # def __cmp__(self, other):
    #     return cmp((self.family_name, self.first_name),
    #                (other.family_name, other.first_name))
    def __eq__(self, other):
        return (self.family_name == other.family_name) and (self.first_name == other.first_name)
    def __lt__(self, other):
        return self.first_name < other.first_name and self.family_name < other.family_name
    def __str__(self):
        return '<Person: {} {}>'.format(self.first_name, self.family_name)
    def say(self, toWhom, something):
        return self.first_name + ' ' + self.family_name + ' says to ' + toWhom.firstName() + ' ' + \
         toWhom.familyName() + ': ' + something
    # standard practice: when refering to itself, can just access the values;
    # when calling other objects, use method (send the message)
    # (but either way produces the same result)
    def sing(self, toWhom, something):
        # a method using another method -> nice modularity
        return self.say(toWhom, something + ' tra la la')

per = Person('tang', 'sinan')
# print(per.familyName()) # method
# print(per.family_name)  # field
#
# print(per.say(per, 'you\'re great!'))
# print(per.sing(per, 'you\'re great!'))


@total_ordering
class MITPerson(Person):
## inherit from Person class
    # a local variable
    nextIdNum = 0
    def __init__(self, family_name, first_name):
        # example of inheritance
        # using first_name/family_name or firstName/familyName has same effect
        Person.__init__(self, family_name, first_name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1
    def getIdNum(self):
        return self.idNum
    def __str__(self):
        return '<MIT Person: {} {}>'.format(self.family_name, self.first_name)
    def __eq__(self, other):
        return self.idNum == other.idNum
    def __lt__(self, other):
        return self.idNum < other.idNum


p1 = MITPerson('Tang', 'Sinan')
p2 = MITPerson('Schur', 'Sinan')
# p1.familyName() = p1.family_name

# goes up to the parent/super class
print(p1.say(p2, 'i love you'))

# print(p1.getIdNum())
# print(p2.getIdNum())
# print(p1==p2, p1<p2)


class UG(MITPerson):
    def __init__(self, familyName, firstName):
        MITPerson.__init__(self, familyName, firstName)
        self.year = None
    def setYear(self, year):
        if year > 5: raise OverflowError('Too many')
        self.year = year
    def getYear(self):
        return self.year
    def say(self, toWhom, something):
        return MITPerson.say(self, toWhom, 'Excuse me, but ' + something)
        ## Shadowing - overriding


me = Person('Grim', 'Eric')
ug = UG('Mann', 'Kevin')

# print(ug, me)
# print(ug.say(me, 'I did not finish the homework...'))
# print(ug.firstName(), ug.first_name)

# print(ug > per)
# AttributeError

# print(per == ug)
# seems like this works in Python2 but not in Python3


class Prof(MITPerson):
    def __init__(self, familyName, firstName, rank):
        MITPerson.__init__(self, familyName, firstName)
        self.rank = rank
        self.teaching = {}
    def addTeaching(self, term, subj):
        try:
            self.teaching[term].append(subj)
        except KeyError:
            self.teaching[term] = [subj]
    def getTeaching(self,term):
        try:
            return self.teaching[term]
        except KeyError:
            return None
    def lecture(self, toWhom, something):
        return self.say(toWhom, something+'as it is obvious')
    def say(self, toWhom, something):
        if type(toWhom) == UG:
            return MITPerson.say(self, toWhom, 'I do not understand why you say '+ something)
        elif type(toWhom) == Prof:
            return MITPerson.say(self, toWhom, 'I really liked your paper on '+ something)
        else:
            return self.lecture(something)

me = Prof('Grim', 'Eric', 'Full')
me.addTeaching('F08','6.00')
me.addTeaching('S09','6.00')
me.addTeaching('S09','6.XX')

# print(me.getTeaching('F08'))
# print(me.getTeaching('S09'))
# print(me.getTeaching('S08'))
# print(me.teaching)


class Faculty(object):
    def __init__(self):
        self.names = []
        self.IDs = []
        self.members = []
        self.place = None
    def add(self, who):
        if type(who) != Prof: raise TypeError('not a professor')
        if who.getIdNum() in self.IDs: raise ValueError('duplicate ID')
        self.names.append(who.familyName())
        self.IDs.append(who.getIdNum())
        self.members.append(who)
    # Creating iterators
    def __iter__(self):
        self.place = 0
        return self
    def __next__(self):
    # in Python2, def next(self)
        if self.place >= len(self.names):
            raise StopIteration
        self.place += 1
        return self.members[self.place-1]


grimson = Prof('Grimson', 'Eric', 'Full')
lozano = Prof('Lozano', 'Tomas', 'Full')
guttag = Prof('Guttag', 'John', 'Full')
barzilay = Prof('Barzilay', 'Regina', 'Associate')

course6 = Faculty()
course6.add(grimson)
course6.add(lozano)
course6.add(guttag)
course6.add(barzilay)

for p in course6:
    print(p.familyName())

print(ug.say(grimson, 'I do not understand.'))
print(grimson.say(ug, 'you do not understand.'))
print(grimson.say(guttag, 'why the sky is blue'))

print(ug.sing(ug, 'I think I finally understand.'))
