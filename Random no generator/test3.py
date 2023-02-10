from tkinter import *
# learnt how to use check box 
App = Tk()
check = StringVar() #holder for int vals
chk = Checkbutton(App,text='Check Box',variable=check, onvalue='Yes', offvalue='No')
chk.deselect()
chk.pack()

def show():
    msg = Label(App,text='status : '+str(check.get()))
    msg.pack()

btn = Button(App,text='check status', command=show)
btn.pack()
App.mainloop()