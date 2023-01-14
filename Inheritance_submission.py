#
#Version: Python 3.11.1
#
#Author: Jon Duea
#
#Purpose: To create two classes that inherit from another class
#

"""creates the person class, with the firstname and lastname properties
    and a printname method
"""

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

"""This uses the person class to create an object and then excecutes
    the printname method to return the name
"""

person1 = Person('Jon', 'Duea')
person1.printname()


"""This creates a child class of the person class and adds the properties
    graduationyear and major
"""

class Student(Person):
    def __init__(self, fname, lname, year, major):
        super().__init__(fname, lname)
        self.graduationyear = year
        self.areaofstudy = major

    def printname(self):
        print(self.firstname, self.lastname, self.graduationyear, self.areaofstudy)

"""This uses our newly created Student class that inherits the properties of
    the Person class (firstname, lastname) and uses the newly added properties
    in the printname method
"""

student1 = Student('Jon', 'Duea', '2023', 'Software Development')
student1.printname()

"""This creates another child class of the Person class and adds the properties
    job and wage
"""

class Employee(Person):
    def __init__(self, fname, lname, job, wage):
        super().__init__(fname, lname)
        self.occupation = job
        self.basepay = wage

    def printname(self):
        print(self.firstname, self.lastname, self.occupation, self.basepay)

"""This uses our newly created Employee class that inherits the properties
    of the Person class (firstname, lastname) and uses the newly added properties
    in the printname method
"""

employee1 = Employee('Jon', 'Duea', 'Software Developer', '100k')
employee1.printname()
    
