############ step 1 ####################
#sum_even=0
#sum_odd=0
#total=0
#card_number=input("enter your card number:")
#card_number=card_number.replace("-","")
#ard_number=card_number.replace(" ","")
#card_number=card_number[::-1]
############ step 2 #####################
#for x in card_number[ : :2]:
#    sum_odd+=int(x)
############ step 3 #####################
#for x in card_number[1: :2]:
   # x=int(x*2)
   # if x>10:
   #     sum_even+=(1+(x%10))
 #   else:
  #      sum_even+=x
############ step 4 #####################
#total =sum_even + sum_odd
############ step 5 #####################
#if total%10==0:
 #   print(f"valid card number{card_number}")
#else:
   # print(f"no data found for this card number{card_number}")
#sum_odd_digits = 0
#sum_even_digits = 0
#total = 0

# Step 1
#card_number = input("Enter a credit card #: ")
#card_number = card_number.replace("-", "")
#card_number = card_number.replace(" ", "")
#card_number = card_number[::-1]

# Step 2
#for x in card_number[::2]:
 #   sum_odd_digits += int(x)

# Step 3
#for x in card_number[1::2]:
   # x = int(x) * 2
   # if x >= 10:
   #     sum_even_digits += (1 + (x % 10))
  #  else:
 #       sum_even_digits += x

# Step 4
#total = sum_odd_digits + sum_even_digits

# Step 5
#if total % 10 == 0:
 #   print("VALID")
#else:
#    print("INVALID")
####################################################################
########################## MINI BANk ###############################
# Python Banking Program

def show_balance(balance):
    print("*********************")
    print(f"Your balance is ${balance:.2f}")
    print("*********************")

def deposit():
    print("*********************")
    amount = float(input("Enter an amount to be deposited: "))
    print("*********************")
    if amount < 0:
        print("*********************")
        print("That's not a valid amount")
        print("*********************")
        return 0
    else:
        return amount

def withdraw(balance):
    print("*********************")
    amount = float(input("Enter amount to be withdrawn: "))
    print("*********************")

    if amount > balance:
        print("*********************")
        print("Insufficient funds")
        print("*********************")
        return 0
    elif amount < 0:
        print("*********************")
        print("Amount must be greater than 0")
        print("*********************")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("*********************")
        print("   Banking Program   ")
        print("*********************")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("*********************")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("*********************")
            print("That is not a valid choice")
            print("*********************")

    print("*********************")
    print("Thank you! Have a nice day!")
    print("*********************")

if __name__ == '__main__':
    main()

###########################################################################
###########################################################################
import random

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("**************")
    print(" | ".join(row))
    print("**************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0

def main():
    balance = 100

    print("*************************")
    print("Welcome to Python Slots ")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("*************************")

    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lost this round")

        balance += payout

        play_again = input("Do you want to spin again? (Y/N): ").upper()

        if play_again != 'Y':
            break

    print("*******************************************")
    print(f"Game over! Your final balance is ${balance}")
    print("*******************************************")

if __name__ == '__main__':
    main()


