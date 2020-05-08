from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO
import re
from dataclasses import dataclass
from minor import minor

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

def format_text_in_array(unformatted_text):
    text = unformatted_text.decode('utf-8')
    classes_unformatted = text[text.rfind("SUMMARY OF COURSES TAKEN"):text.rfind("COLLEGE GPA")]
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

def is_valid(s):
    trans = re.sub('^([1-9]|1[012])[/]([0-9]|[1-9][0-9])[/](19|20)\d\d$', '', s) # checks for date in m/d/yy format (ugh hate this format why does it exist)
    trans = re.sub('^([1-9]|1[012])[/]([0-9]|[1-9][0-9])$', '', trans) # checks for date in m/d format (ugh again)
    return trans.strip()  # Empty strings are falsy which means they are considered false in a boolean context

def is_class(s):
    return not re.match('([0-9])', s) # lines is comprised of classes and their corresponding grades. Grades will start with a number while classes start with a character (indicating semester when class was taken)

def passed_class(x):
    #Need more info on how classes displayed in dars report for this. What should we do about inprogress courses (count them as passed or not)? I'll count them for now
    passing_grades = ['PS', 'A', 'B', 'C', 'D-', 'S', 'IP']
    grade = x[1]
    
    for pg in passing_grades:
        if pg in grade:
            return True
    return False

def get_courses_without_hours_and_sem(passed_classes): #do we care about getting a list of courses that contains courses one didn't recieve credit for?
    courses_without_hours = []
    for course_grade_pair in passed_classes:
        splitted = course_grade_pair[0].split()
        course_string = splitted[1] +  ' ' + splitted[2]
        courses_without_hours.append(course_string)
    return courses_without_hours
        
def get_courses_in_minor(courses, minor): #changed to take passed classes tuple
    classes_in_minor = []
    for course in courses:
        if minor.code in course:
            classes_in_minor.append(course)
    return classes_in_minor

def get_total_hours_of_courses_in_minor(passed_courses, minor):
    total_hours = 0
    courses_with_credit_no_grade_and_sem = get_classes_with_credit_no_grade_and_sem(passed_courses)
    for course_grade_pair in courses_with_credit_no_grade_and_sem:
        if minor.code in course_grade_pair[0]:
            total_hours += float(course_grade_pair[1])
    return total_hours


def get_classes_with_credit_no_grade_and_sem(passed_classes): #you should only get awarded classes if you pass it right?
    lone_courses = get_courses_without_hours_and_sem(passed_classes)
    classes_w_credit_wo_grade = []
    for course_grade_pair, course in zip(passed_classes, lone_courses):
        raw_grade_string = course_grade_pair[1].split()
        classes_w_credit_wo_grade.append((course, raw_grade_string[0]))
    return classes_w_credit_wo_grade


unformatted_text = pdf_to_text('dara2.pdf') 
lines = format_text_in_array(unformatted_text)
classes = [s for s in lines if is_class(s)]
grades = [s for s in lines if not is_class(s)]

merged = [(classes[i], grades[i]) for i in range(0, len(classes))]
passed_classes = [class_and_grade for class_and_grade in merged if passed_class(class_and_grade)]
computer_science_minor = minor('Computer Science', 'CS', ['CS 125', 'CS 173', 'CS 225'], 11, ['CS 233', 'CS 241', 'CS 357', 'CS 374', 'CS 410'], 9, [['CS 125', 'CS 173', 'CS 225']])
courses_without_hours = get_courses_without_hours_and_sem(passed_classes)
courses_in_minor = get_courses_in_minor(courses_without_hours, computer_science_minor)

# print (computer_science_minor.valid_required_classes_subset(courses_in_minor))

# print (get_classes_with_credit_no_grade_and_sem(passed_classes))
print (passed_classes)
print (get_total_hours_of_courses_in_minor(passed_classes, computer_science_minor))