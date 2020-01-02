import tkinter as  tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

canvas = tk.Canvas(root, height=500, width=700, bg="black")
canvas.pack()

frame = tk.Frame(root, bg="#CCCCCC")
frame.place(relwidth=0.984, relheight=0.98, relx=0.008, rely=0.01)

button = tk.Button(root, text="Button press", padx=10, pady=10, fg="white", bg="Blue")
#button.pack()
button.place(relx=0.50, rely=0.50)

root.mainloop()