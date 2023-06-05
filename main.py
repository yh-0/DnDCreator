import tkinter as tk
from Classes.dice import Dice
from Classes.character import Character
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
    f1.pack()
    f2.pack()

    character = Character()

    def show_text():
        msg1.config(text=f"{character}")

    button = tk.Button(f1, text="Press Me", command=show_text, **button_style)
    button.pack()

    msg1 = tk.Message(f2, text="", width=300, **message_style)
    msg1.pack()

    window.mainloop()


main()
