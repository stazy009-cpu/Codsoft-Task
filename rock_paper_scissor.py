import random

# List of choices
choices = ["rock", "paper", "scissors"]

print("=== Rock Paper Scissors Game ===")

while True:
    user = input("Enter Rock, Paper, or Scissors: ").lower()

    if user not in choices:
        print("Invalid choice! Please try again.")
        continue

    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a Tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("Congratulations! You Win!")

    else:
        print("Computer Wins!")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thank you for playing!")
        break