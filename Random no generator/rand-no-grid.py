from tkinter import *
from random import sample,choice #choses randomly 
App = Tk()
App.title('Random number Generator')
App.geometry('300x200')

inp = Entry(App)#entry field widget
inp.grid(row=0,column=0,columnspan=2, padx=20,pady=5)

no_choice = IntVar()
chk = Checkbutton(App, text='2 choices', variable=no_choice, onvalue=2, offvalue=1)
chk.grid(row=0, column=2, padx=20,pady=5)

def pick():
    INP =  (inp.get()).split(',')

    if no_choice.get() == 2:
        ele = sample(INP,2)
        chosen = 'Generated : '+ str(ele[0]) + ' ' + str(ele[1])
    else:
        chosen = 'Generated : '+str(choice(INP))

    msg = Label(App, text=chosen,width=20,relief='groove')
    msg.grid(row=3, column=0, columnspan=2, padx=25,pady=5)

    if quitB['state'] == DISABLED: #uses global func state key 
        quitB['state'] = NORMAL

B = Button(App, text='Choose', command=pick,background='green')
B.grid(row=2,column=0, padx=20,pady=5)

quitB = Button(App, text='Quit', command=App.quit, state=DISABLED,background='red')
quitB.grid(row=2, column=1)

App.configure(bg='#969a97')
App.mainloop()