from tkinter import *
App = Tk()
choice = StringVar()
r1 = Radiobutton(App, text='Option 1', variable=choice, value='R1 selected')
r2 = Radiobutton(App, text='Option 2',variable=choice, value='R2 selected')
r1.deselect()
r2.deselect()
r1.pack()
r2.pack()

App.mainloop()