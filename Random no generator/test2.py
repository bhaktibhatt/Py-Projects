from tkinter import *
from random import randint
App = Tk()
App.title('First GUI in py')
App.geometry('250x200')
Display = Label(App,text = 'Random Number Generator')
Display.pack()

def show_rand():
    msg = Label(App,text = randint(1,100))
    msg.pack()
    
B = Button(App,text = 'click',command=show_rand)
B.pack()
App.mainloop()