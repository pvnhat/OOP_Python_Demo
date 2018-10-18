from animal import Animal
from cat import Cat
from unknown import Unknown

animal1 = Animal("unknown")
print(animal1.getName() )
animal1.showInfo()
#animal1.eat();
print("\n")



jerry =  Cat("jerry", 6, 9)
print("Hello, " + jerry.getName())
print("age: " + str(jerry.getAge()))
print("height: " + str(jerry.getHeight()))
jerry.showInfo()
jerry.eat()


unknown = Unknown("name", 9, 6)
unknown.showInfo()



