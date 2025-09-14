import tkinter as tk
import random

# Possible choices
choices = ["snake", "water", "gun"]

# Outcomes dictionary
outcomes = {
    ("water", "gun"): "You Win",
    ("gun", "snake"): "You Win",
    ("snake", "water"): "You Win",
    ("water", "snake"): "Computer Wins",
    ("gun", "water"): "Computer Wins",
    ("snake", "gun"): "Computer Wins",
}

# Scores
score = {
    "user": 0,
    "computer": 0,
    "ties": 0
}

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    return outcomes.get((user_choice, computer_choice), "Invalid Match")

def play(user_choice):
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)

    # Update scores
    if result == "You Win":
        score["user"] += 1
    elif result == "Computer Wins":
        score["computer"] += 1
    else:
        score["ties"] += 1

    # Update UI
    result_label.config(
        text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\nResult: {result}"
    )
    score_label.config(
        text=f"Your Score: {score['user']}   Computer Score: {score['computer']}   Ties: {score['ties']}"
    )

# GUI Setup
root = tk.Tk()
root.title("Snake Water Gun Game")
root.geometry("400x300")

title = tk.Label(root, text="Snake 🐍 Water 💧 Gun 🔫 Game", font=("Helvetica", 16))
title.pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Snake", width=10, command=lambda: play("snake")).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Water", width=10, command=lambda: play("water")).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Gun", width=10, command=lambda: play("gun")).grid(row=0, column=2, padx=5)

# Result display
result_label = tk.Label(root, text="", font=("Helvetica", 12), pady=10)
result_label.pack()

# Scoreboard
score_label = tk.Label(root, text="Your Score: 0   Computer Score: 0   Ties: 0", font=("Helvetica", 12))
score_label.pack()

root.mainloop()
