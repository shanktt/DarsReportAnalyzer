import os
from flask import Flask, request, redirect, render_template

import dars_parser, minor_parser, progress_checker

app = Flask(__name__)

app.config['ALLOWED_EXTENSIONS'] = ['pdf']

def file_allowed(filename):
    file_extension = filename.rsplit('.', 1)[1].lower()
    extension_allowed = file_extension in app.config["ALLOWED_EXTENSIONS"]
    return '.' in filename and extension_allowed


@app.route('/', methods=['GET', 'POST'])
def upload_image():

    if request.method == 'POST':

        if request.files:

            pdf = request.files['file']

            if pdf.filename == '':
                # print('file must have nonempty filename') # show this on webpage
                return redirect(request.url)

            if not file_allowed(pdf.filename):
                # print('extension not allowed') # show this on webpage
                return redirect(request.url)

            # pass info from here into html for visuals
            pdf_text = dars_parser.convert_pdf_to_text(pdf) # .pdf to one long string
            course_text = dars_parser.get_courses_from_text(pdf_text) # extract course list from string
            courses = dars_parser.put_courses_into_tuples(course_text) # put course text into list of tuples
            # for c in courses:
            #     print(c)
            df = minor_parser.create_pd('minor_data.csv')
            minors = minor_parser.create_minors(df)
            # csminor = minors[10]
            info = []

            for mnr in minors:

                infotuple = progress_checker.check_total_credits_met(mnr,courses)

                if (infotuple[0] == 0):
                    continue

                info.append(mnr.name)
                info.append('total credits matched: {}, percentage completed: {}'.format(infotuple[0], str(infotuple[1]*100) + '%'))
                reqtuple = progress_checker.check_required_courses(mnr, courses)
                info.append('required courses completed %: {}, required courses fulfilled: {}'.format(reqtuple[0], reqtuple[1]))

                for g in mnr.required_groups:
                    info.append('group:')

                    if g.goal_type == 'C':
                        # info.append(str(g.goal_type) + ' ' + str(progress_checker.check_C_type_group(g, courses)))
                        tuple = progress_checker.check_C_type_group(g,courses)
                        info.append('group type: {}, group percentage fulfilled: {}, group courses fulfilled: {}'.format(tuple[0], str(tuple[1]*100) + '%', tuple[2]))

                    else:
                        # info.append(str(g.goal_type) + ' ' + str(progress_checker.check_H_type_group(g, courses)))
                        tuple = progress_checker.check_H_type_group(g,courses)
                        info.append('group type: {}, group percentage fulfilled: {}, group courses fulfilled: {}'.format(tuple[0], str(tuple[1]*100) + '%', tuple[2]))

                info.append('\n')


            return render_template('index.html', courses = courses, info = info)

    return render_template('index.html')


# this allows running "python3 views.py" to start server
if __name__ == '__main__':
    app.run(debug=True)
