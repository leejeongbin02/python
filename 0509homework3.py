import tkinter as tk

fnameList = ["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif", "jeju5.gif", "jeju6.gif", "jeju7.gif", "jeju8.gif", "jeju9.gif"]

photoList = [tk.PhotoImage(file=fname) for fname in fnameList]

num = 0

def clickNext():
    global num
    num = (num + 1) % len(fnameList)
    pLabel.configure(image=photoList[num])
    nameLabel.configure(text=fnameList[num])  

def clickPrev():
    global num
    num = (num - 1) % len(fnameList)
    pLabel.configure(image=photoList[num])
    nameLabel.configure(text=fnameList[num])  

window = tk.Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

pLabel = tk.Label(window, image=photoList[num])
pLabel.place(x=15, y=50)

nameLabel = tk.Label(window, text=fnameList[num], font=("Arial", 14))
nameLabel.place(x=300, y=10)

btnPrev = tk.Button(window, text="<< 이전", command=clickPrev)
btnNext = tk.Button(window, text="다음 >>", command=clickNext)
btnPrev.place(x=150, y=10)
btnNext.place(x=450, y=10)

window.mainloop()
