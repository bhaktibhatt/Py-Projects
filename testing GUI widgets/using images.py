from tkinter import *
from PIL import Image, ImageTk
App = Tk()
App.iconbitmap(r'B:\Projects\Python GUI projects\essentials\test_python_icon.ico')
img = ImageTk.PhotoImage(Image.open(r'B:\Projects\Python GUI projects\essentials\Trivia_Love_Poster.jpg'))
img_disp = Label(App, image=img)
img_disp.pack()
App.mainloop()