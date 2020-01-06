from flask import Flask
import pandas as pd

df = pd.read_excel( r'C:\Users\yashpal.yadav\Desktop\PMO Dashboard.xlsx')
print(df)

app = Flask(__name__)

@app.route("/")
def index():
    return ("<div> {} </div>".format(df))
