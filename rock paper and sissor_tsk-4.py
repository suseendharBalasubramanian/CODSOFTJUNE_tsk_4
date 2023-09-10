import tkinter as tk
from tkinter import ttk
import random

# Function to get computer choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle user's choice and update the game
def play_game():
    user_choice = user_choice_var.get()
    computer_choice = get_computer_choice()

    user_choice_label.config(text=f"You chose: {user_choice}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=result)

    if 'You win' in result:
        user_score_var.set(user_score_var.get() + 1)
    elif 'Computer wins' in result:
        computer_score_var.set(computer_score_var.get() + 1)


# Function to reset the game
def reset_game():
    user_score_var.set(0)
    computer_score_var.set(0)
    user_choice_label.config(text="")
    computer_choice_label.config(text="")
    result_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

# Initialize scores
user_score_var = tk.IntVar()
computer_score_var = tk.IntVar()

# Create labels for scores
user_score_label = tk.Label(root, text="Your Score:")
user_score_label.grid(row=0, column=0)
user_score_display = tk.Label(root, textvariable=user_score_var)
user_score_display.grid(row=0, column=1)

computer_score_label = tk.Label(root, text="Computer Score:")
computer_score_label.grid(row=1, column=0)
computer_score_display = tk.Label(root, textvariable=computer_score_var)
computer_score_display.grid(row=1, column=1)

# Create labels for user and computer choices
user_choice_label = tk.Label(root, text="")
user_choice_label.grid(row=3, column=0, columnspan=2)

computer_choice_label = tk.Label(root, text="")
computer_choice_label.grid(row=4, column=0, columnspan=2)

# Create label for game result
result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2)

# Create a label and dropdown for user choice
user_choice_label = ttk.Label(root, text="Choose Rock, Paper, or Scissors:")
user_choice_label.grid(row=2, column=0, columnspan=2)

user_choice_var = tk.StringVar()
user_choice_var.set("rock")
user_choice_dropdown = ttk.Combobox(root, textvariable=user_choice_var, values=["rock", "paper", "scissors"])
user_choice_dropdown.grid(row=2, column=2)

# Create buttons to play and reset the game
play_button = ttk.Button(root, text="Play", command=play_game)
play_button.grid(row=3, column=2)

reset_button = ttk.Button(root, text="Reset", command=reset_game)
reset_button.grid(row=4, column=2)

# Start the GUI main loop
root.mainloop()
