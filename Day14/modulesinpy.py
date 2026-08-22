#import math
#a,b,c,d,e=1,2,3,4,5
#print(math.e+a)
#print(e+b)###E#### here we can see e=5 and we imported e from math module so if the varible is not defined with module then it takes local variable
#if it is declar with module it take module value###
##########################
#L->E->G->B scope resolution
#def fun1():
 #   a=1
  #  print(a)
#def fun2():
 #   b=2
  #  print(b)
#fun1()
#fun2()
#########same local variable

#def fun1():
 #   x=1
 #   print(x)
#def fun2():
 #   x=2
 #   print(x)
#fun1()
#fun2()
##############enclosed
#def fun1():
   # a=1
    
   # def fun2():
  #      print(a)
 #   fun2()
#fun1()
###############global
#def fun1():
 #   print(x)
#def fun2():
# #   print(x)

#x=4

#fun1()
#fun2()
################Buit-in
#from math import e
#def fun1():
 #   print(e)

#e=4    ######### here it check in order of l-e-g-b  we hve global so it print global value
 
#fun1()


#def greet():
 #   print("Hello!")

##   greet()
  #  print("Program running")

##   main()

def digit(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

print(digit(355))

import math
def countmath(num):
    return int(math.log10(num)+1)
print(countmath(4758))

class Solution:
    def fun(self, x):
        sign = 0
        if x < 0:
            sign = -1
        else:
            sign = 1
        x = abs(x)
        s = str(x)
        n = int(s[::-1])
        if n > ((2**31) - 1):
            return 0
        return n * sign


sol = Solution()
x = -120
print(sol.fun(x))