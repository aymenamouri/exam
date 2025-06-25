import random
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import StringVar, Canvas

# Theme state
current_theme = "flatly"

# Create main window
window = tb.Window(themename=current_theme)
window.title("Rock Paper Scissors — Emoji Style")
window.geometry("700x550")
window.resizable(False, False)

# Game variables
choices = ["rock", "paper", "scissors"]
result_var = StringVar()
comp_thinking_var = StringVar(value="Computer is thinking...")
player_score_var = StringVar(value="Player: 0")
computer_score_var = StringVar(value="Computer: 0")
player_score = 0
computer_score = 0
animation_counter = 0
animation_max = 15
animation_job = None
user_pick = None

# Flash window background
def flash_background(color):
    original = window.cget("background")
    window.configure(background=color)
    window.after(800, lambda: window.configure(background=original))

# Show result
def show_result():
    global player_score, computer_score, user_pick
    comp_pick = random.choice(choices)
    comp_thinking_var.set(f"Computer chose: {comp_pick.capitalize()}")
    if user_pick == comp_pick:
        result_var.set(f"Draw! Both chose {comp_pick}.")
    elif (user_pick == "rock" and comp_pick == "scissors") or \
         (user_pick == "scissors" and comp_pick == "paper") or \
         (user_pick == "paper" and comp_pick == "rock"):
        result_var.set(f"You win! Computer chose {comp_pick}.")
        player_score += 1
        player_score_var.set(f"Player: {player_score}")
        flash_background("lightgreen")
    else:
        result_var.set(f"You lose! Computer chose {comp_pick}.")
        computer_score += 1
        computer_score_var.set(f"Computer: {computer_score}")
        flash_background("lightcoral")

# Animate thinking
def animate_choice():
    global animation_counter, animation_job
    current_choice = choices[animation_counter % 3]
    comp_thinking_var.set(f"Computer is choosing: {current_choice.capitalize()}")
    animation_counter += 1
    if animation_counter < animation_max:
        animation_job = window.after(100, animate_choice)
    else:
        show_result()

# Play
def play(choice):
    global user_pick, animation_counter, animation_job
    user_pick = choice
    result_var.set("")
    animation_counter = 0
    if animation_job:
        window.after_cancel(animation_job)
    animate_choice()

# Reset game
def reset():
    global player_score, computer_score
    result_var.set("")
    comp_thinking_var.set("Computer is thinking...")
    player_score = 0
    computer_score = 0
    player_score_var.set("Player: 0")
    computer_score_var.set("Computer: 0")

# Exit app
def exit_game():
    window.destroy()

# ---------------------------
# Custom iOS-Style Theme Switch
# ---------------------------
class ThemeSwitch(Canvas):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, width=60, height=30, highlightthickness=0, bg=window.cget("background"))
        self.slider = self.create_oval(3, 3, 27, 27, fill="#FFD700", outline="")
        self.sun = self.create_text(45, 15, text="🌞", font=("Arial", 10))
        self.moon = self.create_text(15, 15, text="🌙", font=("Arial", 10))
        self.bind("<Button-1>", self.toggle)
        self.position = "right"  # Light mode start

    def toggle(self, event=None):
        global current_theme
        if self.position == "right":
            self.animate_to("left")
            window.style.theme_use("darkly")
            current_theme = "darkly"
            self.position = "left"
        else:
            self.animate_to("right")
            window.style.theme_use("flatly")
            current_theme = "flatly"
            self.position = "right"

    def animate_to(self, target):
        start = 3 if target == "right" else 30
        end = 30 if target == "right" else 3
        step = 1 if end > start else -1
        for i in range(start, end + step, step):
            self.coords(self.slider, i, 3, i + 24, 27)
            self.update()
            self.after(5)

# ---------------------------
# UI Layout
# ---------------------------
frame = tb.Frame(window, padding=30)
frame.place(relx=0.5, rely=0.5, anchor="center")

lbl_title = tb.Label(frame, text="🖥️ Rock, Paper, Scissors", font=("Helvetica Neue", 26, "bold"))
lbl_prompt = tb.Label(frame, text="Choose your move:", font=("Helvetica Neue", 13))

# Buttons
icon_frame = tb.Frame(frame)
btn_rock = tb.Button(icon_frame, text="🪨 Rock", command=lambda: play("rock"), bootstyle="outline-dark", width=14)
btn_paper = tb.Button(icon_frame, text="📄 Paper", command=lambda: play("paper"), bootstyle="outline-dark", width=14)
btn_scissors = tb.Button(icon_frame, text="✂️ Scissors", command=lambda: play("scissors"), bootstyle="outline-dark", width=14)
btn_rock.pack(side="left", padx=5)
btn_paper.pack(side="left", padx=5)
btn_scissors.pack(side="left", padx=5)

# Result area
comp_label = tb.Label(frame, textvariable=comp_thinking_var, font=("Helvetica Neue", 13), bootstyle="secondary")
result_entry = tb.Entry(frame, textvariable=result_var, font=("Helvetica Neue", 14),
                        bootstyle="light", width=45, state="readonly")

# Score area
score_frame = tb.Frame(frame)
score_player = tb.Label(score_frame, textvariable=player_score_var, font=("Helvetica Neue", 12), bootstyle="success")
score_computer = tb.Label(score_frame, textvariable=computer_score_var, font=("Helvetica Neue", 12), bootstyle="danger")
score_player.pack(side="left", padx=10)
score_computer.pack(side="right", padx=10)

# Control buttons
btn_frame = tb.Frame(frame, padding=(0, 10))
btn_reset = tb.Button(btn_frame, text="↻ Reset", command=reset, bootstyle="outline-dark", width=14)
btn_exit = tb.Button(btn_frame, text="⏹ Exit", command=exit_game, bootstyle="outline-dark", width=14)
switch = ThemeSwitch(btn_frame)

btn_reset.pack(side="left", padx=7)
btn_exit.pack(side="left", padx=7)
switch.pack(side="left", padx=12)

# Layout pack
lbl_title.pack(pady=(0, 20))
lbl_prompt.pack(pady=5)
icon_frame.pack(pady=10)
comp_label.pack(pady=5)
result_entry.pack(pady=10, ipady=6)
score_frame.pack(pady=8)
btn_frame.pack(pady=25)

# Footer
footer = tb.Label(window, text="Powered by Aymen and khalil", font=("Helvetica Neue", 10), bootstyle="secondary")
footer.pack(side="bottom", pady=10)

# Start app
window.mainloop()
