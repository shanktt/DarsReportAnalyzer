from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO
import re
from dataclasses import dataclass
from minor import minor
import sys
from os import path
from course import course
# import json as j

# @profile
def pdf_to_text(path):
    manager = PDFResourceManager()
    retstr = BytesIO()
    layout = LAParams(all_texts=True)
    device = TextConverter(manager, retstr, laparams=layout)
    filepath = open(path, 'rb')
    interpreter = PDFPageInterpreter(manager, device)
    for page in PDFPage.get_pages(filepath, check_extractable=True):
        interpreter.process_page(page)
    text = retstr.getvalue()
    filepath.close()
    device.close()
    retstr.close()
    return text

# @profile
def format_text_in_array(unformatted_text):
    text = unformatted_text.decode('utf-8')
    classes_unformatted = text[text.rfind("SUMMARY OF COURSES TAKEN"):text.rfind("COLLEGE GPA")] # start to end of pdf
    classes_unformatted = classes_unformatted.replace("SUMMARY OF COURSES TAKEN -", "")
    classes_unformatted = classes_unformatted.replace(">I", "")
    classes_unformatted = classes_unformatted.replace("My Audit - Audit Results Tab", "")
    # classes_unformatted = classes_unformatted.replace("https://uachieve.apps.uillinois.edu/uachieve_uiuc/audit/read.html?printerFriendly=true&id=JobQueueRun!!!!ISEhIWludFNlcU5vPTMxMjczNDI=", "")
    lines = classes_unformatted.splitlines()
    lines = [line for line in lines if is_valid(line)]
    if '\uf00c' in lines:
        lines.remove('\uf00c')
    
    for s in lines:
        if '.edu' in s:
            lines.remove(s)

    # target_index = lines.index()
    try:
        target_index = lines.index('CREDIT NOT COUNTING TOWARDS GRADUATION')
        lines = lines[:target_index]
    except ValueError:
        pass

    return lines

# input pdf text. Output an array of courses taken
def format_text_in_array_regex(unformatted_text):
    text = unformatted_text.decode('utf-8')
    courses_unformatted = text[text.rfind("SUMMARY OF COURSES TAKEN"):]
    courses_unformatted = courses_unformatted.splitlines()
    courses_taken = []
    for c in courses_unformatted:   # for each unformatted line, check if it's a course. add to courses_taken if it is
        if re.search(r"[A-Z]{2}\d{2} [A-Z]{2,4} \d(\d|-){2} \w{1,3}", c) != None:
            c = c.split()
            courses_taken.append(course(c[1], c[2], -1))

    idx = 0
    for c in courses_unformatted: # for each course, find associated credit hours
        if re.search(r"\d\.0 (PS|IP|S|[A-D][-+]?)", c) != None:
            c = c.split()
            courses_taken[idx].credit_hours = c[0]
            idx += 1
    for c in courses_taken:
        print(c)
    return courses_taken



# @profile
def is_valid(s):
    trans = re.sub('^([1-9]|1[012])[/]([0-9]|[1-9][0-9])[/](19|20)\d\d$', '', s) # checks for date in m/d/yy format (ugh hate this format why does it exist)
    trans = re.sub('^([1-9]|1[012])[/]([0-9]|[1-9][0-9])$', '', trans) # checks for date in m/d format (ugh again)
    return trans.strip()  # Empty strings are falsy which means they are considered false in a boolean context

# @profile
def is_class(s):
    return not re.match('([0-9])', s) # lines is comprised of classes and their corresponding grades. Grades will start with a number while classes start with a character (indicating semester when class was taken)

# @profile
def passed_class(x):
    #Need more info on how classes displayed in dars report for this. What should we do about inprogress courses (count them as passed or not)? I'll count them for now
    passing_grades = ['PS', 'A', 'B', 'C', 'D-', 'S', 'IP']
    grade = x[1]
    
    for pg in passing_grades:
        if pg in grade:
            return True
    return False

# @profile
def get_courses_without_hours_and_sem(passed_classes): #do we care about getting a list of courses that contains courses one didn't recieve credit for?
    courses_without_hours = []
    for course_grade_pair in passed_classes:
        splitted = course_grade_pair[0].split()
        course_string = splitted[1] +  ' ' + splitted[2]
        courses_without_hours.append(course_string)
    return courses_without_hours

# @profile    
def get_courses_in_minor(courses, minor): #changed to take passed classes tuple
    classes_in_minor = []
    for course in courses:
        if minor.code in course:
            classes_in_minor.append(course)
    return classes_in_minor

# @profile
def get_total_hours_of_courses_in_minor(passed_courses, minor):
    total_hours = 0
    courses_with_credit_no_grade_and_sem = get_classes_with_credit_no_grade_and_sem(passed_courses)
    for course_grade_pair in courses_with_credit_no_grade_and_sem:
        if minor.code in course_grade_pair[0]:
            total_hours += float(course_grade_pair[1])
    return total_hours

# @profile
def get_classes_with_credit_no_grade_and_sem(passed_classes): #you should only get awarded classes if you pass it right?
    lone_courses = get_courses_without_hours_and_sem(passed_classes)
    classes_w_credit_wo_grade = []
    for course_grade_pair, course in zip(passed_classes, lone_courses):
        raw_grade_string = course_grade_pair[1].split()
        classes_w_credit_wo_grade.append((course, raw_grade_string[0]))
    return classes_w_credit_wo_grade

try:
    unformatted_text = pdf_to_text(sys.argv[len(sys.argv) - 1])
except IOError as e:
    print(e)
    print("Please pass in a valid path!")

format_text_in_array_regex(unformatted_text)
# lines = format_text_in_array(unformatted_text)
# classes = [s for s in lines if is_class(s)]
# grades = [s for s in lines if not is_class(s)]

# merged = [(classes[i], grades[i]) for i in range(0, len(classes))]
# passed_class = [class_and_grade for class_and_grade in merged if passed_class(class_and_grade)]
# passed_classes = filter(lambda x: "--" not in x[0], passed_class)
# passed_classes = list(passed_classes)
# computer_science_minor = minor('Computer Science', 'CS', ['CS 125', 'CS 173', 'CS 225'], 11, ['CS 233', 'CS 241', 'CS 357', 'CS 374', 'CS 410'], 9, [['CS 125', 'CS 173', 'CS 225']])
# courses_without_hours = get_courses_without_hours_and_sem(passed_classes)
# courses_in_minor = get_courses_in_minor(courses_without_hours, computer_science_minor)

# print (computer_science_minor.valid_required_classes_subset(courses_in_minor))

# print (get_classes_with_credit_no_grade_and_sem(passed_classes))

# print (courses_without_hours)
# print(passed_classes)
# json = j.dumps(dict(passed_classes))
# print(json)
# with open("sample.json", "x") as outfile:
#     outfile.write(json)

# print (get_total_hours_of_courses_in_minor(passed_classes, computer_science_minor))
# print(sys.argv[len(sys.argv) - 1])
