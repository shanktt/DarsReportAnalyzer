from flask import Flask, render_template, url_for, flash, redirect
# need to add request later on

# can add another secret key using import secrets secrets.token_hex(16)
# TODO: FIGURE OUT CACHE BUSTING to reload the CSS quicker

app = Flask(__name__)
app.config['ALLOWED_EXTENSIONS'] = ['pdf']
app.config['SECRET KEY'] = '289b39a433b94ad4882d3f1acd4e1956'


# routes the home page
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
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
    return render_template('visual.html', title='Visualization')



####################################### HELPER METHODS #######################################

def check_file(filename):
    file_extension = filename.rsplit('.', 1)[1].lower()
    extension_allowed = file_extension in app.config["ALLOWED_EXTENSIONS"]
    return '.' in filename and extension_allowed


if __name__ == '__main__':
    app.run(debug=True)