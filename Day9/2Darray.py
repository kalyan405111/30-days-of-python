#fruits = ["apple", "orange", "banana", "coconut"]
#meats = ["chicken", "fish", "turkey"]

#groceries = [fruits, vegetables, meats]

#print(groceries[0][3])
##print(groceries[1][0])
#print(groceries[2][2])
#number =[]
#phone=((1,2,3),(4,5,6),(7,8,9),("*",0,"#"))
###   row = int(input("enter the row:"))
    #if row==999:
     #   break
    #else:
     #   column = int(input("enter the column:"))
      #  number.append(phone[row][column])

#for i in number:
 #   print(i,end="") 
#n = 5
#for i in range(1, n+1):
  #  print(" "*(n-i), end="")
  #  for j in range(1, i+1):
  #      print(j, end="")  
  #  print()


questions = ("How many elements are in the periodic table? ",
                       "Which animal lays the largest eggs?: ",
                       "What is the most abundant gas in Earth's atmosphere? ",
                       "How many bones are in the human body? ",
                       "Which planet in the solar system is the hottest? ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
                   ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
                   ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
                   ("A. 206", "B. 207", "C. 208", "D. 209"),
                   ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0
 
for question in questions:
    print(question)
    for option in options[question_num]:
     print(option)
    
    guess=input("enter your answer:").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        print("correct")
        score+=1
    else:
       print(f"the correct answer is {answers[question_num]}")
    question_num+=1
print("============result===============")
print("answer: ",end="")
for answer in answers:
   print(answer,end=" ")
print()

print("your guess: ",end="")
for guess in guesses:
   print(guess, end=" ")
print()


score=int(score/len(questions))*100
print("=============your score ==============")
print(f"                {score}%                 ")
print("======================================")
   