from tkinter import *


def say_hi():
    print("hello~!")


root = Tk()
frame_1 = Frame(root)
frame_2 = Frame(root)
root.title("tkinter frame")
label = Label(frame_1, text="Greeting", justify=LEFT)
label.pack(side=LEFT)
hi_there = Button(frame_2, text="say hi~", command=say_hi)
hi_there.pack()
frame_1.pack(padx=1, pady=1)
frame_2.pack(padx=10, pady=10)
root.mainloop()
