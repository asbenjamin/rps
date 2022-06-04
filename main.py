import random

while True:   

    user_action = input("Enter a choice (R for rock, P for paper, S for scissors): ")

    possible_actions = ["R", "P", "S"]
    computer_action = random.choice(possible_actions)

    if user_action.upper() == "R" or user_action.upper() == "P" or user_action.upper() == "S":

        print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

        if user_action.upper() == computer_action:
            print(f"Both players selected {user_action}. It's a tie!")
        elif user_action.upper() == "R":
            if computer_action == "S":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif user_action.upper() == "P":
            if computer_action == "R":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif user_action.upper() == "S":
            if computer_action == "P":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")

        break

    else:
        print("Oops, Wrong Input, try again, type either R, P or S")
