#list,tuple,set
#fruit =["apple","panana","graps"]
#print(fruit[::-1])
# #print(len(fruit))
#print("apple"in fruit)
#fruit[0]="rara"
#fruit.insert(0,"randi")
#fruit.remove("apple")
#fruit.sort()
#print(fruit.index("apple"))
#print(fruit.count("apple"))
#fruit.reverse()
#fruit.clear()
#print(fruit)
#print(fruit)
###################################################################
#list
#fruit ={"apple","panana","graps","juice"}
#print("apple" in fruit)
#fruit.add("banana")
#fruit.remove("apple")
#fruit.pop()
#fruit.clear()
#print(fruit)
##################################################################
#tuple
#fruit =["apple","panana","graps"]
#print(help(fruit))
###################################################################


#problem
foods = []
prices=[]
total=0
while True:
    food = input("enter your food items (q to quit):").lower()
    if food.lower()=="q":
        break
    if food ==" ":
        print("no space are allowed")
    else:
        price=float(input("enter the price of the:${food}")) 
        foods.append(food)
        prices.append(price)   

print("=======your cart========")
for food in foods:

   print(food,"=",price)

for price in   prices:
    total+=price

print(f"the total cost is :${total}")







