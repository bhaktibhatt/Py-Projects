from tkinter import *
from random import choice
App = Tk()
App.title('Random number Generator')
App.geometry('300x200')
inp = Entry(App)
inp.grid(row=0,column=0,columnspan=2, padx=20,pady=5)

def pick():
    INP =  (inp.get()).split(',')
    chosen = 'Generated : '+str(choice(INP))
    msg = Label(App, text=chosen)
    msg.grid(row=0, column=2, padx=20,pady=5)

B = Button(App, text='Choose', command=pick)
B.grid(row=2,column=0, padx=20,pady=5)
quitB = Button(App, text='Quit', command=App.quit)
quitB.grid(row=2, column=1)
App.mainloop()