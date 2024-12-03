import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        user_input = input("Type 'roll' to roll the dice or 'exit' to quit: ").lower()
        if user_input == 'roll':
            print(f"You rolled a {roll_dice()}!")
        elif user_input == 'exit':
            print("Thank you!")
            break
        else:
            print("Invalid input. Please type 'roll' or 'exit'.")

if __name__ == "__main__":
    main()
