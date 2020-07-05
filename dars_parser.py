import pdftotext
import unicodedata
import re
import subprocess
import os
from collections import OrderedDict

# Function takes the path to a pdf and then converts it to a string
def convert_pdf_to_text(pdf):
    # with open(path, 'rb') as f:
    #     pdf = pdftotext.PDF(f)

    pdf = pdftotext.PDF(pdf)

    whole_report = str()

    for page in pdf:
        whole_report += page

    # TODO: handle cases in which the passed file is not a pdf or is not an actual dars report
    # if we want to implement check for valid
    # dars, put it here - but should we even
    # ask for entire dars report?

    return whole_report

# Function takes a dars report in string format and returns a list of unformatted strings representing that courses a student has taken or is taking
def get_courses_from_text(text):

    #TODO: Identify all different formats of dars reports
    # Essentially that if else if tree is trying to shortern text to that only the total courses a student has taken remains in the string
    # So we can filter this shorter and easier to parse string
    if 'SUMMARY OF COURSES TAKEN' in text:
        # Concatenates text to substring in text between last found occurences of 'SUMMARY OF COURSES TAKEN' to the end of text
        text = text[text.rfind('SUMMARY OF COURSES TAKEN'):]
    elif 'YOU MUST COMPLETE' in text:
        # Concatenates text to substring in text between last found occurences of 'YOU MUST COMPLETE to the end of text
        text = text[text.rfind('YOU MUST COMPLETE'):]

    # text = text[text.rfind('SUMMARY OF COURSES TAKEN'):]

    # Creats a list of all the lines in text
    lines = text.split('\n')

    # Uses regex to remove all extra spaces as well as leading spaces from a string. Example " Quick    Brown    Fox" -> "Quick Brown Fox"
    lines = [re.sub(' +', ' ', s.lstrip()) for s in lines]

    # Removes strings whose first 4 characters are not two letters followed by two digits
    # The list of courses a student has taken is in the form of [Term][Year] followed by the course and more information
    # [Term] and [Year] are represented by 2 uppercase letters and two digits respectively
    # Therefore strings in lines that do not follow this format are not lines containing a course a student has taken and we can throw them out
    courses = [s for s in lines if re.match('[A-Z].*[A-Z][1-9][0-9]', s[0:4])]

    return courses

# Function takes an unformatted list of courses and returns a list of tuples with each tuple
# in the form (course (ex CS), course number, hours, grade)
def put_courses_into_tuples(course_text):
    courses = []

    for s in course_text:
        # ignores any duplicate courses from the DARS report
        if '>D' in s:
            continue
        # Creates a list of strings split on whitespaces
        splitted = s.split()

        course = splitted[1]
        course_num  = splitted[2]

        # check if the class is gotten by transfer credit,
        # if so hours will located in a different place in the list
        if 'TR' in splitted:
            hours = splitted[3]
        else:
            hours = splitted[4]

        # ocrmypdf sometimes incorrectly removes the decimal from the number of credits for a course
        # For example sometimes 4.0 becomes 40. This if statement adds back the missing decimal place
        if '.' not in hours:
            # Converts hours to a float then divide by 10 then converts back to a string
            hours = str(float(hours) / 10)

        # format of string is different for transfer credit
        if 'TR' in splitted:
            grade = splitted[4]
        else:
            grade = splitted[5]

        courses.append((course, course_num, hours, grade))

    # filtering
    courses = filter(lambda x: '--' not in x[1] and 'F' not in x[3], courses)
    courses = list(courses)
    courses = list(OrderedDict.fromkeys(courses))

    list_of_courses = []
    for tup in courses:
        list_of_courses.append((tup[0] + ' ' + tup[1], float(tup[2])))
    return list_of_courses

# given a filtered list of course tuples, return just the courses
#TODO: put in utils
def get_courses_only(course_tuple_list : list):
    return [c[0] for c in course_tuple_list]