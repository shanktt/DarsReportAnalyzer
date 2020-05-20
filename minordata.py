import pandas as pd
from course import course
from minor import minor
from group import group


def create_tuples_from_data(path):
    data = pd.read_csv(path)
    a = []
    for i in data.itertuples():
        a.append(i)
    return a

def create_courses(stuffs):
    courses = []
    for s in stuffs:
        dept = s[0:int(s.find(' '))]
        course_num = s[int(s.find(' ') + 1):int(s.find(':'))]
        credit_hours = int(s[int(s.find(':')) + 1])
        courses.append(course(dept, course_num, credit_hours))
    return courses


a = create_tuples_from_data('sample_data.csv')
a.pop(0)
stuff = a[0][4]
stuff2 = a[0][4].split(',')
stuff2[0] = stuff2[0].replace('{', '')
stuff2[len(stuff2) - 1] = stuff2[len(stuff2) - 1].replace('}', '')



b = create_courses(stuff2)
print(b)