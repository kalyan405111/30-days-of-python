#names={"kalyan","raju","rajesh"}
#name=input("enter your name:-")
#if name in names:
 #   print(f"the name is in list:-{name}")
#else:
#   print(f"the  name is not in list:{names}")

#word ="kalyan"
#name=input("enter your secret word")
#if name not in word:
 #   print(f"the word is not in name")
    
#else:
 #   print(f"the word is in name{name}")

#menu={"name":"kalyan","age":25,"school":"prakash"}
#details=input("enter your thing:")
#if details in menu:
 #   print(f"{details}:{menu[details]}")
#else:
 #   print("no")    
#grades=[45,60,65,76,69,98,88]
#pass_grade=[grade for grade in grades if grade>=60]
#print(pass_grade)
def match_day(n):
    match n:
        case 1:
            return "this is sunday"
        case 2:
            return "this is monday"
        case _:
            return "what the hell"
print(match_day(3))

def week_end(day):
    match day:
        case "saturday" | "sunday":
            return True
        case "monday"|"tuesday"|"wednesday"|"friday"|"thursday":
            return False
print(week_end("monday"))       
        