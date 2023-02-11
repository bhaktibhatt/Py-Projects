from tkinter import *
die = {
    0 : '🎲',
1 : '⚀',
2 : '⚁',
3 : '⚂',
4 : '⚃', 
5 : '⚄',
6 : '⚅'
}

App = Tk()
App.geometry('300x300')
App.title('Dice Roller')

dice = Label(App, text=die[0], font=('Times', 100), foreground = '#845EC2',background='#B0A8B9', width=3, justify=CENTER)
dice.grid(row = 0, column=0, padx=25, pady=5)

def roll():
    from random import randint
    i = randint(1,6)
    show_die = Label(App, text=die[i], font=('Times', 100), foreground = '#845EC2',background='#B0A8B9', width=3, justify=CENTER)
    show_die.grid(row = 0, column=0, padx=25, pady=5)

roll_btn = Button(App, text='Roll dice', command=roll, background='#4E8397', foreground='#D5CABD')
roll_btn.grid(row =1, column=0)
App.configure(bg='#B0A8B9')
App.mainloop()