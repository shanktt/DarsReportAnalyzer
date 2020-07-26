from flask import Flask, render_template, url_for, flash, redirect, request
import os
from werkzeug.utils import secure_filename
import time

# can add another secret key using import secrets secrets.token_hex(16)
# import os; print(os.urandom(16))
# TODO: FIGURE OUT CACHE BUSTING to reload the CSS quicker

ALLOWED_EXTENSIONS = {'pdf'}
UPLOAD_FOLDER = '/Users/ameyagharpure/DarsReportAnalyzer/site/static/pdf_uploads'

app = Flask(__name__)
app.config['SECRET_KEY'] = ''
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS

# routes the home page
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == "POST":

        # TODO: ENSURE THAT ALL FILES ARE REMOVED BEFORE HAND
        
        # Error handling to ensure that a pdf is one the files
        # gotten via the POST request 
        if 'pdf' not in request.files:
            flash('bro', category='danger')
            return redirect(request.url)
        
        # get the file from the POST request
        file = request.files['pdf']
        
        # Check to make sure that data is passed to the app
        # if not flash error message
        if check_file(file.filename) is None:
            flash('gimme some data doggo', category='danger')
            return redirect(request.url)

        # check to make sure the file is a valid pdf
        if not check_file(file.filename):
            flash('bruh tf u doing gimme a pdf', category='danger')
            return redirect(request.url)

        # if the user doesn't select a file
        # browser might submit an empty part without filename
        if file.filename == '':
            flash('bruh no file selected', category='danger')
            return redirect(request.url)
        
        if file and check_file(file.filename):
            filename = secure_filename(file.filename)
            # save the file to directory so that it can be 
            # analyzed for visualization
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File Uploaded Successfully', category='success')
            
            # go to the page for d3.js visualization after waiting 0.5 seconds
            # time.sleep(0.5)
            return redirect(url_for('visualization'))

    return render_template('home.html', title='Home')
    

# routes the about page
@app.route('/about')
def about():
    return render_template('about.html', title='About')


# routes the visualization page that will only be accessed through the home page
# TODO: HOW TO PREVENT PEOPLE FROM VISITING THIS PAGE EVEN IF THEY HAVE THE LINK TO IT
# https://stackoverflow.com/questions/42450813/in-flask-how-do-i-prevent-a-route-from-being-accessed-unless-another-route-has
# https://flask-wtf.readthedocs.io/en/stable/form.html
# https://flask-wtf.readthedocs.io/en/stable/csrf.html

@app.route('/visualization')
def visualization():
    folder = os.listdir(UPLOAD_FOLDER)

    # if no pdf is in the folder redirect to the home page
    # mayb display an error message??? cuz it should never get here without a file
    # within the directory
    if len(folder) == 0:
        return redirect(url_for('home'))
    else:
        return render_template('visual.html', title='Visualization')
        

####################################### HELPER METHODS #######################################

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