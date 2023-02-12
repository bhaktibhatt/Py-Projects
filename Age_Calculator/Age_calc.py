from tkinter import *
from datetime import datetime
App = Tk()
App.title('Age Calculator')

bg = 'black'
fg = 'green'
App['background'] = bg

msg = Label(text='Enter your DOB',background=bg, foreground=fg)
msg.grid(row = 0, column= 0, columnspan=3)

dayL = Label(App, text='Day: ',pady=2,background=bg, foreground=fg)
dayE = Entry(App, width=2,background=bg, foreground=fg,insertbackground='green')

monthL = Label(App, text='Month: ',pady=2,background=bg, foreground=fg)
monthE = Entry(App, width=2,background=bg, foreground=fg,insertbackground='green')

yearL = Label(App, text='Year: ',pady=2,background=bg, foreground=fg)
yearE = Entry(App, width=4,background=bg, foreground=fg,insertbackground='green')

dayL.grid(row = 1, column = 0,)
dayE.grid(row = 1, column = 1)
monthL.grid(row = 1, column = 2)
monthE.grid(row = 1, column = 3)
yearL.grid(row = 1, column = 4)
yearE.grid(row = 1, column = 5)

def find_days_lived():
    date = int(dayE.get())
    mon = int(monthE.get())
    year = int(yearE.get())
    dob = datetime(day=date, month=mon, year=year)

    time_now = datetime.now()
    time_lived = time_now - dob

    days_lived = Label(App, text='You have lived '+str(time_lived.days)+' days!',padx=20,pady=5,background=bg, foreground=fg)
    days_lived.grid(row = 4, column=0, columnspan=4)
    

def find_sec_lived():
    date = int(dayE.get())
    mon = int(monthE.get())
    year = int(yearE.get())
    dob = datetime(day=date, month=mon, year=year)
    time_now = datetime.now()
    time_lived = time_now - dob

    seconds = Label(App, text='You have lived '+str(time_lived.seconds)+' seconds!',pady=2,background=bg, foreground=fg)
    seconds.grid(row = 5, column=0, columnspan=4)



b_days = Button(App, text='Total days', command=find_days_lived,background=bg, foreground=fg)
b_days.grid(row=3, column=0,columnspan=3)

b_seconds = Button(App, text='Total seconds', command=find_sec_lived,background=bg, foreground=fg)
b_seconds.grid(row=3, column=5, columnspan=5)


App.mainloop()
