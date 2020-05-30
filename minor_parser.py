import pandas as pd
import sys
import re
import os.path
from enum import Enum, auto
from group import group, grouptype
from course import course
from minor import minor

# column 1 = minor_name
# column 2 = required_courses
# column 3 + 3x (where x is group number) = group_type
# column 4 + 3x (where x is group number) = group_num (credits/num_classes)
# column 5 + 3x (where x is group number) = list_of_courses
# x = 0, 1, 2, 3, 4
# column 18 = total_credits_required
def put_data_into_tuples(path):
    if not os.path.exists(path):
        print('Invalid path!')
        sys.exit(1)
    dataframe = pd.read_csv(path, header=None) # csv files don't have headers
    tuple_list = []
    for i in dataframe.itertuples():
        if len(i) != 19: # data safety check 
            print(i)
            print("a row in the csv is not of length 19")
            sys.exit(0)
        tuple_list.append(i)
    return tuple_list
    

def create_course_list(courses : str):
    if not pd.isnull(courses):
        req_courses = []
        course_list = []
        
        course_list = courses.split(',')
        course_list = map(lambda x : x.upper(), course_list) # ensure all strs are upper case
        course_list = list(course_list) # ensure that list is still a list
        course_list = [x.strip() for x in course_list] # remove leading/trailing spaces
        
        # ex: course_list looks like ['KIN 249', 'KIN 250 OR KIN 259', 'CS 125 AND CS 173']
        for i in course_list:
            if 'AND' in i: # TODO: Figure out how to handle this edge case
                pass
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
            elif '!' in i: # ex !ANSC 101
                dept = i[1:i.find(' ')]
                num = i[i.find(' ') + 1:]
                
                # ensure these courses do not count towards the minor
                req_courses.append(course(dept, num, counts_=False))
            else:
                dept = i[0:i.find(' ')] 
                num = i[i.find(' ') + 1:]
                
                num = int(num[0:1]) * -100 if 'XX' in num else int(num)
                
                req_courses.append(course(dept, num))
        
        return req_courses
    return list() # return empty list instead


# given a tuple (a row in the spreadsheet, representing one minor), extract the required groups and return a list of groups
def create_groups(group_tuple : tuple):
    group_list = []
    for n in range(0, 5):  # minor has maximum of 5 groups
        
        if pd.isnull(group_tuple[5 + 3 * n]): # if the group's course list is empty, we are finished
            return group_list
        
        group_course_list = create_course_list(group_tuple[5 + 3 * n])
        group_type_num = group_tuple[4 + 3 * n]
        group_type = grouptype.COURSES if group_tuple[3 + 3 * n] == 'C' else grouptype.CREDIT_HOURS
        
        group_list.append(group(group_type, group_type_num, group_course_list))

    return group_list


# given a tuple (representing one minor), return a minor object
def create_minor_object(minor_tuple : tuple):
    required_courses = create_course_list(minor_tuple[2]) # tuple[2] = string with required courses
    group_list = create_groups(minor_tuple)
    
    return minor(minor_tuple[1], required_courses, group_list, minor_tuple[18]) # tuple[1] = minor name, tuple[18] = total required hours for minor

def create_minor_list(tuple_list):
    minor_list = []
    for x in tuple_list:
        minor_obj = create_minor_object(x)
        minor_list.append(minor_obj)

    return minor_list


######################### testing below #########################

a = put_data_into_tuples(sys.argv[len(sys.argv) - 1])

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

minors = create_minor_list(a)
print(*minors, '\n')