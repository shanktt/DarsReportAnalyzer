from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO
import re
from dataclasses import dataclass
from minor import minor

# Function takes the path to a pdf file and returns a string
def pdf_to_string(path):
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
    text = text.decode('utf-8')
    return text

# Function takes a string representation of the transcript and returns a list of strings that are the classes a student has taken or is taking
def unformatted_string_to_classes(text):
    sat_act_credit = act_sat_credit(text)
    print (sat_act_credit)

# Function takes a string representation of the transcript and returns a list of tuples that are classes a student has recieved credit for from the the act/sat
# Function is a helper function for unformatted_string_to_classes
# Currently the only class one can recieve credit for from the act/sat is rhet 105 it seems
# TODO: Obtain a transcript where a student does not have credit for RHET 105 and adapt this function for that case
# It could be possible to search the entire string for 'RHET' and if it doesn't exist return an empty list
def act_sat_credit(text):

    # Get the portion of the string that contains the credit earned from sat/act
    act_sat_unformatted = text[text.rfind('TRANSFER CREDIT ACCEPTED BY INSTITUTION'):text.rfind("Advanced Placement Tests")]
    
    # Convert that string into a list of all the lines in the string
    unformatted_string_list = act_sat_unformatted.split('\n')
    
    # Remove the empty strings in the list
    unformatted_string_list = [s for s in unformatted_string_list if s]

    courses_and_course_nums = []
    for s in unformatted_string_list:
        # Removes string in list that are not between length of 3 and 4 (Course codes are of either length 3 or 4 and course numbers are of length 3) 
        # Need to verify this though
        if (len(s) <= 4 and len(s) >= 3): 
            # Removes string that contain the substring '.' or 'GPA'
            if not ('.' in s) and not ('GPA' in s):
                courses_and_course_nums.append(s)

    # Set courses equal to the first half of courses_and_course_nums
    courses = courses_and_course_nums[:len(courses_and_course_nums)//2]
    # Set course_nums equal to the second half of courses_and_course_nums
    course_nums = courses_and_course_nums[len(courses_and_course_nums)//2:]

    # Create a list of tuples from the two lists
    course_and_nums_tuples = list(zip(courses, course_nums))
    
    return course_and_nums_tuples


unformatted_text = pdf_to_string('test.pdf') 
unformatted_string_to_classes(unformatted_text)