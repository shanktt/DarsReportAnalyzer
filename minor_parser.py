import pandas as pd
import sys
import os.path
from group import group, grouptype
from course import course
from minor import minor

# minor_data.csv layout:
# Name (col. 1) | List of req. courses (col. 2) | List of req. groups (col. 3 ~ 17, 1 group = 3 columns) | total req. credits (col. 18)

# convert a .csv file into a list of tuples
def csv_into_tuples(path):
    if not os.path.exists(path):
        print('Invalid path!')
        sys.exit(1)
    dataframe = pd.read_csv(path, header=None) # minor csv file doesn't have a header
    tuple_list = []
    for i in dataframe.itertuples():
        if len(i) != 19: # data safety check 
            print(i)
            print("A row in the given .csv file is not of length 19!")
            sys.exit(0)
        tuple_list.append(i)
    return tuple_list
    

# creates a list of courses based of the csv file
# accounts for replacement courses/pair courses/cross-listed courses
def create_course_list(courses : str):
    if not pd.isnull(courses):
        req_courses = []
        course_list = []
        
        course_list = courses.split(',')
        course_list = map(lambda x : x.upper(), course_list) # ensure all strs are upper case
        course_list = list(course_list) # ensure that list is still a list
        course_list = [x.strip() for x in course_list] # remove leading/trailing spaces
        
        # ex: course_list looks like ['KIN 249', 'KIN 250 OR KIN 259', 'CS 125 AND CS 173', 'CS/ECE 374']
        for i in course_list:
            # cross-listed course case
            if '/' in i:
                dept1 = i[0:i.find('/')]
                dept2 = i[i.find('/') + 1:i.find(' ')]
                num = i[i.find(' ') + 1:]

                num = int(num[0:1]) * -100 if 'XX' in num else int(num)
                req_courses.append(course(dept1, num))
                req_courses.append(course(dept2, num))
            # pair course case
            elif 'AND' in i:
                List = i.split('AND')
                List = [x.strip() for x in List]

                dept = List[0][0:List[0].find(' ')]
                num = List[0][List[0].find(' ') + 1:]

                num = int(num[0:1]) * -100 if 'XX' in num else int(num)

                other_dept = List[1][0:List[1].find(' ')]
                other_num = List[1][List[1].find(' ') + 1:]

                other_num = int(other_num[0:1]) * -100 if 'XX' in other_num else int(other_num)

                req_courses.append(course(dept, num, course_pair_=(other_dept, other_num, None)))
            # replacement course case
            elif 'OR' in i and not ('HORT' in i or 'PORT' in i or 'KOR' in i): # to prevent issues with HORT, PORT, KOR
                repl_list = i.split('OR')
                repl_list = [x.strip() for x in repl_list] # strip extra spaces
                
                # ex: repl_list looks like ['KIN 250', 'KIN 259']
                
                dept = repl_list[0][0:repl_list[0].find(' ')]
                num = repl_list[0][repl_list[0].find(' ') + 1:]
                
                num = int(num[0:1]) * -100 if 'XX' in num else int(num)

                course_rep_list = []
                for i in range(1, len(repl_list)):
                    repl_dept = repl_list[i][0:repl_list[i].find(' ')]
                    repl_num = repl_list[i][repl_list[i].find(' ') + 1:]

                    repl_num = int(repl_num[0:1]) * -100 if 'XX' in repl_num else int(repl_num)

                    tup = (repl_dept, repl_num, None)

                    course_rep_list.append(tup)
                req_courses.append(course(dept, num, repl_list_=course_rep_list))
            # course not accepted for a minor case
            elif '!' in i: # ex !ANSC 101
                dept = i[1:i.find(' ')]
                num = i[i.find(' ') + 1:]
                
                # ensure these courses do not count towards the minor
                req_courses.append(course(dept, num, counts_=False))
            # regular course case
            else:
                dept = i[0:i.find(' ')] 
                num = i[i.find(' ') + 1:]
                
                num = int(num[0:1]) * -100 if 'XX' in num else int(num)
                
                req_courses.append(course(dept, num))
        
        return req_courses
    return list() # return empty list instead


# given a tuple (a row in the spreadsheet, representing one minor), extract the required groups and return a list of groups
def create_groups(minor_ : tuple):
    group_list = []
    for n in range(0, 5):  # minor has maximum of 5 groups
        
        # if the group's course list is empty, we are finished
        if pd.isnull(minor_[5 + 3 * n]):
            return group_list
        
        # extract group's information
        group_course_list = create_course_list(minor_[5 + 3 * n])
        group_type_num = minor_[4 + 3 * n]
        group_type = grouptype.COURSES if minor_[3 + 3 * n] == 'C' else grouptype.CREDIT_HOURS
        
        group_list.append(group(group_type, group_type_num, group_course_list))

    return group_list


# given a tuple (representing one minor), return a minor object
def create_minor_object(minor_ : tuple):
    required_courses = create_course_list(minor_[2]) # minor[2] = string with required courses
    group_list = create_groups(minor_)
    
    # tuple[1] = minor name, tuple[18] = total required hours for minor
    return minor(minor_[1], required_courses, group_list, minor_[18])


# given a path to a csv file containing minor data, return a list of minor objects
def create_minor_list(path):
    tuple_list = csv_into_tuples(path)
    minor_list = []
    for x in tuple_list:
        minor_obj = create_minor_object(x)
        minor_list.append(minor_obj)

    return minor_list


######################### testing below #########################

# a = csv_into_tuples(sys.argv[len(sys.argv) - 1])

# print(a[2])

# test to check for any mistakes in the excel sheet
# List = []
# for y in range(2, 18, 3):
#     for x in range(0, len(a)):
#         var = create_course_list(a[x][y])
#         List.append(var)

# print(*List, sep='\n')
# for i in range(0, len(List)):
#     print(i, List[i])

# tup = a[2]
# group = create_groups(tup)
# print(group)
# minor = create_minor_object(tup)
# print(minor)
# print(minor.name)

# minors = create_minor_list(sys.argv[len(sys.argv) - 1])
# print(minors[22])
# print(*minors, '\n')