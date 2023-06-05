import tkinter as tk
from dice import Dice
from widget_styles import *


def main():
    window = tk.Tk()
    window.title("Empty Window")
    window.geometry("800x600")
    window.resizable(width=False, height=False)
    window.configure(bg="#202020")

    # TODO: create function that wraps button in frame. Alternatively create custom button.
    f1 = tk.Frame(window, bg="white", padx=2, pady=2)
    f2 = tk.Frame(window, bg="white", padx=2, pady=2)
    f3 = tk.Frame(window, bg="white", padx=2, pady=2)
    f1.pack()
    f2.pack()
    f3.pack()

    roll = Dice.roll(6)
    ss = Dice.show_single(roll)

    stats = Dice.roll_stats()
    sr = Dice.show_rolls(stats)

    def show_text():
        msg1.config(text=f"{ss}")
        msg2.config(text=f"{sr}")

    button = tk.Button(f1, text="Press Me", command=show_text, **button_style)
    button.pack()

    msg1 = tk.Message(f2, text="", width=200, **message_style)
    msg2 = tk.Message(f3, text="", width=200, **message_style)
    msg1.pack()
    msg2.pack()

    window.mainloop()


main()
