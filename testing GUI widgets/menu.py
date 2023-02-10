from tkinter import *
App =Tk()

menu_ch = StringVar()
drop_options = ['Red', 'Yellow','Blue']
menu = OptionMenu(App, menu_ch, *drop_options)
menu.pack()
menu_ch.set('Red')
def show():
    msg = Label(App, text="              ", background=(menu_ch.get()).lower())
    msg.pack()

B = Button(App, text='show', command=show)
B.pack()
App.mainloop()