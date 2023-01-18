#
#Version: Python 3.11.1
#
#Author: Jon Duea
#
#Purpose: Create a class with a protected property, a private property, and create
#           an object of that class that utilizes the protected and private properties.
#

"""creates the person class, with the firstname as a protected property
    and lastname as a  private property. Then the getName and setName methods
    are added so we can view/change the data stored as needed
"""

class Person:
    def __init__(self):
        self._firstname = 'Jon'
        self.__lastname = 'Duea'

    def getName(self):
        print(self._firstname, self.__lastname)


    def setName(self, setFirstName, setLastName):
        self._firstname = setFirstName
        self.__lastname = setLastName


if __name__ == "__main__":

    """This creates the an instance of the person class as person1 and calls the
        getName method to output the info stored initially, then uses the setName
        method to change the info stored and finally prints the new info
    """
    person1 = Person()
    person1.getName()
    person1.setName('John', 'Doe')
    person1.getName()
