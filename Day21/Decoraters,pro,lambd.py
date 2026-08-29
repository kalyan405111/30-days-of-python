# Decorator = A function that extends the behavior of another function
#                      w/o modifying the base function
#                      Pass the base function as an argument to the decorator

# def add_sprinkles(func):
    # def wrapper(*args, **kwargs):
        # print("*You add sprinkles 🎊*")
        # func(*args, **kwargs)
    # return wrapper

# def add_fudge(func):
    # def wrapper(*args, **kwargs):
        # print("*You add fudge 🍫*")
        # func(*args, **kwargs)
    # return wrapper

# @add_sprinkles
# @add_fudge
# def get_ice_cream(flavor):
    # print(f"Here is your {flavor} ice cream 🍨")

# get_ice_cream("vanilla")
############################################################
# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#                        Benefit: Add additional logic when you read, write, or delete attributes
#                        Gives you a getter, setter, and deleter method

# class Rectangle:
    # def __init__(self, width, height):
        # self._width = width
        # self._height = height
# 
    # @property
    # def width(self):
        # return f"{self._width:.1f}cm"

    # @property
    # def height(self):
        # return f"{self._height:.1f}cm"

    # @width.setter
    # def width(self, new_width):
        # if new_width > 0:
            # self._width = new_width
        # else:
            # print("Width must be greater than zero")
# 
    # @height.setter
    # def height(self, new_height):
        # if new_height > 0:
            # self._height = new_height
        # else:
            # print("Height must be greater than zero")
# 
    # @width.deleter
    # def width(self):
        # del self._width
        # print("Width has been deleted")

    # @height.deleter
    # def height(self):
        # del self._height
        # print("Height has been deleted")
# 
# rectangle = Rectangle(3, 4)

# rectangle.width=0
# print(rectangle.width)
#################################################################
double= lambda x : x*3
add = lambda x,y : x+y
max = lambda x,y: x if x>y else y
min = lambda x,y: x if x<y else y
full_mane = lambda first , last : first + " " + last
age = lambda age : True if age>18 else False
print(full_mane("kalyan","yalla"))
print(age(22))
print(add(2,3))
print(double(2))
print(max(4,5))
print(min(5,4))
