#class Library:
#    def __init__(self,name):
#        self.name=name
#        self.books=[]

#    def add_books(self,book):
#        self.books.append(book)    

#    def list_books(self):
#        return (f"{books.title} by {books.author}" for books in self.books)  

#class Book:
#    def __init__(self,title,author):
#        self.title= title
#        self.author=author

#library=Library("mind blowing Library")
#book1=Book("raju story","raju")
#book2=Book("ramesh story","ramesh")

#library.add_books(book1)
#library.add_books(book2)

#print("#########################")
#print( "  "   , library.name)
#print("#########################")
#for books in library.list_books():
#    print(books)
############################################################################
# Composition = The composed object directly owns its components, which cannot exist independently
#                            "owns-a" relationship

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]

    def display_car(self):
        return f"{self.make} {self.model} {self.engine.horse_power}(hp) {self.wheels[0].size}in"

car1 = Car(make="Ford", model="Mustang", horse_power=500, wheel_size=18)
car2 = Car(make="Chevrolet", model="Corvette", horse_power=670, wheel_size=19)

print(car1.display_car())
print(car2.display_car())
#############################################################################
# Nested class = A class defined within another class
#                            class Outer:
#                                class Inner:

# Benefits: Allows you to logically group classes that are closely related
#                 Encapsulates private details that aren't relevant outside of the outer class
#                 Keeps the namespace clean; reduces the possibility of naming conflicts

class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)

    def list_employees(self):
        return [employee.get_details() for employee in self.employees]

company1 = Company("Krusty Krab")
company2 = Company("Chum Bucket")

company1.add_employee("Eugene", "Manager")
company1.add_employee("Spongebob", "Cook")
company1.add_employee("Squidward", "Cashier")

company2.add_employee("Sheldon", "Manager")
company2.add_employee("Karen", "Assistant")

for employee in company2.list_employees():
    print(employee)


        


