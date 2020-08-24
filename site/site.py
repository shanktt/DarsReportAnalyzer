from flask import Flask, render_template, url_for, flash, redirect, request
from sys import path
path.append('/Users/ameyagharpure/DarsReportAnalyzer')
from dars_parser import convert_pdf_text
from driver import get_graph_list
import os
from werkzeug.utils import secure_filename
import time

ALLOWED_EXTENSIONS = {'pdf'}
UPLOAD_FOLDER = '/Users/ameyagharpure/DarsReportAnalyzer/site/static/pdf_upload'

app = Flask(__name__)
app.config['SECRET_KEY'] = '7cb92ea70a44597ac5f029e5febc4aea'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS

# route for the home page
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    # empty pdf_upload directory
    if len(app.config['UPLOAD_FOLDER']) != 0:
            filelist = os.listdir(app.config['UPLOAD_FOLDER'])
            for f in filelist:
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'], f))

    if request.method == "POST":
        
        # empty pdf_upload directory
        if len(app.config['UPLOAD_FOLDER']) != 0:
            filelist = os.listdir(app.config['UPLOAD_FOLDER'])
            for f in filelist:
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'], f))

        # Error handling to ensure that a pdf is one the files
        # gotten via the POST request 
        if 'pdf' not in request.files:
            flash('No PDF Received', category='danger')
            return redirect(request.url)
        
        # get the file from the POST request
        file = request.files['pdf']
        
        # Check to make sure that data is passed to the app
        # if not flash error message
        if check_file(file.filename) is None:
            flash('No File Selected', category='danger')
            return redirect(request.url)

        # check to make sure the file is a valid pdf
        if not check_file(file.filename):
            flash('Please Select A PDF', category='danger')
            return redirect(request.url)

        # if the user doesn't select a file
        # browser might submit an empty part without filename
        if file.filename == '':
            flash('No File Selected', category='danger')
            return redirect(request.url)
        
        # TODO: Add another check to ensure its a valid DARS Report

        if file and check_file(file.filename):
            filename = secure_filename(file.filename)
            # save the file to directory so that it can be 
            # analyzed for visualization
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # if check_if_dars_report(app.config['UPLOAD_FOLDER'] + '/' + filename):
            flash('File Uploaded Successfully', category='success')
            return redirect(url_for('visualization'))
        
    return render_template('home.html', title='Home')
    

# route for the about page
@app.route('/about')
def about():
    return render_template('about.html', title='About')

# route for the visualization page
@app.route('/visualization')
def visualization():
    if len(UPLOAD_FOLDER) == 0:
        return redirect(url_for('home'))

    graph_list = get_graph_list()

    if graph_list is None:
        flash('Cannot Display Visualization', category='danger')
        return redirect(url_for('home'))
    else:
        return render_template('graph.html', title='Visualization', 
                                                graph_list=graph_list)
        

####################################### HELPER METHODS #######################################

# helper to ensure the file is a pdf
def check_file(filename):
    if filename != '':
        file_extension = filename.rsplit('.', 1)[1].lower()
        extension_allowed = file_extension in app.config['ALLOWED_EXTENSIONS']
        return '.' in filename and extension_allowed
    else:
        return None

if __name__ == '__main__':
    app.secret_key = app.config['SECRET_KEY']
    app.run(debug=True)