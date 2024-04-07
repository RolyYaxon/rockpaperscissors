import random

def play(): 
    choices = {'p': 'Paper', 'r': 'Rock', 's': 'Scissors'}
    while True:
        try:
            user_choice = input("Enter your choice: 'p' for Paper, 'r' for Rock, 's' for Scissors: ")
            computer_choice = random.choice(list(choices.keys()))
            
            if user_choice not in choices:
                raise ValueError("Invalid choice. Please enter 'p' for Paper, 'r' for Rock, or 's' for Scissors.")

            result = determine_winner(user_choice, computer_choice)

            print(f"You chose {choices[user_choice]} and the computer selected {choices[computer_choice]} so {result}")
            break
        except ValueError as e:
            print(e)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 's' and computer_choice == 'p') or \
         (user_choice == 'p' and computer_choice == 'r'):
        return "you won"
    else:
        return "you lost"

play()
