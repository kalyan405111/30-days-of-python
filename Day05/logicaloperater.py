#x= int(input("enter a number:"))
#sunny =(input("is it sunny outside:"))

#if x<=50 and x>111=100:
 #   print(" the value is between 50 and 100")
#elif x==50 or x==100:
#    print("the value is either 50 or 100")
#else:
 #   print("the value is not between 50 and 100")


#if  sunny=="no" and sunny=="yes":
   # print("it is sunny outside")
#else:
 #   print("it is not sunny outside")

value = input("enter the sign value[+,-,*,%] :")
num= float(input("enter the 1st value:"))
num1= float(input("enter the 1st value:"))
if value =="+" :
    result= num + num1
    print(f"the sum of the number is: {result}")
elif value =="-":
    result = num - num1
    print(f"the sub  value is: {result}")
elif value =="*":
    result = num * num1
    print(f"the sub  value is: {result}")
elif value =="%":
    result = num % num1
    print(f"the sub  value is: {result}")
else:
    print("enter the value correctly")    
