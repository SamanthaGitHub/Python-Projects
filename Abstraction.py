#
# Python:   3.9.7
#
# Author:    Samantha
#
# Purpose:  To demonstrate the use of abstraction.
#           The class should containat least one abstract method and one
#           regular method.  
#           Create a child class that defines the implementation of its parents
#           abstract method.
#           Create an object that utilizes both the parent and child methods.

from abc import ABC, abstractmethod

class Box(ABC):
    @abstractmethod # abstract method
    def volume(self):
        pass
    
    def height(self, height): # regular method
        print("The height of the box is {}".format(height))

class Big(Box): # child class that defined the volume method
    def __init__(self, height, width, length):
        self._height = height
        self._width = width
        self._length = length

    def volume(self):
        return self._height * self._width * self._length 

    
        
if __name__ == "__main__":
    myBox = Big(100,50,70) # my myBox object
    print(myBox.volume())
    myBox.height(100)
