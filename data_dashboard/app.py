from flask import Flask,render_template,request,redirect,flash,send_from_directory,url_for
import os
import pandas as od
import matplotlib.pyplot as plt
from werkzeug.utils import secure_filename
from config import UPLOAD_FOLDER,PROCESSED_FOLDER,SECRET_KEY

#setup app.py
app=Flask(__name__)
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER#“In the app’s settings, store the rule that uploaded files go into this folder.”
app.secret_key=SECRET_KEY

#Create a route to display the upload form
@app.route('/')
def index():
    return render_template('index.html')# http response

# Handle CSV uploads
@app.route('/upload',methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('no file part')
        return redirect(url_for('index'))
    file=request.files['file']

if __name__=="__main__":
    app.run(debug=True)
