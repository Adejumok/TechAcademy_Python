import tkinter as tk

window = tk.Tk()
window.title('Obiligado!')
window.geometry("500x300")

l = tk.Label(window, bg='white', fg='black', width=20, text='Otigoke')
l.pack()


def print_selection(c):
    l.config(text='You have selected ' + c)


s = tk.Scale(window, label='Oya na', from_=10, to=10, orient=tk.HORIZONTAL, length=200, showvalue=0, tickinterval=2,
             resolution=0.01, command=print_selection)
s.pack()

window.mainloop()
