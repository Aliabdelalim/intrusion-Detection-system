from datetime import date
from flask import Flask 
from flask import jsonify
from intrusion import Check
from flask import render_template,request
import pandas as pd
app= Flask (__name__)


@app.route("/")
@app.route("/index.html")
def index():
    return render_template('index.html')
    
    
@app.route("/about.html")
def about():
    return render_template('about.html')



#@app.route("/protect")    
#def protect():
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import os

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return render_template('index.html', output='') 

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/Check')
def check():
    df = None
    if os.path.exists('t.csv'):
        df = pd.read_csv('t.csv')
    else:
        print('File t.csv not found!')
        exit(1)
    out = Check(df)       
    print('Now returning index.html')
    return render_template('index.html', output=out)    


app.run()