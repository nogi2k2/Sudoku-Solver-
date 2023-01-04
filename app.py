import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import uuid

UPLOAD_FOLDER='images'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app=Flask(__name__)
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

def allowed_extensions(filename):
    return '.'in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method=='POST':
        if 'file' not in request.files:
            flash('No file uploaded')
            return redirect(request.url)
        
        file=request.files['file']
        
        if file.filename=='':
            flash('No file selected')
            return redirect(request.url)

        if file and allowed_extensions(file.filename):
            old_filename = secure_filename(file.filename)
            new_filename = str(uuid.uuid4()) + '.' + old_filename.split('.')[1]
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_filename))
            return redirect(url_for('upload_file', filename=new_filename))
    return render_template('home.html')

if __name__=='__main__':
    app.run(debug=True)