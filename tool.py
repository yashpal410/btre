from flask import Flask, render_template, request, send_file
from werkzeug import secure_filename
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    global file
    if request.method=='POST':
        file = request.files["file"]
        df = pd.read_excel(file)
        return render_template("index.html",text=df.to_html())

if __name__ == '__main__':
    app.run()
