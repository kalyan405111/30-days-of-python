import time
start=time.perf_counter()
for i in range(1000):
    pass
end=time.perf_counter()
result=end-start
print(f"Execution time: {result:.2f} seconds")
#########################################################
# Python reading files (.txt, .json, .csv)

# ---------- .txt ----------

file_path = "C:/Users/HP/Desktop/input.txt"

try:
  with open(file_path, 'r') as file:
     content = file.read()
     print(content)
except FileNotFoundError:
  print("That file was not found")
except PermissionError:
  print("You do not have permission to read that file")

# ---------- .json ----------
import json

file_path = "C:/Users/HP/Desktop/input.json"

try:
  with open(file_path, 'r') as file:
      content = json.load(file)
      print(content )
except FileNotFoundError:
  print("That file was not found")
except PermissionError:
  print("You do not have permission to read that file")

# ---------- .csv ----------
import csv

file_path = "output.csv"

try:
  with open(file_path, 'r') as file:
      content = csv.reader(file)
      for line in content:
          print(line)
except FileNotFoundError:
  print("That file was not found")
except PermissionError:
  print("You do not have permission to read that file")
  ###################################################################
import datetime

date = datetime.date(2025, 1, 2)
today = datetime.date.today()

time = datetime.time(12, 30, 0)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %m-%d-%Y")
print(f"Current time is: {now}")

#target_datetime = datetime.datetime(2020, 1, 2, 12, 30, 1)
#current_datetime = datetime.datetime.now()

#if target_datetime < current_datetime:
  #  print("Target date has passed")
#else:
 #   print("Target date has NOT passed")

