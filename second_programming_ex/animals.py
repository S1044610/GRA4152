## The superclass for different types of animals.
# It is the attributes and methods that are common to all animals.
#       
class Animal:   
    def __init__(self, animalType):
        "Initialises the Animal with a specified type."
        self._type = animalType
    
    def greets(self):
        "Abstract method for animal greeting. To be overridden in subclasses."
        raise NotImplementedError
       
    def run(self):
        "Prints a message indicating that the animal is running. "
        print('The {} is running'.format(self._type))
    
    def summarizeMyanimal(self):
        "Calls the greets and run methods for the animal's behaviors."
        self.greets()
        self.run()

## A cat class is a subclass of Animal.
# Inherits the Animal class and overrides the greets method.
#
class Cat(Animal):
    "Initialises the Cat with a specified type."
    def __init__(self, animalType):
        super().__init__(animalType)

    def greets(self):
        "Overrides the greets method from Animal class to print the cat's greeting 'meow'"
        print("meow")

## A dog class is a subclass of Animal.
# Inherits the Animal class and overrides the greets method.
#
class Dog(Animal):
    def __init__(self, animalType):
        "Initializes the Dog with a specified type."
        super().__init__(animalType)
    
    def greets(self):
        "Overrides the greets method from Animal class to print the dog's greeting 'woof'."
        print("woof")

## A big dog class is a subclass of Dog and Animal
#  Inherits the Animal class and Dog class and overrides the greets method.
#
class BigDog(Dog):
    def greets(self):
        "Overrides the greets method from Dog class and add an additional greeting 'woooof'."
        super().greets() 
        print("woooof") 

# polymorphism: Instances of Cat, Dog, and BigDog
mycat = Cat(animalType='cat')
mydog = Dog(animalType='dog')
my_big_dog = BigDog(animalType='big dog')

mycat.summarizeMyanimal()
mydog.summarizeMyanimal()
my_big_dog.summarizeMyanimal()


#Inheritance:
# Subclasses Cat, Dog, and BigDog are inherit from the superclass Animal. 

#Overriding:
# Subclasses Cat, Dog, and BigDog overrides the greets method. 

#Polymorphism:
# The greets method can be differently baes on the subclass that invokes it. 
# Even though each class has a greets method, it is polymorphism, 
# the output will be different when called on an instance of Cat, Dog, or BigDog.


    
