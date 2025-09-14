import random

def determine_winner(user_choice, computer_choice):
  outcomes = {
    ("water", "gun"): "You win",
    ("gun", "snake"): "You win",
    ("snake", "water"): "You win",
    ("gun", "water"): "Computer wins",
    ("snake", "gun"): "Computer wins",
    ("water", "snake"): "Computer wins",
  }
  if user_choice == computer_choice:
    return "It's a tie!"
  return outcomes.get((user_choice, computer_choice), "Invalid Match!")

choices = ["snake", "water", "gun"]
score_user = 0
score_comp = 0

print("Welcome to Snake Water Gun Game!")
rounds = int(input("How many rounds do you want to play? "))

for i in range(rounds):
  print(f"\nRound {i+1}")
  user_choice = input("Choose snake, water or gun: ")
  if user_choice not in choices:
    print("Invalid choice, please try again.")
    continue
  computer_choice = random.choice(choices)
  print(f"\nComputer chose {computer_choice}")

  result = determine_winner(user_choice, computer_choice)
  print(result)

  if "You win" in result:
    score_user += 1
  elif "Computer wins" in result:
    score_comp += 1

print("\nGame Over!")
print(f"You scored {score_user}")
print(f"Computer scored {score_comp}")

if score_user > score_comp:
  print("You won the game!")
elif score_user < score_comp:
  print("Computer won the game!")
else:
  print("It's a draw!")