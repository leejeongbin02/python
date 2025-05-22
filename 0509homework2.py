import tkinter as tk
import random

window = tk.Tk()
window.title("Self Study 10-2")

filename_list = ["froyo.gif", "gingerbread.gif", "honeycomb.gif", "icecream.gif", "jellybean.gif", "kitkat.gif", "lollipop.gif", "marshmallow.gif", "nougat.gif"]

random.shuffle(filename_list)

photo_list = [tk.PhotoImage(file=name) for name in filename_list]

btn_list = [None] * 9

for i in range(3):
    for j in range(3):
        index = i * 3 + j
        btn_list[index] = tk.Button(window, image=photo_list[index])
        btn_list[index].grid(row=i, column=j)

window.mainloop()
