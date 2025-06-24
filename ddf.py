import tkinter as tk
import random

# Main window setup
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("1360x768")
window.resizable(False, False)
window.configure(bg="blue")

# Title label
lbl_title = tk.Label(window, text="Rock, Paper, Scissors Game", font=("Good Times", 16), bg="white", fg="black")
lbl_title.pack(pady=10)

# Prompt label
lbl_prompt = tk.Label(window, text="Choose Rock, Paper, or Scissors:", font=("Good Times", 12), bg="white", fg="black")
lbl_prompt.pack()

# User input
user_choice = tk.Entry(window, font=("Good Times", 12), justify='center')
user_choice.pack(pady=5)

# Result label
lbl_result = tk.Label(window, text="", font=("Good Times", 12), bg="white", fg="black")
lbl_result.pack(pady=20)

# Function 1: Play
def play():
    choices = ["rock", "paper", "scissors"]
    comp_pick = random.choice(choices)
    user_pick = user_choice.get().lower()

    if user_pick not in choices:
        lbl_result["text"] = "Invalid input! Choose rock, paper, or scissors."
        return

    if user_pick == comp_pick:
        result = f"Draw! Both chose {comp_pick}."
    elif (user_pick == "rock" and comp_pick == "scissors") or \
         (user_pick == "scissors" and comp_pick == "paper") or \
         (user_pick == "paper" and comp_pick == "rock"):
        result = f"You win! Computer chose {comp_pick}."
    else:
        result = f"You lose! Computer chose {comp_pick}."

    lbl_result["text"] = result

# Function 2: Reset
def Reset():
    user_choice.delete(0, tk.END)
    lbl_result.config(text="")

# Function 3: Exit
def Exit():
    window.destroy()

# Buttons
btn_play = tk.Button(window, text="Play", font=("Good Times", 12), command=play)
btn_play.pack(pady=5)

btn_reset = tk.Button(window, text="Reset", font=("Good Times", 12), command=Reset)
btn_reset.pack(pady=5)

btn_exit = tk.Button(window, text="Exit", font=("Good Times", 12), command=Exit)
btn_exit.pack(pady=5)

# Start the application
window.mainloop()
