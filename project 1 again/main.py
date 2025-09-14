import random

def determine_winner(user_choice, computer_choice):
  outcomes = {
    ("water", "gun"): "You Win",
    ("gun", "snake"): "You Win",
    ("snake", "water"): "You Win",
    ("water", "snake"): "Computer Wins",
    ("gun", "water"): "Computer Wins",
    ("snake", "gun"): "Computer Wins",
  }

  if user_choice == computer_choice:
    return "It's a tie!"
  else:
    return outcomes.get((user_choice, computer_choice), "Invalid Input")
  
choices = ["snake", "water", "gun"]

score = {
  "user_score": 0,
  "computer_score": 0,
  "ties": 0,
}

print("Welcome to the Snake, Water, Gun Game.....")

rounds = int(input("How many rounds do you want to play? "))

for i in range(rounds):

  while True:
    print()
    print(f"Round {i+1}:-")
    user_choice = input("Enter your choice: ").lower()
    if user_choice in choices:
      break
    print("Invalid Choice, Please try again!")

  computer_choice = random.choice(choices)

  print(f"You chose {user_choice}")
  print(f"Computer chose {computer_choice}")
  result = determine_winner(user_choice, computer_choice)
  print(f"Result: {result}")
  
  if result == "You Win":
    score["user_score"] += 1
  elif result == "Computer Wins":
    score["computer_score"] += 1
  else:
    score["ties"] += 1

user_score = score['user_score']
computer_score = score['computer_score']
ties = score['ties']

print()
print("Final Result: ")
print(f"User_Score: {user_score}")
print(f"Computer_Score: {computer_score}")
print(f"Ties: {ties}")

if user_score > computer_score:
  print("You won the game!")
elif computer_score > user_score:
  print("Computer won the game!")
else:
  print("It's a tie overall!")