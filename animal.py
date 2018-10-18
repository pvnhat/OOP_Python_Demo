class Animal :  
 
    # Constructor
    def __init__(self, name):
        self.name= name 


    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name


    # Phương thức (method):
    def showInfo(self):
        print ("I'm " + self.name)


    def __testPrivate(self):
        print("You can't access this method form another class")

    def _testProtected(self):
        print("Only access this method from its Subclass")


    #abs class 
    def eat(self):
    	raise NotImplementedError("Subclass must implement abstract method")