import tkinter as tk
from tkinter import messagebox

def keyEvent(event):
    shift_pressed = (event.state & 0x0001) != 0  # Shift 키 감지

    arrows = {
        37: "왼쪽 화살표",
        38: "위쪽 화살표",
        39: "오른쪽 화살표",
        40: "아래쪽 화살표"
    }

    if shift_pressed and event.keycode in arrows:
        msg = f"눌린 키 : Shift + {arrows[event.keycode]}"
        messagebox.showinfo("키보드 이벤트", msg)

window = tk.Tk()
window.title("Self Study 10-4")
window.geometry("300x100")

window.bind("<Key>", keyEvent)

window.mainloop()
