from sys import path
path.append('DarsReportAnalyzer/dars_parser.py')
import dars_parser
import dars_filter
import minor_parser
from progress import check_C_type_group, check_H_type_group, get_unique_courses_in_group, check_required_courses
import os


UPLOAD_FOLDER = 'DarsReportAnalyzer/site/static/pdf_upload'
MINOR_DATA = 'DarsReportAnalyzer/minor_data/minor_data.csv'

# Struct to make data easier to visualize for Chart.js
class minor_progress_struct():
    def __init__(self, name_ : str, group_names_ : list, group_percentages_ : list, groups_info_ : list):
        self.name = name_
        self.group_names = group_names_
        self.group_percentages = group_percentages_
        self.groups_info = groups_info_

    def __str__(self):
        return (f'{self.name}, {self.group_names}, {self.group_percentages}, {self.groups_info}')

    def __repr__(self):
        return (f'{self.name}, {self.group_names}, {self.group_percentages}, {self.groups_info}')

    def dump(self):
        return {'name' : self.name,
                'group_names' : self.group_names,
                'group_percentages' : self.group_percentages,
                'groups_info' : self.groups_info}


def analyze_dars():
    folder = os.listdir(UPLOAD_FOLDER)

    # visualization should not run if no DARS report is uploaded
    if len(folder) == 0:
        return None, None

    # get the first file
    name = folder[0]

    # generate the path for the files
    path = UPLOAD_FOLDER + '/' + name

    # convert pdf into a string
    # use ocr if needed
    pdf = dars_parser.convert_pdf_text(path=path)

    # get list of unformated courses
    courses = dars_parser.get_courses_from_text(text=pdf)
    # get courses in the form: (deptartment, course number, hours, grade)
    courses = dars_parser.get_courses_num_grade_and_hours(courses=courses)
    # filter out all duplicate, invalid, not passed courses
    courses = dars_filter.filter_courses(courses)
    # get set of all depts present in the dars report
    dept_set = dars_filter.get_dept_set(courses=courses)
    # put all the courses in the form: (department + ' ' + course number, credit hours earned)
    courses = dars_filter.put_into_courses(courses=courses)

    # return all the departments in DARS report/all courses taken
    # by the student
    return dept_set, courses

def analyze_minors():
    # create dataframe from minor_data csv
    df = minor_parser.create_pd(MINOR_DATA)
    # extract a list of all minors
    minors = minor_parser.create_minors(df)

    # return list of all minors
    return minors

# get a list of minor_progress_structs for the given DARS Report
def get_graph_list(intersection=1):
    dept_set, courses = analyze_dars()

    if dept_set is None and courses is None:
        return []

    minors = analyze_minors()
    graph_list = []
    for minor in minors:
        # if there is no intersection between the depts in the DARS Report
        # and the minors skip checking progress for the minor
        if len(minor.dept_set.intersection(dept_set)) < intersection:
            continue

        groups_info = []
        group_names = []
        group_percentages = []

        for i, group in enumerate(minor.required_groups, start=1):
            copy_courses = courses.copy()
            # get progress for H type group
            if group.goal_type == 'H':
                group_percentages.append(check_H_type_group(group, get_unique_courses_in_group(minor, group), copy_courses)[1])
            # get progress for C type group
            else:
                group_percentages.append(check_C_type_group(group, get_unique_courses_in_group(minor, group), copy_courses)[1])
            group_names.append((f'Group {i}'))

            # get list of courses that fulfil the group
            total = group.get_courses() + group.get_repl_courses_flattened()
            groups_info.append(total if len(total) <= 5 else total[:5])

        # check progress for the required courses for the minor
        if len(minor.required_courses) != 0:
            copy_courses = courses.copy()
            group_percentages.append(check_required_courses(minor, copy_courses)[1])
            group_names.append('Required Courses')

            total = minor.get_courses() + minor.get_repl_courses_flattened()
            groups_info.append(total if len(total) <= 5 else total[:5])

        progress = minor_progress_struct(name_=minor.name,
                                            group_names_=group_names,
                                                group_percentages_=group_percentages,
                                                    groups_info_=groups_info)

        graph_list.append(progress)

    # filter our all minors with 0 progress here
    i = 0
    while i < len(graph_list):
        if all(v == 0 for v in graph_list[i].group_percentages):
            graph_list.pop(i)
            continue
        i += 1

    # After all necessary information is taken from the DARS Report
    # Delete the File from the Upload Folder
    folder = os.listdir(UPLOAD_FOLDER)
    name = folder[0]
    path = UPLOAD_FOLDER + '/' + name

    os.remove(path=path)
    
    graph_list = [o.dump() for o in graph_list]

    return graph_list