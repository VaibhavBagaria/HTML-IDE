from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
import os
root = Tk()
root.minsize(600,300)
root.maxsize(800,500)
root.configure(bg="lightgrey")

open_file=ImageTk.PhotoImage(Image.open("open.png"))
save_file=ImageTk.PhotoImage(Image.open("save.png"))
play_file=ImageTk.PhotoImage(Image.open("play.png"))

label_file_name = Label(root, text="Name")
label_file_name.place(relx=0.3,rely=0.1,anchor= CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.5,rely=0.1, anchor= CENTER)

my_text= Text(root,height=20,width=70,bg="darkgrey",fg="white")
my_text.place(relx=0.5,rely=0.7,anchor= CENTER)

name=0
def file_open():
    global name
    my_text.delete(1.0,END)
    input_file_name.delete(0,END)
    textfile=filedialog.askopenfilename(title="Open Html File",filetype=(("Html Files","*.html"),))
    print(textfile)
    name=os.path.basename(textfile)
    print(name)
    formatted_name=name.split('.')[0]
    print(formatted_name)
    input_file_name.insert(END,formatted_name)
    root.title(formatted_name)
    read_file=open(textfile,'r')
    paragraph=read_file.read()
    my_text.insert(END,paragraph)
    read_file.close()
def file_save():
    user=0

def file_play():
    html_code=0
    #executed_text=my_text.get()
    #execution=str(executed_text)
    #exec(html_code)

open_button=Button(root,image=open_file, command=file_open)
open_button.place(relx=0.03,rely=0.1,anchor=W)
save_button=Button(root,image=save_file, command=file_save)
save_button.place(relx=0.11,rely=0.1,anchor= W)
play_button=Button(root,image=play_file, command=file_play)
play_button.place(relx=0.19,rely=0.1,anchor= W)

root.mainloop()

