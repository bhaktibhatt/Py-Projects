from tkinter import *

App = Tk()
App.title('Icon Creator')
App.geometry('300x200')


def open_img():
    from PIL import Image
    from tkinter import filedialog
    global img

    App.img_dir = filedialog.askopenfilename(
        initialdir = 'B:', 
        title = 'Select an image', 
        filetypes = (('PNG Image','*.png'), ('JPG Image', '*.jpg'),('All Files', '*.*'))
        )

    img = Image(App.img_dir)

def convert_img():
    from PIL import Image

    img.save(f'{ico_name.get()}'.ico, format = 'ICO', sizes =[(ico_size.get(), ico_size.get())])

    success = Toplevel()
    success.title('Success')
    msg = Label(success, text='File conversion completed!')
    msg.pack()

    success.mainloop()

def preview():
    prev = Toplevel()
    prev.title('Ico Preview')
    prev.iconbitmap(f'{ico_name.get()}.ico')

    prev_label = Label(prev, text='Check the icon preview')
    prev_label.pack()
    prev.mainloop()

choose_img_lbl = Label(App, text='Select a image: ')
choose_img_lbl.grid(row=0,column=0)

choose_img_btn = Button(App, text='Select', command=open_img)
choose_img_btn.grid(row=0, column=2)

size_L = Label(App, text = 'Select icon size')
size_L.grid(row=1, column=0)

ico_size = IntVar()
size_opts = [16,24,32,48,64,128,256]
ico_size.set(32)
size_menu = OptionMenu(App, ico_size, *size_opts)
size_menu.grid(row =1, column=2)

fnameL = Label(App, text='Enter file name: ')
fnameL.grid(row=2, column=0)

ico_name = Entry(App)
ico_name.grid(row=2, column=2)

convert_btn = Button(App, text='Convert', command=convert_img)
convert_btn.grid(row=4, column=0)

prev_btn = Button(App,text='View Preview', command=preview)
prev_btn.grid(row=4, column=2)

App.mainloop()