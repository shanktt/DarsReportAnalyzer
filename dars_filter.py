from collections import OrderedDict
import sys

# filter out classes with course numbers such as 1--
# filter out duplicates courses
def filter_courses(classes : list):
    classes = filter(lambda x: '--' not in x[1] and ('F' not in x[3] or 'NP' in x[3]), classes)
    classes = list(classes)

    classes = list(OrderedDict.fromkeys(classes))
    return classes

# create list of tuples (dept + course_num, credit_hours)
def put_into_courses(courses : list):
    list_of_courses = []
    for tup in courses:
        list_of_courses.append((tup[0] + ' ' + tup[1], float(tup[2])))
    return list_of_courses

# get a set of all the departments from which a student has taken a course
def get_dept_set(courses : list):
    depts = set()
    for c in courses:
        depts.add(c[0])
    return depts