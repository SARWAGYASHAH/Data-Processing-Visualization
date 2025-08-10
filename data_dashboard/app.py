from flask import Flask,render_template,request
import os
app=Flask(__name__)
# an instance is created
# web app is prepared !!!
@app.route('/')# when someone visits this url 
def index():# this function undertakes evaulation
    return render_template('index.html')# http response

##@app.route('/upload',methords=['POST'])
##def upload_file():
 ##   if request.method==['POST']:

if __name__=="__main__":
    app.run(debug=True)
