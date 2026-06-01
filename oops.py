# To Map with real world scenarioes, we started using  objects in code. This is called 
# oops

class Car:
    color = "blue"
    brand = "mercedes"
    horse_power = "1200"

Car1 = Car()
print(Car1.color)
print(Car1.brand)
print(Car1.horse_power)


# Constructor: it is basically an init function. All classes have a function called _init_ 
# _() Which is always executed when the class is being initiated

# Creating class
# Class Student:
#    def__init__(self, fullname):
#         self.name = fullname 

# the self parameter is used to reference to current instance of the class,
# and is used to access variables that belongs to the class.

# Creating Object
# s1 = Student("Karan")
# print(s1.name)


class student:

    def __init__(self):
        pass

    def __init__(self, name, marks):
        self.name = name 
        self.marks = name 
        print("adding new students in database...")

s1 = student("karan ", 97)
print(s1.name, s1.marks )

s2 = student ("Arjun ", 88)
print(s2.name, s2.marks )

