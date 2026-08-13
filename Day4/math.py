friend =2
#friend +=1
#friend -=2
#friend*= 2
#friend **=2
reminder = friend // 2
#print(friend)
#print(reminder)

x=3
y = 4.344444
z= 4
result = pow(4, 2)
minimum = min(x,y,z)
maximum = max(x,y,z)
#print(f"the minimum value is :{minimum}")   
#print(f"the maximum value is :{maximum}")
#print(f"the rounded value is :{result}")

import math

x=9.4
result = math.floor(x)
result = math.ceil(x)
#print(f"the floor value of {x} is :{result}")

#print(f"the square root of {x} is :{result}")

#print(round(math.pi,3))
#print(round(math.e,3))
#radius = float(input("enter the radius of circle:"))
#circumference = 2 * math.pi * radius
#area = math.pi * radius ** 2
#print(f"the circumference of circle is :{round(circumference,2)}")
#print(f"the area of circle is :{round(area,2)}")


age = int(input("enter your age:"))
if age >=18:
    print("you can vote ")
else:
    print("you cant vote")    


order=input("what do you want to order sir:")
if order == "y":
    print("yes")
elif order =="n":
    print("puck you ")
else:
    print("go to other place broo")

