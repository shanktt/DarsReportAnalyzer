import pandas as pd
import sys
import os.path
from group import group, grouptype
from minor import minor

# minor_data.csv layout:
# Name (col. 1) | List of req. courses (col. 2) | List of req. groups (col. 3 ~ 17, 1 group = 3 columns) | total req. credits (col. 18)

# convert a .csv file into a list of tuples
def csv_into_tuples(path):
    if not os.path.exists(path):
        print('Invalid path!')
        sys.exit(1)
    dataframe = pd.read_csv(path) # minor csv file doesn't have a header
    tuple_list = []
    for i in dataframe.itertuples():
        if len(i) != 28: # data safety check 
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
        repl_courses = []

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

                tup = (dept1 + ' ' + num, True)

                List = []
                List.append(dept2 + ' ' + num)

                tup2 = (dept1 + ' ' + num, List)

                req_courses.append(tup)
                # handle the second as a replacement course for the other
                repl_courses.append(tup2)
            
            # replacement course case
            elif 'OR' in i and not ('HORT' in i or 'PORT' in i or 'KOR' in i): # to prevent issues with HORT, PORT, KOR
                repl_list = i.split('OR')
                repl_list = [x.strip() for x in repl_list] # strip extra spaces
                
                # ex: repl_list looks like ['KIN 250', 'KIN 259']
                first_course = repl_list.pop(0)
                tup = (first_course, repl_list)
             
                repl_courses.append(tup)
                req_courses.append((first_course, True))
            # course not accepted for a minor case
            # regular course case
            else:
                tup = (i, False)
                                
                req_courses.append(tup)
        
        return req_courses, repl_courses
    return list(), list() # return empty list instead


# given a tuple (a row in the spreadsheet, representing one minor), extract the required groups and return a list of groups
def create_groups(minor_ : tuple):
    group_list = []
    for n in range(0, 5):  # minor has maximum of 5 groups
        
        # if the group's course list is empty, we are finished
        if pd.isnull(minor_[4 + 3 * n]):
            return group_list
        
        # extract group's information
        group_course_list, repl_list = create_course_list(minor_[4 + 4 * n])
        group_type_num = minor_[3 + 4 * n]
        group_type = grouptype.COURSES if minor_[2 + 4 * n] == 'C' else grouptype.CREDIT_HOURS
        group_unallowed = create_course_list(minor_[5 + 4 * n])
        group_unallowed = group_unallowed[0]
        
        unallowed = []
        
        for i in range(0, len(group_unallowed)):
            unallowed.append(group_unallowed[i][0])
        
        group_list.append(group(group_type, group_type_num, group_course_list, dict(repl_list), unallowed))

    return group_list


# given a tuple (representing one minor), return a minor object
def create_minor_object(minor_ : tuple):
    required_courses = create_course_list(minor_[26]) # minor[2] = string with required courses
    required_courses = required_courses[0]
    group_list = create_groups(minor_)
    
    # tuple[1] = minor name, tuple[27] = total required hours for minor
    return minor(minor_[1].upper(), required_courses, group_list, minor_[27])


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
# # print(a[10])
# List = create_minor_object(a[55])
# # # d = dict(d)
# List = create_minor_list(sys.argv[len(sys.argv) - 1])
# print(*List, sep='\n')

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