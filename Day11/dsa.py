low = 1
high = 100
options = ("Rock", "Paper", "Scissors")
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# number = random.random()
# number = random.randint(low, high)
# choice = random.choice(options)
# random.shuffle(cards)

# -------------- NUMBER GUESSING GAME --------------

import random

low = 1
high = 100
guesses = 0
number = random.randint(low, high)

#while True:
 #  guess = int(input(f"Enter a number between ({low} - {high}): "))
  # guesses += 1

   ##   print(f"{guess} is too low")
   #elif guess > number:
    #   print(f"{guess} is too high")
   ##   print(f"{guess} is correct!")
     #  break

#print(f"This round took you {guesses} guesses")


#import random

#ptions = ("rock", "paper", "scissors")
#score=0
#running = True

#while running:

   # player = None
    #computer = random.choice(options)

    #while player not in options:
     #   player = input("Enter a choice (rock, paper, scissors): ")

    #print(f"Player: {player}")
    #print(f"Computer: {computer}")

    #if player == computer:
     #   print("It's a tie!")
    #elif player == "rock" and computer == "scissors":
      #  print("You win!")
     #   score+=1
    #elif player == "paper" and computer == "rock":
      #  print("You win!")
     #   score+=1
    #elif player == "scissors" and computer == "paper":
      #  print("You win!")
     #   score+=1
    #else:
   #     print("You lose!")

  #  if not input("Play again? (y/n): ").lower() == "y":
 #       running = False


#print("=============== ⭐⭐⭐ SCORE ⭐⭐⭐  ================")
#print(f"your score is={score}")
#print("Thanks for playing!")



########################################################################################################
import random
    
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# PRINT VERTICALLY
# for die in range(num_of_dice):
#    for line in dice_art.get(dice[die]):
#        print(line)

# PRINT HORIZONTALLY
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()

for die in dice:
    total += die
print(f"total: {total}")