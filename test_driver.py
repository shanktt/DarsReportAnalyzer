import minor_parser
import dars_parser
import dars_filter
import os

# basic script to show how many minors we probably have to check for most DARS Reports
def func(min_similar_depts):
    for file in os.listdir('dars_pdfs'):
        filename = os.fsdecode(file)
        if filename.endswith('.pdf'):
            dataframe = minor_parser.create_pd('minor_data/minor_data.csv')
            minors = minor_parser.create_minors(dataframe)

            text = dars_parser.convert_pdf_text('dars_pdfs/' + str(filename))
            courses = dars_parser.get_courses_from_text(text)
            courses = dars_parser.get_courses_num_grade_and_hours(courses)

            courses = dars_filter.filter_courses(courses)

            depts = dars_filter.get_dept_set(courses)
            courses = dars_filter.put_into_courses(courses)

            count = 0
            print(filename)
            for i, m in enumerate(minors):
                # print(m)
                intersect = m.dept_set.intersection(depts)
                if len(intersect) >= min_similar_depts:
                    count += 1
                    print(i, m.name, intersect)
            print('Intersection with {} minors'.format(count))
if __name__ == '__main__':
    func(3)
