from sys import path
path.append('/Users/ameyagharpure/DarsReportAnalyzer')
import dars_parser
import dars_filter
import minor_parser
from progress import check_C_type_group, check_H_type_group, get_unique_courses_in_group, check_required_courses
import os


UPLOAD_FOLDER = '/Users/ameyagharpure/DarsReportAnalyzer/site/static/pdf_upload'
MINOR_DATA = '/Users/ameyagharpure/DarsReportAnalyzer/minor_data/minor_data.csv'



# Struct to make data easier to visualize for d3.js
class minor_progress_struct():
    def __init__(self, name_ : str, group_names_ : list, group_percentages_ : list):
        self.name = name_
        self.group_names = group_names_
        self.group_percentages = group_percentages_

    def __str__(self):
        return (f'{self.name}, {self.group_names}, {self.group_percentages}')

    def __repr__(self):
        return (f'{self.name}, {self.group_names}, {self.group_percentages}')

    def dump(self):
        return {'name' : self.name,
                'group_names' : self.group_names,
                'group_percentages' : self.group_percentages}


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

    # remove the dars reports from the directory once all needed information is gathered
    # os.remove(path=path)

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

# creates a list of tuples with each tuple formatted (Minor name, List of tuples with completion for each group)
# the inner list of tuples will be formatted (Group Number, (Group type, Percentage Completed, Courses Counted Towards Group))
def create_completion_list(intersection=1):
    dept_set, courses = analyze_dars()

    if dept_set == None and courses == None:
        return []

    minors = analyze_minors()

    completion_list = []
    for minor in minors:
        # if the length of the intersection of the set of departments in the minor/the student's DARS report is less than
        # the intersection length parameter skip progress checking for that minor
        if len(minor.dept_set.intersection(dept_set)) < intersection:
            continue
        minor_completion = []
        # iterate through the groups for the minor
        for i, group in enumerate(minor.required_groups, start=1):
            progress = []
            copy_courses = courses.copy()
            if group.goal_type == 'H':
                progress = check_H_type_group(group, get_unique_courses_in_group(minor, group), copy_courses)
            else:
                progress = check_C_type_group(group, get_unique_courses_in_group(minor, group), copy_courses)
            minor_completion.append((f'Group {i}', tuple(progress)))
        
        # only check progress for the required courses if there are any required_courses for minor
        if len(minor.required_courses) != 0:
            copy_courses = courses.copy()
            progress = check_required_courses(minor, copy_courses)
            minor_completion.append(('Required Courses', progress))
        
        # append a tuple with in the form with the name of the minor with a
        # list of lists with the completion progress for each group for the minor
        tup = (minor.name, minor_completion)
        completion_list.append(tup)

    return completion_list

def get_completion_list(intersection=1):
    completion_list = create_completion_list()
    
    # in case that visualization cannot be displayed
    if len(completion_list) == 0:
        return None

    final_completion_list = []
    for c in completion_list:
        all_zero = True
        for x in c[1]:
            if x[1][1] > 0:
                all_zero = False
        if not all_zero:
            final_completion_list.append(c)
    
    return final_completion_list

def get_graph_list():
    completion_list = get_completion_list()
    graph_list = []

    for minor in completion_list:
        name = minor[0]
        group_names = []
        group_percentages = []
        for c in minor[1]:
            group_name = c[0]
            # print(group_name)
            percentage = c[1][1]
            # print(percentage)
            group_names.append(group_name)
            group_percentages.append(percentage)
        
        progress = minor_progress_struct(name_=name, group_names_=group_names, group_percentages_=group_percentages)
        graph_list.append(progress)

    return graph_list


if __name__ == '__main__':
    # print(analyze_dars())
    # print(analyze_minors())
    # print(*get_completion_list(), sep='\n')
    l = get_graph_list()
    l = [o.dump() for o in l]
    print(*l, sep='\n')
    # print(get_graph_list())
    # for i in range(1):
    #     List = get_completion_list()
    #     # stuff = get_minor_and_groups(List)
    #     print(*stuff, sep='\n')