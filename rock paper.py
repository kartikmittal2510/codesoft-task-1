import tkinter as tk
import random

# Choices for the game
choices = ["Rock", "Paper", "Scissors"]

# Initialize scores
user_score = 0
computer_score = 0

# Main function to play the game
def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)
    
    # Determine the result
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        computer_score += 1

    # Update Labels
    user_choice_label.config(text=f"You chose: {user_choice}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result)
    score_label.config(text=f"Score: You {user_score} - {computer_score} Computer")

# Reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="You chose: ")
    computer_choice_label.config(text="Computer chose: ")
    result_label.config(text="")
    score_label.config(text="Score: You 0 - 0 Computer")

# Create main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x400")

# Title
tk.Label(root, text="Rock-Paper-Scissors", font=("Helvetica", 18, "bold")).pack(pady=10)

# Instruction
tk.Label(root, text="Choose your move:", font=("Helvetica", 12)).pack()

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

for choice in choices:
    tk.Button(button_frame, text=choice, width=10, command=lambda c=choice: play(c)).pack(side=tk.LEFT, padx=5)

# Display Area
user_choice_label = tk.Label(root, text="You chose: ", font=("Helvetica", 12))
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(root, text="Computer chose: ", font=("Helvetica", 12))
computer_choice_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score: You 0 - 0 Computer", font=("Helvetica", 12))
score_label.pack(pady=10)

# Play Again Button
tk.Button(root, text="Reset Game", command=reset_game).pack(pady=10)

root.mainloop()