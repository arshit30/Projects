from flask import Flask,request,render_template
app=Flask(__name__)


@app.route('/')
def index(methods=['GET','POST']):
    return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      files = request.files['file']
      return 'file uploaded successfully'

app.run(debug=True)