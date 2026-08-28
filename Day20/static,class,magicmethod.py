class Employee:
    def __init__(self,name ,position):
        self.name=name
        self.position=position

    def info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def valid_post(position):
        valid_post=["manger","cook"]
        return position in valid_post

employee = Employee("raju","manager")
employee1 = Employee("raju","cook")

print(Employee.valid_post("manger"))
print(employee.info())
print(employee1.info())
#################################################################################
# Class methods = Allow operations related to the class
#                                Take (cls) as the first parameter, which represents the class itself.

#  Instance methods = Best for operations on instances of the class (objects)
#  Static methods = Best for utility functions that do not need access to class data
#  Class methods = Best for class-level data or require access to the class itself

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa / cls.count:.2f}"

student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)
student3 = Student("Sandy", 4.0)

print(Student.get_count())
print(Student.get_average_gpa())##class method   
print(student1.get_info())##instance method
##################################################################################################
# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                                 They are automatically called by many of Python's built-in operations.
#                                 They allow developers to define or customize the behavior of objects

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found"

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)

print(book1)  # Calls __str__
print(book1 == book3)  # Calls __eq__
print(book1 < book2)  # Calls ___lt__
print(book2 > book3)  # Calls __gt__
print(book1 + book2)  # Calls __add__
print("Lion" in book3)  # Calls __contains__
print(book3['title'])  # Calls __getitem__
