from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
from typing import Sized

file_path = ''


def set_file_path(pth):
    global file_path
    file_path = pth


def OpenFile():

    path = askopenfilename(filetypes=[("Python Files", "*.py")])

    with open(path, 'r') as file:
        code = file.read()
        editor.delete("1.0", END)
        editor.insert("1.0", code)
        set_file_path(path)


def run():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code')
        text.pack()
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code.insert('1.0', output)
    code.insert('1.0',  error)


def SaveAs():

    path = asksaveasfilename(filetypes=[('Python Files', '*.py')])

    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)


# ________________________________IDE_____________________________
compiler = Tk()
compiler.title("Basic studios")


menu_bar = Menu(compiler)

File = Menu(menu_bar, tearoff=0)
File.add_command(label='Open', command=OpenFile)
File.add_command(label='Save', command=SaveAs)
File.add_command(label='Save as', command=SaveAs)
File.add_command(label='Exit', command=exit)

menu_bar.add_cascade(label='File', menu=File)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run', menu=run_bar)

compiler.config(menu=menu_bar)

editor = Text(font= 'comic-sans',borderwidth = 3)
editor.pack()


code = Text(height = 10,borderwidth=4)
code.pack()
compiler.mainloop()
