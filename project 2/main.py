import random
rand_num = random.randint(0, 100)

attempts = 1

while True:
  user_guess = int(input("Guess the correct number: "))

  if user_guess > rand_num:
    print("Lower number please.")
  elif user_guess < rand_num:
    print("Higher number please.")
  else:
    print(f"You guessed the correct number {rand_num} in {attempts} attempts.")
    break
  attempts += 1