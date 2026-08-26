########## Pattern 1 ############
#*
#* *
#* * *
#* * * *
#* * * * *
#################################
#n=5
#for i in range(1,n+1):
 #   for j in range(1,i+1):
  #      print("*",end="")
   # print()


######### Pattern 2 #############
#        *
#      * *
#    * * *
#  * * * *
#* * * * *
##################################
#n=5
#for i in range(1,n+1):
#    for j in range(i,i+1):
#        print(" "*(n-i),end="")
#        for k in range(1,i+1):
#         print("*",end="")
#    print()


######### Pattern 3 #############
#* * * * *
#* * * *
#* * *
#* *
#*
################################
#n = 5
#for i in range(n, 0, -1):     # count downward: 5, 4, 3, 2, 1
 #   for j in range(i):
  #      print("*", end=" ")
   # print()



######### Pattern 4 #############  
#* * * * *
#  * * * *
#    * * *
#      * *
#        *
#################################
#n=5
#for i in range(n,0,-1):
 #        print(" "*(n-i),end="")
  #       for k in range(1,i+1):
   #        print("*",end="")
    #     print()



########## Pattern 5 ##############
#        *                      
#      * * *                    
#    * * * * *                  
#  * * * * * * *                
#* * * * * * * * *              
#################################
#n=5
#for i in range(1,n+1):
 #   print(" "*(n-i),end="")
  #  for j in range(2*i-1):
   #      print("*",end="")
    #print()


########### Pattern 6 ############
#        *
#       * *
#      *   *
#     *     *
#    *       *
#     *     *
#      *   *
#       * *
#        *
###################################
#n= 5
#for i in range(1,n+1):
#    print(" "*(n-i),end="")
#    if i==1:
#        print("*")
#    else:
#        print("*"+" "*(2*i-3)+"*")
#for i in range(n-1,0,-1):
#    print(" "*(n-i),end="")
#    if i==1:
#        print("*")
#    else:
#        print("*"+" "*(2*i-3)+"*")
########### Pattern 7 ###################
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5
##########################################
#n=5
#for i in range(1,n+1):
#   for j in range(1,i+1):
#     print(j,end="")
#   print()  
################ Pattern 8 #################   
#1
#22
#333
#4444
#55555
#########################################
#n=5
#for i in range(1,n+1):
#    for j in range(1,i+1):
#        print(i,end="")
#    print()    
################## Pattern 9 ##################
#        1
#      1 2
#    1 2 3
#  1 2 3 4
#1 2 3 4 5
###############################################
#n=5
#for  i in range(1,n+1):
#    print(" "*(n-i),end="")
#    for j in range(1,i+1):
#        print(j,end=" ")
#    print()
################## Pattern 10 ######################
#1 
#2 3 
#4 5 6 
#7 8 9 10 
#11 12 13 14 15 
###################################################
#n=5
#num=1
#for i in range(1,n+1):
#    for j in range(i):
#        print(num,end=" ")
#        num+=1
#    print()
####################### pattern 11 #######################
#1 2 3 4 5 
#1 2 3 4 
#1 2 3 
#1 2 
#1 
##################################################
# n=5
#for i in range(n,0,-1):
#    for j in range(1,i+1):
#        print(j,end=" ")
#    print()    
################### Pattern 12 ###################    
# 1
#0 1 
#1 0 1 
#0 1 0 1 
#1 0 1 0 1 
#################################################
#n=5
#for i in range(1,n+1):
#    for j in range(1,i+1):
#        if (i+j)%2==0:
#         print("1",end=" ")
#        else:
#           print("0",end=" ")
#    print()
################# Pattern 13 ########################
 #    1 
 #   1 1 
 #  1 2 1 
 # 1 3 3 1 
 #1 4 6 4 1 
###################################################
#n = 5
#for i in range(n):
 #   print(" "*(n-i),end="")
  #  val = 1
  #  print(val, end=" ")
   # for j in range(1, i + 1):
   #     val = val * (i - j + 1) // j
   #     print(val, end=" ")
   # print()
#################### Pattern 14 ########################
#A
#B B
#C C C
#D D D D
#E E E E E
#############################################
#n = 5
#for i in range(1, n + 1):
 #   ch = chr(64 + i)          # 1->A, 2->B, 3->C...
  #  for j in range(i):
   #     print(ch, end=" ")
   # print()
################ Pattern 15 #######################
#A
#AB
#ABC
#ABCD
#ABCDE
#################################################
#n=5
#for i in range(1,n+1):
 #   for j in range(1,i+1):
  #      print(chr(64+j),end="")
   # print()
################ Pattern 16 #######################
#A
#B C
#D E F
#G H I J
#K L M N O
################################################
#n=5
#char=1
#for i in range(1,n+1):
 #   for j in range(i):
 #       print(chr(64+char),end=" ")
  #      char+=1
   # print()
############### Pattern 17 #####################
#    *
#   ***
#  *****
# *******
#*********
# *******
#  *****
#   ***
#    *
###############################################
#n=5
#for i in range(1,n+1):
#    print(" "*(n-i),end="")
#    for j in range(2*i-1):
#        print("*",end="")
#    print()
#for i in range(n-1,0,-1):
#    print(" "*(n-i),end="")
#    for j in range(2*i-1):
#        print("*",end="")
#    print()
############### Pattern 18 #####################
#*       *
# *     *
#  *   *
#   * *
#    *
#   * *
#  *   *
# *     *
#*       *
################################################
#n=5
#for i in range(n,0,-1):
#    print(" "*(n-i),end="")
#    if i ==1:
#        print("*")
#    else:
#        print("*"+" "*(2*i-3)+"*")
#for i in range(2,n+1):
#    print(" "*(n-i),end="")
#    if i ==1:
#        print("*")
#    else:
#        print("*"+" "*(2*i-3)+"*")
################### Pattern 19 ################
#* * * * * 
#*       * 
#*       * 
#*       * 
#* * * * * 
############################################
#n=5
#for i in range(n):
#   for j in range(n):
#        if i==0 or i==n-1 or j==0 or j==n-1:
#            print("*",end=" ")
#        else:
#            print(" ",end=" ")
#    print()
################ Pattern 20 ##############################
#1 2 3 4 5 
#2 4 6 8 10 
#3 6 9 12 15 
#4 8 12 16 20 
#5 10 15 20 25 
###########################################
#n=5
#for i in range(1, 6):
#    for j in range(1, 6):
#        print(i * j, end=" ")
#    print()
############################################  
from array import *

myarray = array('i', [10,20,30,40,50])

#print("traversing")
#for x in myarray:
# print(x,end=" ")
#print("accessing")
#print(myarray[0])
#myarray.insert(2,33)
#for x in myarray:
#    print(x)
#myarray.remove(30)
##for x in myarray:
#   print(x)
#print(myarray.index(40))
#myarray[2]=44
#for x in myarray:
# print(x)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#print(matrix[2][2])
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()


    arr = [10, 20, 30, 40, 50]
left = 0
right = len(arr) - 1

while left <= right:
    print(f"left={arr[left]}, right={arr[right]}")
    left += 1
    right -= 1