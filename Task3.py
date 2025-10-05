import random

# Welcome message
print("Welcome to Rock, Paper, Scissors Game!")

# Score start me 0 rakhe
user_score = 0
computer_score = 0

while True:
    # User se choice lo
    user = input("\nEnter your choice (rock / paper / scissors): ").lower()

    # Computer random choice lega
    options = ["rock", "paper", "scissors"]
    computer = random.choice(options)

    print("You chose:", user)
    print("Computer chose:", computer)

    # Game ke rules check karo
    if user == computer:
        print("It's a Tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You Win!")
        user_score += 1
    elif user in options:
        print("You Lose!")
        computer_score += 1
    else:
        print("Invalid input! Please choose rock, paper, or scissors.")
        continue

    # Score dikhao
    print(f"Score -> You: {user_score} | Computer: {computer_score}")

    # Pooche ki dubara khelna hai kya
    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        print("\nThank you for playing! Goodbye!")
        break
