#num =5
#print("hi" if num>0 else "hiii")
#cost= int(input("enter the value:"))
#result = "even" if num %2==0  else "odd" "hi"if num1=="10" else "hiiiiii"
#age = 19
#result = "old" if age >=18 else "child"
#result= "buy" if cost <100 else "to much cost "
#print(result)
#name=input("enter your name :")
#hello=name.len()
#hello =name.find("a")
#hello=name.rfind("a")
#hello=name.capitalize()
#hello= name.upper()
#hello = name.lower()
#hello= name.isdigit()
#hello=name.isalpha()
#hello=name.count("0")
#hello=name.replace("0","4")
#print(hello)
#name = input("Enter the user name: ")

#if len(name) > 12:
#    print("Name should be less than 12 characters.")
#elif " " in name:
#    print("Spaces are not allowed.")
#elif not name.isalpha():
#    print("Only letters are allowed.")
#else:
 #   print(f"The name is: {name}")

#number="1234-5678"
#print(number[-9:4   ])

#student = input("Enter your name: ")
#index = student.index(" ")
#name=student[:index]
#cl=student[index+1:]
#print(f"Name: {name}")  #

#print(f"Class: {cl}")      

# price=3333.333444444444444444444444444444444444
#print(f"the price is :${price:.2f}")
#print(f"the price is :${price:10.2f}")
#print(f"the price is :${price:<10.2f}")
#print(f"the price is :${price:>10.2f}")
#print(f"the price is :${price:^10.2f}")
#print(f"the price is :${price:+}")
#print(f"the price is :${price:+,.2f}")
#print(f"the price is :${price:=+,.2f}")
#print(f"the price is :${price: 2f}")
#print(f"the price is :${price:+,.2f}")



s = "helloworld"

q = ["o", "l", "j", "h"]

hash = [0] * 26

# Count each character
for i in s:
    ascii = ord(i)
    index = ascii - 97
    hash[index] += 1

# Example: find how many times "o" occurs
# ord("o") = 111
# index = 111 - 97 = 14
# So hash[14] stores the count of "o"

print("Number of times o occurs:", hash[14])

# Find frequency of characters in q
for i in q:
    ascii = ord(i)
    index = ascii - 97
    print(i, hash[index])