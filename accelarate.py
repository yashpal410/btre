#https://datatofish.com/read_excel/
'''import tkinter as tk
from tkinter import filedialog
import pandas as pd

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue')
canvas1.pack()

def getExcel ():
    global df
    
    import_file_path = filedialog.askopenfilename()
    df = pd.read_excel (import_file_path)
    print (df)
    
browseButton_Excel = tk.Button(text='Import Excel File', command=getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=browseButton_Excel)

root.mainloop()
'''
from flask import Flask
import pandas as pd

df = pd.read_excel( r'C:\Users\yashpal.yadav\Desktop\PMO Dashboard.xlsx')
print(df)

app = Flask(__name__)

@app.route("/")
def index():
    return ("<div> {} </div>".format(df))
