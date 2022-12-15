import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog as fd
import main
import subprocess

app_name = 'PDF Summary'
version = '(beta)'
maintitle = '{0} {1}'.format(app_name, version)

root = tk.Tk()  # Создаём окно приложения.

root.title(maintitle)  # Добавляем название приложения.
# root.iconbitmap(r'C:\PyProjects\PDFreader\icon.ico')
root.geometry('325x100+700+350')
root.config(bg="white")

height_lb = tk.Label(text="Текущая директория  ", font='Calibri 14', background='white')
height_lb.pack()

current_directory = tk.Label(text='не указана', font='Calibri 12', foreground='red', background='white')
current_directory.pack()


def open_dir():
    dirpath = fd.askdirectory()
    if dirpath != "":
        current_directory.configure(text=dirpath, foreground='green')
        message_true = 'Отчет сформирован. Открыть директорию?'
        message_false = 'Директория не содержит документов PDF'
        result = main.main_prg(dirpath)
        if result:
            answer = messagebox.askyesno(title=maintitle, message=message_true)
            if answer:
                process = 'explorer'
                path = f'"{dirpath}"'
                edited_path = path.replace("/", "\\")
                output_dir = str(f'{process} {edited_path}')
                subprocess.Popen(output_dir)
        else:
            messagebox.showinfo(title=maintitle, message=message_false)


open_button = tk.Button(text="Указать директорию", command=open_dir)
open_button.pack()



root.mainloop()
