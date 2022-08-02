import random
#take the user input
user_action = input("Enter a choice (rock,paper,scissors:)")
possible_actions = ["rock","paper","scissors"]
#make the computer choose
computer_action = random.choice(possible_actions)
print(f"\n You chose {user_action}, computer chose {computer_action}.\n")
#determine a winner
if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "paper":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts the paper. You lose")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
    

    