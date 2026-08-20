#import random
#import string

#chars = " " + string.punctuation + string.digits + string.ascii_letters
#chars = list(chars)
###random.shuffle(key)

#ENCRYPT
##plain_text = input("Enter a message to encrypt: ")
#ipher_text = ""

#for letter in plain_text:
 #   index = chars.index(letter)
  #  cipher_text += key[index]

#print(f"original message : {plain_text}")
#print(f"encrypted message: {cipher_text}")

#DECRYPT
#cipher_text = input("Enter a message to encrypt: ")
#plain_text = ""

#for letter in cipher_text:
 #   index = key.index(letter)
  #  plain_text += chars[index]

#print(f"encrypted message: {cipher_text}")
#print(f"original message : {plain_text}")

#def display_invoice(username, amount,month,day,year):
 #   print(f"the invoice for :-{username}")
  #  print(f"the amount to pay is:- ${amount}")
   # print(f"before the due date of:- {month}/{day}/{year}")

#display_invoice("kalyan",4500,12,3,2036)

#def add(x,y):
  #  z=x+y
 #   return z

#print(add(1,2))

#def creat_name(first, last):
 #   first=first.capitalize()
  #  last=last.capitalize()
   # return first+" "+last
#full_name=creat_name("bro","code")
#print(full_name)

#def mrp(price,discount=0,tax=0):
 #   return price+discount*tax
#print(mrp(444,1,40))

#import time
#def clock(start,end):
    
    #for i in range(start,end+1):
   #     print(i)
  #      time.sleep(1)
 #   print("done")
#clock(1,5)

#num1=int(input("enter your first number:"))
#um2=int(input("enter your second number:"))
#if num2>num1:
#    mn=num1
#else:
 #   mn=num2

#for i in range(1,mn+1):
 #   if num1%i==0 and num2%i==0:
  #      hcf=i

#print("the hcf of the two numbers is {hcf}")


