import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter.messagebox import showinfo
from docx2pdf import convert

win = tk.Tk()
win.geometry('200x100')
win.title("Word to Pdf")

def openfile():
  file = filedialog.askopenfilename(filetypes=[('Word Files', '*.docx')])
  convert(file, r'D:\Study\Team projects\docx to pdf convertor\demo.pdf')
  showinfo("Done", "File successfully converted ")

label = tk.Label(win, text="Choose a file!")
label.grid(row=10, column=5, padx=5, pady=5)

button=ttk.Button(win,text="Select",width=30,command=openfile)
button.grid(row=20,column=5,padx=5,pady=5)

win.mainloop()