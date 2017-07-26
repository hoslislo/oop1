# sample class syntax

class Bear:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


a = Bear("Oski", 180)
b = Bear("Winnie", 100)
c = Bear("Yogi", 115)

# Class instances in Python can be treated like any other data type:
# they can be assigned to other variables, put in lists, iterated over, etc.

my_bears = [a, b, c]

total_weight = 0
for z in my_bears:
    total_weight += z.weight
print (total_weight < 300)
print a
print b

class Bear:
    def vocalize(self):
        print("growl")
class Cat:
    def vocalize(self):
        print("meow")
class Duck:
    def vocalize(self):
        print("quack")

oski = Bear()
bill = Cat()
daffy = Duck()

def harmonize(chorus):
    for member in chorus:
        member.vocalize()

# The harmonize() function doesn't care at all what each type of singer is. Each singer simply must have a vocalize() method.

harmonize([oski, bill, daffy])

'''
False
<__main__.Bear instance at 0x02A1E5F8>
<__main__.Bear instance at 0x02A1E620>
growl
meow
quack
'''
'''
a class is an object, like a template or, e.g., a record; inside the class are methods, which are just functions by another name
variables defined in a class are available only within the class; a variable might be defined in a class to be used as an attribute
    def __init__(self, name, weight): Python requires "self" as part of the method definition and uses it to assign attributes, etc.
a = Bear("Oski", 180) creates an instance of the object, i.e., a is instantiated; in the print, a is not the same as b; they are different instances of the object
__init__ is a method that initializes the instance of the object
advantages of classes are reusability, easier to maintain, etc., etc.
'''