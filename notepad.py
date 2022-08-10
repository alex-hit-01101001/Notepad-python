import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os

# Functions
def new():
    inpu1 = T.get("1.0", 'end-1c')
    if inpu1 != "" or saved != True:
        new_root = Tk()
        new_root.geometry("200x100")
        new_root.title("")
        label_ask = Label(new_root, text="are you sure ?")
        label_ask.pack(expand=True)
        button_yes = Button(new_root, text="yes")
        button_yes.pack(side="left")
        button_no = Button(new_root, text="no")
        button_no.pack(side="right")

def save():
    i = 0
    name = "untitled", i, ".txt"
    name = ''.join(name)
    try:
        text_file = open(name, "r")
        text_file.close()
    except FileNotFoundError:
        text_file = open(name, "w")
        inpu = T.get("1.0", 'end-1c')
        text_file.write(inpu)

def save_as():
    directory = os.getcwd()
    filename = filedialog.asksaveasfilename(initialdir= directory, title="Select a File",
                                          filetypes=(("Text files", "*.txt*"), ("all files", "*.*")),
                                          initialfile = "Untitled")
    print(os.path.dirname(filename))
    try:
        text_file = open(filename, "r")
        text_file.close()
    except FileNotFoundError:
        text_file = open(filename, "w")
        inpu = T.get("1.0", 'end-1c')
        text_file.write(inpu)

def open1():
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                          filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
    text_file = open(filename, "r")
    content = text_file.read()
    text_file.close()
    T.clipboard_clear()
    T.insert(INSERT, content)
    
    
# Main
root = Tk()
root.geometry("800x600")
root.title("Notepad")
saved = False
S = tk.Scrollbar(root)
T = tk.Text(root, height=4, width=50)
S.pack(side=tk.RIGHT, fill=tk.Y)
T.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)

# TOP BAR MENU
menu1 = Menu(root)
root.config(menu=menu1)
# NEW
File_menu = Menu(menu1)
menu1.add_cascade(label="File", menu=File_menu)
File_menu.add_command(label="New", command=new)
File_menu.add_command(label="Open", command=open1)
File_menu.add_command(label="Save", command=save)
File_menu.add_command(label="Save as", command=save_as)
# EDIT
Edit_menu = Menu(menu1)
menu1.add_cascade(label="Edit", menu=Edit_menu)
Edit_menu.add_command(label="Preferences", command="")
# SETTINGS
Settings_menu = Menu(menu1)
menu1.add_cascade(label="Settings", menu=Settings_menu)
Settings_menu.add_command(label="Preferences", command="")
# HELP
help_menu = Menu(menu1)
menu1.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command="")

tk.mainloop()