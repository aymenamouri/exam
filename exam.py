import tkinter as tk
import random


window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("1360x768")
window.resizable(False, False)


window.configure(bg="blue")


lbl_title = tk.Label(window, text="Rock, Paper, Scissors Game", font=("Good Times", 10), bg="white", fg="black")
lbl_title.pack(pady=10)

lbl_prompt = tk.Label(window, text="Choose Rock, Paper, or Scissors:", font=("Good Times", 10), bg="white", fg="black")
lbl_prompt.pack()


user_choice = tk.Entry(window, font=("Good Times", 10), justify='center')
user_choice.pack(pady=5)


lbl_result = tk.Label(window, text="", font=("Good Times", 10), bg="white", fg="black")
lbl_result.pack(pady=20)


def play_game():
    choices = ["rock", "paper", "scissors"]
    comp_pick = random.choice(choices)
    user_pick = user_choice.get().lower()

    if user_pick not in choices:
        lbl_result["text"] = "Invalid input! Choose rock, paper, or scissors."
        return

    result = ""
    if user_pick == comp_pick:
        result = f"Draw! Both chose {comp_pick}."
    elif (user_pick == "rock" and comp_pick == "scissors") or \
         (user_pick == "scissors" and comp_pick == "paper") or \
         (user_pick == "paper" and comp_pick == "rock"):
        result = f"You win! Computer chose {comp_pick}."
    else:
        result = f"You lose! Computer chose {comp_pick}."

    lbl_result["text"] = result


btn_play = tk.Button(window, text="Play", font=("Good Times", 12), command=play_game)
btn_play.pack()


window.mainloop()
