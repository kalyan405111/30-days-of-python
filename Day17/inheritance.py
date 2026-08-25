#class Animal:
#    def __init__(self,name):
#        self.name=name
#        self.is_alive=True

#    def eat(self):
#        print(f"{self.name} is eating")

#    def sleep(self):
#        print(f"{self.name} is sleeping")

#class Dog(Animal):
#    def speak(self):
#        print("the dog sound is woof")


#dog=Dog("puppy")
#print(dog.name)
#dog.speak()
#dog.eat()
#dog  .sleep()
#########################################################
#class Animal:

#   def __init__(self, name):
#        self.name = name

#    def eat(self):
#        print(f"{self.name} is eating")

#    def sleep(self):
#        print(f"{self.name} is sleeping")

#class Prey(Animal):
#    def flee(self):
#        print(f"{self.name} is fleeing")

#class Predator(Animal):
#    def hunt(self):
#        print(f"{self.name} is hunting")

#class Rabbit(Prey):
#    pass

#class Hawk(Predator):
#    pass

#class Fish(Prey, Predator):
#   pass

#rabbit = Rabbit("Bugs")
#hawk = Hawk("Tony")
#fish = Fish("Nemo")
############################################################

# Abstract class: A class that cannot be instantiated on its own; Meant to be subclassed.
#                 They can contain abstract methods, which are declared but have no implementation.
#                 Abstract classes benefits:
#                 1. Prevents instantiation of the class itself
#                 2. Requires children to use inherited abstract methods

#from abc import ABC, abstractmethod

#class Vehicle(ABC):

 #   @abstractmethod
  #  def go(self):
  #      pass

 #   @abstractmethod
 #   def stop(self):
 #       pass

#class Car(Vehicle):

  #  def go(self):
   #     print("You drive the car")

  #  def stop(self):
   #     print("You stop the car")

#class Motorcycle(Vehicle):

   # def go(self):
   #     print("You ride the motorcycle")

 #   def stop(self):
 #       print("You stop the motorcycle")

#class Boat(Vehicle):

  #  def go(self):
 #       print("You sail the boat")
#
#    def stop(self):
#        print("You anchor the boat")

#car = Car()
#motorcycle = Motorcycle()
#boat = Boat()
#car.go()
#boat.go()
#car.stop()
#boat.stop()
######################################################