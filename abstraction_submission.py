#
#Version: Python 3.11.1
#
#Author: Jon Duea
#
#Purpose: To create a class that utilizes the concept of abstraction
#

from abc import ABC, abstractmethod

class Person(ABC):
    def getName(self, name):
        print("Hello {}!".format(name))
#This function defines the arguments for it without telling you how or what kind of data it will be
    @abstractmethod
    def getContactInfo(self,name,email):
        pass

#create the child class student that inherits from the Person class
class Student(Person):
#Here we define how we want to implement the getContactInfo function from the parent class
    def getContactInfo(self,name,email):
        print('Hello {}, your currently saved contact e-mail is {}'.format(name,email))

if __name__ == "__main__":

    #This creates an instance of the student class and assigns it to the variable student1 and then utilizes the functions from the parent class
    student1 = Student()
    student1.getName('John Doe')
    student1.getContactInfo('John Doe', 'JohnDoe@gmail.com')
    
    #This checks if the student1 object we instantiated is an instance of the Person class and returns true or false.
    print('student1 is an instance of the Person class?', isinstance(student1, Person))
