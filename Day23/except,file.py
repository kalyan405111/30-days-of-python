# exception = An event that interrupts the flow of a program
#                     (ZeroDivisionError, TypeError, ValueError)
#                     1.try, 2.except, 3.finally

# try:
    # number = int(input("Enter a number: "))
    # print(1 / number)
# except ZeroDivisionError:
    # print("You can't divide by zero IDIOT!")
# except ValueError:
    # print("Enter only numbers please!")
# except Exception:
    # print("Something went wrong!")
# finally:
    # print("Do some cleanup here")
#################################### File Detection ####################################


# Python file detection

#import os

# file_path = r"C:\Users\user\OneDrive\Desktop\22mh1a42a7.png"
# 
# if os.path.exists(file_path):
    # print(f"The location '{file_path}' exists")
# 
  #  if os.path.isfile(file_path):
        # print("That is a file")
    # elif os.path.isdir(file_path):
        # print("That is a directory")
# else:
    # print("That location doesn't exist")
############################### File  writing ######################################


# Python writing files (.txt, .json, .csv)

# --------- .txt ---------
txt_data = "I like pizza!"

file_path = "output.txt"

try:
   with open(file_path, 'w') as file:
      file.write(txt_data)
      print(f".txt file '{file_path}' has been created successfully")
except FileExistsError:
   print("That file already exists")

# --------- .json ---------

import json

employee = {
   "name": "Spongebob",
   "age": 30,
   "job": "Cook"
}

file_path = "output.json"

try:
    with open(file_path, 'w') as file:
        json.dump(employee, file, indent=4)

    print(f"JSON file '{file_path}' has been created successfully")
except FileExistsError:
    print("That file already exists!")

# --------- .csv---------
import csv

employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

file_path = "output.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")