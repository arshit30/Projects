from flask import Flask,render_template, request, redirect,send_file
from subtitles import *
from translate import translation
import os

app= Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/uploads'

@app.route('/', methods=['GET','POST'])

def home():
    
    if os.path.exists("translated.srt"):
        os.remove('translated.srt')
    
    if request.method =='POST':
        
        source = request.form['slan']
        destination = request.form['dlan']
        
        mp4 = request.files['mp4']
        
        if mp4.filename!='':
            mp4.save(os.path.join('./uploads/',mp4.filename))
            timings,dialogues=transcribe('./uploads/'+mp4.filename,source)
            translations=translation(dialogues,source,destination)
            create_subtitles(timings,translations)
            return send_file(filename_or_fp='translated.srt',as_attachment=True)
        else:
            sub = request.files['sub']
            sub.save(os.path.join('./uploads/',sub.filename))
            timings,dialogues=subtitle_data('./uploads/'+sub.filename)
            translations=translation(dialogues,source,destination)
            create_subtitles(timings,translations)
            return send_file(filename_or_fp='translated.srt',as_attachment=True)
    return render_template('home.html')

app.run(host='0.0.0.0',port=5000)
