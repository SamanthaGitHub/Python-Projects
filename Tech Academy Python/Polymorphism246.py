
#parent class
class Tomato:
    def __init__(self,stemColor,fleshColor,waterContent):
        self.stemColor = stemColor
        self.fleshColor = fleshColor
        self.waterContent = waterContent

    def information(self):
        message = "This tomato has a {} stem, {} body, and has {} water content"\
                  .format(self.stemColor,self.fleshColor,self.waterContent)
        return message

#child class
class Cherry(Tomato):
    def __init__(self,stemColor,fleshColor,waterContent,roundness):
        super().__init__(stemColor,fleshColor,waterContent)
        self.roundness = roundness
        
    def information(self):
        message = "This tomato has a {} stem, {} body, {} water content, and is {} round"\
                  .format(self.stemColor,self.fleshColor,self.waterContent, self.roundness)
        return message

#child class
class Roma(Tomato):
    def __init__(self,stemColor,fleshColor,waterContent,ratio):
        super().__init__(stemColor,fleshColor,waterContent)
        self.ratio = ratio

    def information(self):
        message = "This tomato has a {} stem, {} body, {} water content, and a flesh to water ratio of {}"\
                  .format(self.stemColor,self.fleshColor,self.waterContent, self.ratio)
        return message



if __name__ == "__main__":
    tom1 = Tomato('green','red','high')
    print(tom1.information())

    tom2 = Cherry('green','yellow','low','very')
    print(tom2.information())

    tom3 = Roma('brown','green','low','2:1')
    print(tom3.information())
