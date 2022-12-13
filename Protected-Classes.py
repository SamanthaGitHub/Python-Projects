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

    def getCourse(self): # print the variables
        print(self.__course)

    def setCourse(self, newCourse): # sets a new course
        self.__course = newCourse



if __name__ == "__main__":
    sam = Student()
    print(sam._name) # printing the protected variable
    sam._name = 'Samantha'
    print(sam._name) # printing the updated protected variable
    sam.getCourse() # prints the private variable __course
    sam.setCourse('C#') # sets a new course using a private variable
    sam.getCourse() # prints the new/set private variable __course
