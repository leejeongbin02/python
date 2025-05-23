from tkinter import *

window = Tk()

photo1 = PhotoImage(file="C:\\Users\\MYCOM\\Desktop\\파이썬프로그래밍\\실습 파일\\WindowProgramming\\cat.gif")
photo2 = PhotoImage(file="C:\\Users\\MYCOM\\Desktop\\파이썬프로그래밍\\실습 파일\\WindowProgramming\\cat2.gif")

label1 = Label(window, image=photo1)
label2 = Label(window, image=photo2)

label1.pack(side=LEFT)
label2.pack(side=LEFT)

window.mainloop()
