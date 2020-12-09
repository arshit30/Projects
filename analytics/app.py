from flask import Flask,request,render_template
from files import read_data

app=Flask(__name__)

@app.route('/')
def index(methods=['GET','POST']):
    return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      files = request.files['file']
      dataset=read_data(files)
      return render_template('uploader.html',items=dataset)

app.run(debug=True)