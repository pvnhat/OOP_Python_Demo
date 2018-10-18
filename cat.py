from animal import Animal       
         
# Lớp Cat kế thừa (extends) từ lớp Animal.
class Cat (Animal): 
     
    def __init__(self, name, age, height):
        super().__init__(name)
        self.age = age 
        self.height = height



    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

    def setHeight(self, height):
        self.height = height

    def getHeight(self):
        return self.height

     
    # override phương thức cùng tên của lớp cha.
    def showInfo(self): 
        print ("I'm " + self.name)
        print (" age " + str(self.age))
        print (" height " + str(self.height))
        animal = Animal("animal A");
        animal._testProtected() #call this method from its superClass
        #animal.__testPrivate() #call this method from its superClass



    #override eat() method
    def eat(self):
        print("Fish")