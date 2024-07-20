import random
import tkinter as tk

def roll_dice():
    result.set(random.randint(1, 6))

root = tk.Tk()
root.title("Dice Simulator")

result = tk.IntVar()
result.set(0)

label = tk.Label(root, text="Press the button to roll the dice!")
label.pack(pady=10)

result_label = tk.Label(root, textvariable=result, font=("Helvetica", 32))
result_label.pack(pady=10)

roll_button = tk.Button(root, text="Roll Dice", command=roll_dice)
roll_button.pack(pady=20)

root.mainloop()
