# Exercise 4 — Rock, Paper, Scissors (vs. Computer)

player = input("Enter your choice (rock / paper / scissors): ").lower()
computer = "rock"

print(f"Computer chose: {computer}")

if player == computer:
    print("It's a tie!")
elif (player == "paper" and computer == "rock") or \
     (player == "scissors" and computer == "paper") or \
     (player == "rock" and computer == "scissors"):
    print("You win!")
elif player in ["rock", "paper", "scissors"]:
    print("Computer wins!")
else:
    print("Invalid choice. Please enter rock, paper, or scissors.")
