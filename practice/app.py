from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/<name>')
def names(name):
    return render_template('user.html',name=name)

app.run(debug=True) #restarts the application when change in code is mades