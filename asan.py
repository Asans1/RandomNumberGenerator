import tkinter as tk 
import random

window = tk.Tk()
window.geometry("300x200")
window.title("Random number generator")

secret = random.randint(1,100)
attempts_left = 7

def guess():
    pass

entry = tk.Entry(window)
entry.pack(pady=10)

result = tk.Label(window, text="")
result.pack(pady=10)

button = tk.Button(window,text="нажми сюда",command=guess)
button.pack(pady=10)

window.mainloop()
