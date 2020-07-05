import minor_parser
import dars_parser
import dars_filter
import sys

# basic script to show how many minors we probably have to check for most DARS Reports
dataframe = minor_parser.create_pd('minor_data/minor_data.csv')
minors = minor_parser.create_minors(dataframe)

text = dars_parser.convert_pdf_text(sys.argv[len(sys.argv) - 1])
courses = dars_parser.get_courses_from_text(text)
courses = dars_parser.get_courses_num_grade_and_hours(courses)

courses = dars_filter.filter_courses(courses)
depts = dars_filter.get_dept_set(courses)
courses = dars_filter.put_into_courses(courses)

for i, m in enumerate(minors):
    print(m)
    intersect = m.dept_set.intersection(depts)
    if len(intersect) > 0:
        print(i, m.name, intersect)