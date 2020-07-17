from flask import Flask, render_template, url_for, flash, redirect, request


app = Flask(__name__)
app.config['ALLOWED_EXTENSIONS'] = ['pdf']


def check_file(filename):
    file_extension = filename.rsplit('.', 1)[1].lower()
    extension_allowed = file_extension in app.config["ALLOWED_EXTENSIONS"]
    return '.' in filename and extension_allowed

@app.route('/', methods=['GET', 'POST'])
@app.route('/home')
def home():
    # can adds some vars when you get to the pt
    if request.method == 'POST':
        pdf = request.files['file']

        # TODO: MAKE THIS A FLASH USING BOOTSTRAP TO TELL USER TO INPUT SOMETHING VALID YOU FEEL
        # redirect back to the homescreen
        # if pdf.filename == '':
        #     flash()

        # TODO: MAKE THIS A FLASH USING BOOTSTRAP TO TELL USER TO INPUT SOMETHING VALID YOU FEEL
        # redirect back to the homescreen
        # if not check_file(pdf.filename):
        #     flash()
        # return render_template('home_vis.html', content=content)
        return render_template('home.html', title='Home')
    else:
        return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')



if __name__ == '__main__':
    app.run(debug=True)