#
# Python:   3.9.7
#
# Author:    Samantha
#
# Purpose:  To demonstrate the use of private and proteced
#           attributes in classes.

class Student:
    def __init__(self):
        self._name = 'Sam' # protected variable
        self.__course = 'Python' # private variable

    def getInfo(self): # print the variables
        print(self._name)
        print(self.__course)

    def setName(self, newName): # sets a new name
        self._name = newName



if __name__ == "__main__":
    sam = Student()
    sam.getInfo()
    sam.setName('Samantha')
    sam.getInfo()
