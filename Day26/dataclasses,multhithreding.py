# Generator Expression = Similar to a list comprehension but uses () instead of []
# Creates a generator (iterator) that yields values one at a
# No need to define a function or use yield
# Less flexible than a gen func and not reusable
# object = (expression for value in iterabler if condition)

number = int(input("Enter a number to square up to: "))

even_squares = (x ** 2 for x in range(1, number + 1) if x % 2 == 0)

for square in even_squares:
  print(square)
###################################################################
# Data Class = A special kind of class that's designed mostly for holding data
#                        without writing a lot of the boilerplate code for regular classes.
#                        They automatically generate: _init__, __repr__, __eq_
#                       (Python 3.7+)

from dataclasses import dataclass, field

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    password: str = field(repr=False)
    is_alive: bool = True

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")

person1 = Person("Spongebob", 30, "pineapple1")
person2 = Person("Patrick", 35, "password")
# person1.age = 31  # This will raise an error because the dataclass is frozen

print(person1)
print(person2)
print(person1 == person2)

#################################################################
# multithreading = Used to perform multiple tasks concurrently (multitasking)
#                               Good for I/O bound tasks like reading files or fetching data from APIs

import threading
import time

def walk_dog(first, last):
   time.sleep(8)
   print(f"You finish walking {first} {last}")

def take_out_trash():
   time.sleep(2)
   print("You take out the trash")

def get_mail():
   time.sleep(4)
   print("You get the mail")

chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

# .join() ensures that all tasks are completed before proceeding
chore1.join()
chore2.join()
chore3.join()

print("All chores are complete!")
