import tkinter as tk
from tkinter import filedialog
import pandas as pd
from flask import Flask
import webbrowser

root= tk.Tk()
canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue')
canvas1.pack()



def getExcel ():
    global df

    import_file_path = filedialog.askopenfilename()
    df = pd.read_excel (import_file_path)
    open("link.html", "w").write("{}".format(df.to_html())
    webbrowser.open("link.html")

def getFile():
    getExcel()

browseButton_Excel = tk.Button(text='Import Excel File', command=getFile, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=browseButton_Excel)
root.mainloop()
