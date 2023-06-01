import tkinter as tk
from dice import Dice
from widget_styles import *

def main():
    window = tk.Tk()
    window.title("Empty Window")
    window.geometry("800x600")
    window.resizable(width=False, height=False)
    window.configure(bg="#202020")

    frame = tk.Frame(window, bg='white', padx=2, pady=2)
    frame.pack()

    roll = Dice.roll_stats()
    show = Dice.show_rolls(roll)

    def show_text():
        label.config(text=f"{show}")

    button = tk.Button(frame, text="Press Me", command=show_text, **button_style)
    button.pack()

    label = tk.Message(window, text="", **label_style)
    label.pack()

    window.mainloop()

main()