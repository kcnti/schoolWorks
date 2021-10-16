import tkinter as tk
import tkinter.messagebox as msg

string = ''
screen = tk.Tk()
screen.geometry('400x270')

def backspace(field):
    global string
    string = ''.join(string[:-1])
    field.set(string)
def input_num(num, field):
    global string
    string = string + str(num)
    field.set(string)
def clear_input():
    global string
    string = ""
    field.set("")
def answer(field):
    global string
    try:
        result = str(float((eval(string))))
        field.set(result)
    except:
        msg.showerror("Error", "Something Wrong!")
def button():
