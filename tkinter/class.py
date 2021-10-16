import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox as msg
import sys

screen = tk.Tk()
screen.geometry('500x500')
screen.title('Program')

img = Image.open('license.jpg')
photo = ImageTk.PhotoImage(img)

def greet():
    print("Hello World")

button = tk.Button(text='Submit', fg='red', command=greet)
#######
radio_buttonF = tk.Radiobutton(text="Female")
radio_buttonM = tk.Radiobutton(text="Male")
#######
spinbox = tk.Spinbox(from_=1, to=10)
#######
entry = tk.Entry().pack()
frame = tk.Frame(screen, bg='blue', bd=5).place(relx=0.5,
                                                rely=0.5,
                                                relheight=0.1,
                                                anchor='n')
#entry.place(relwidth=0.65, relheight=1)
########
menubar = tk.Menu(screen)
fileMenu = tk.Menu(menubar, tearoff=0)
fileMenu.add_command(label='New')
fileMenu.add_command(label='Save')
fileMenu.add_command(label='Open')
fileMenu.add_separator() # add separate at drop down menu
fileMenu.add_command(label='Exit', command=screen.quit)
menubar.add_cascade(label='File', menu=fileMenu)
helpMenu = tk.Menu(menubar, tearoff=0)
helpMenu.add_command(label = 'Check for Updates')
helpMenu.add_command(label = 'About')
menubar.add_cascade(label='Help', menu=helpMenu)
screen.config(menu=menubar)
########
def hello():
    #showinfo showwarning showerror askquestion askokcancel askyesno askretrycancel
    status = msg.askyesno('Say Hello', 'ต้องการปิดโปรแกรมไหม')
    if status == True:
        sys.exit()
    else:
        print('Press No')
messagebox = tk.Button(screen, text='Say Hello', command=hello).pack()
########
picture = tk.Label(image=photo)
picture.image = photo
picture.place(x=20, y=20)
########
text = tk.Label(text="Hello World!",
                fg='red',
                bg='blue')
########
scale = tk.Scale(screen, from_=0, to=42).pack()
scale = tk.Scale(screen, from_=0, to=200, orient=tk.HORIZONTAL).pack()
#######
radio_buttonM.pack()
radio_buttonF.pack()
spinbox.pack()
picture.pack()
text.pack(ipadx=50, ipady=50, side='bottom')
screen.mainloop()
