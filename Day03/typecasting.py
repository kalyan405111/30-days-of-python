#mad lib
#tyoe casting ,userinput 
age=33
age=float(age)
print(type(age))
print(age)

student=True
student=str(student)
print(type(student))
print(student)

age=bool(age)
print(age)
print(type(age))
x=2
y=2.0
x=x/y
print(x)

age =int(input("what is your age:"))

age =age+33
print(f"your age is:{age}")

#################################################1 problem

adjactive=input("enter an adj" )
noun=input("enter your noun")
verb=input("enter your  verb")
adj=input("enter your adj")
print(f"i saw an {adjactive} youtube channel")
print(f"the youtube channel name is {noun}")
print(f"brocode was {verb} a code")
print(f"i like the {adj}")

#################################################2 problem

length=int(input("enter the length :"))
width=int(input("enter the width :"))
height =int(input("enter the height:"))
volume= length + width + height

print(f"the volume of triangle is :{volume}")

#################################################3 problem

item=input("what do you want to buy:")
price=float(input("the cost of that is:"))
quantity= int(input("how many you want:"))
total=  price * quantity
print(f"the total cost is{round(total,2)}")
#################################################