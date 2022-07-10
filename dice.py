import random
from tkinter import *
root=Tk()
root.geometry("700x450")
l=Label(root, font=("times",200))
def roll():
 number=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
 l.config(text=f'{random.choice(number)}{random.choice(number)}')
 l.pack()
b=Button(root, text="press me", command=roll)
b.place(x=330,y=0)

root.mainloop()