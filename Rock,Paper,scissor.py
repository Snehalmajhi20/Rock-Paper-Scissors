import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, window):
        self.window = window
        self.window.title("Rock Paper Scissors Game")
        self.window.geometry("400x200")
        self.window.configure(bg="lightblue")

        self.player_choice = tk.StringVar()
        self.computer_choice = tk.StringVar()

        self.label = tk.Label(self.window, text="Rock, Paper, Scissors", font=("Helvetica", 16), bg="lightblue")
        self.label.pack(pady=10)

        self.player_frame = tk.Frame(self.window, bg="lightblue")
        self.player_frame.pack()

        tk.Label(self.player_frame, text="Your Choice:", font=("Helvetica", 12), bg="lightblue").grid(row=0, column=0)
        tk.Button(self.player_frame, text="Rock", command=lambda: self.make_choice("Rock")).grid(row=0, column=1)
        tk.Button(self.player_frame, text="Paper", command=lambda: self.make_choice("Paper")).grid(row=0, column=2)
        tk.Button(self.player_frame, text="Scissors", command=lambda: self.make_choice("Scissors")).grid(row=0, column=3)

        self.result_label = tk.Label(self.window, text="", font=("Helvetica", 14), bg="lightblue")
        self.result_label.pack(pady=10)

    def make_choice(self, player_choice):
        self.player_choice.set(player_choice)

        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)
        self.computer_choice.set(computer_choice)

        result = self.determine_winner(player_choice, computer_choice)
        self.display_result(result)

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "It's a tie!"
        elif (
            (player_choice == "Rock" and computer_choice == "Scissors") or
            (player_choice == "Paper" and computer_choice == "Rock") or
            (player_choice == "Scissors" and computer_choice == "Paper")
        ):
            return "You win!"
        else:
            return "Computer wins!"

    def display_result(self, result):
        self.result_label.config(text=result)
        messagebox.showinfo("Result", result)

if __name__ == "__main__":
    window = tk.Tk()
    rps_game = RockPaperScissorsGame(window)
    window.mainloop()
