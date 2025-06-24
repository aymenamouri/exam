import tkinter as tk
import random

# Main window setup
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("1360x768")
window.resizable(False, False)

# Create full-window canvas for gradient
canvas = tk.Canvas(window, width=1360, height=768, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Gradient colors
color1 = "blue"
color2 = "white"
color3 = "lightblue"
r1, g1, b1 = [c // 256 for c in window.winfo_rgb(color1)]
r2, g2, b2 = [c // 256 for c in window.winfo_rgb(color2)]
width = 1360

# Draw horizontal gradient
for i in range(width):
    nr = int(r1 + ((r2 - r1) * i / width))
    ng = int(g1 + ((g2 - g1) * i / width))
    nb = int(b1 + ((b2 - b1) * i / width))
    color = f"#{nr:02x}{ng:02x}{nb:02x}"
    canvas.create_line(i, 0, i, 768, fill=color)

# Variables
result_var = tk.StringVar()

# Function: Play
def play():
    choices = ["rock", "paper", "scissors"]
    comp_pick = random.choice(choices)
    user_pick = user_choice.get().lower()

    if user_pick not in choices:
        result_var.set("Invalid input! Choose rock, paper, or scissors.")
        return

    if user_pick == comp_pick:
        result = f"Draw! Both chose {comp_pick}."
    elif (user_pick == "rock" and comp_pick == "scissors") or \
         (user_pick == "scissors" and comp_pick == "paper") or \
         (user_pick == "paper" and comp_pick == "rock"):
        result = f"You win! Computer chose {comp_pick}."
    else:
        result = f"You lose! Computer chose {comp_pick}."

    result_var.set(result)

# Function: Reset
def Reset():
    user_choice.delete(0, tk.END)
    result_var.set("")

# Function: Exit
def Exit():
    window.destroy()

# Create all widgets
lbl_title = tk.Label(window, text="Rock, Paper, Scissors Game", font=("Good Times", 20),fg="black")
lbl_prompt = tk.Label(window, text="Choose Rock, Paper, or Scissors:", font=("Good Times", 14),fg="blue")
user_choice = tk.Entry(window, font=("Good Times", 14), justify='center')
result_entry = tk.Entry(window, font=("Good Times", 14), textvariable=result_var, justify='center', state='readonly')

btn_play = tk.Button(window, text="PLAY", font=("Good Times", 12), command=play)
btn_reset = tk.Button(window, text="RESET", font=("Good Times", 12), command=Reset)
btn_exit = tk.Button(window, text="EXIT", font=("Good Times", 12), command=Exit)

# Place widgets on canvas
canvas.create_window(680, 80, window=lbl_title)
canvas.create_window(680, 160, window=lbl_prompt)
canvas.create_window(680, 220, window=user_choice, width=300)
canvas.create_window(680, 280, window=result_entry, width=600)

canvas.create_window(680, 350, window=btn_play, width=100)
canvas.create_window(680, 400, window=btn_reset, width=100)
canvas.create_window(680, 450, window=btn_exit, width=100)

# Run the app
window.mainloop()
