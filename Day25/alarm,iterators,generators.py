# Python Alarm Clock
# import time
# import datetime
# import pygame
# 
# 
# def set_alarm(alarm_time):
    # print(f"Alarm set for {alarm_time}")
    # sound_file = "my_music.mp3"
    # is_running = True
# 
    # while is_running:
        # current_time = datetime.datetime.now().strftime("%H:%M:%S")
        # print(current_time)
# 
        # if current_time == alarm_time:
            # print("WAKE UP! 😴")
# 
            # pygame.mixer.init()
            # pygame.mixer.music.load(sound_file)
            # pygame.mixer.music.play()
# 
            # while pygame.mixer.music.get_busy():
                # time.sleep(1)
# 
            # is_running = False
# 
        # time.sleep(1)


# if __name__ == "__main__":
    # alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    # set_alarm(alarm_time)
    #############################################################
   # Iterator = An object that returns elements one at a time
#                  from a sequence (or data stream)
#                  and remembers its position between calls.
#                  A Python object is an iterator if it has:
#                 __iter__() → Returns the iterator object itself
#                 __next__() → Returns the next item in the sequence
#                                        (raises StopIteration when there's no more items)

import random

class Dice:
    def __init__(self, rolls):
        self.rolls = rolls
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.rolls:
            self.count+=1
            return random.randint(1, 6)
        else:
            raise StopIteration

dice = Dice(3)

for die in dice:
    print(die)
###########################################################
# Generator = Function that behaves like an iterator (it can be used in a for loop)
#                      Pauses a function, returns a value, then resumes
#                      Uses 'yield' instead or 'return'
#                      Iterate without loading everything into memory (ex. reading large files)
#                      return = Pouring bucket
#                      yield = Drip faucet

# ---------- EXAMPLE 1 ----------

def count_to(n):
   count = 1
   while count <= n:
       yield count  # Pause here and return the current value
       count += 1

number = int(input("Enter a number to count up to: "))

for n in count_to(number):
   print(n)

# ---------- EXAMPLE 2 ----------

def read_file(file_path):
   with open(file_path) as file:
       for line in file:
           yield line.strip()

filepath = "output.txt"

for line in read_file(filepath):
   print(line)