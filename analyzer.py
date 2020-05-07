from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO
import re

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
    classes_unformatted = classes_unformatted.replace("https://uachieve.apps.uillinois.edu/uachieve_uiuc/audit/read.html?printerFriendly=true&id=JobQueueRun!!!!ISEhIWludFNlcU5vPTMxMjczNDI=", "")
    lines = classes_unformatted.splitlines()
    lines = [line for line in lines if is_valid(line)]
    lines.remove('\uf00c')
    return lines

def is_valid(s):
    trans = re.sub('^([1-9]|1[012])[/]([0-9]|[1-9][0-9])[/](19|20)\d\d$', '', s) # checks for date in m/d/yy format (ugh hate this format why does it exist)
    trans = re.sub('^([1-9]|1[012])[/]([0-9]|[1-9][0-9])$', '', trans) # checks for date in m/d format (ugh again)
    return trans.strip()  # Empty strings are falsy which means they are considered false in a boolean context

def is_class(s):
    return not re.match('([0-9])', s) # lines is comprised of classes and their corresponding grades. Grades will start with a number while classes start with a character (indicating semester when class was taken)

def passed_class(x):
    #Need more info on how classes displayed in dars report for this
    passing_grades = ['PS', 'A', 'B', 'C', 'D-', 'S']
    grade = x[1]
    
    for pg in passing_grades:
        if pg in grade:
            return True

    return False

unformatted_text = pdf_to_text('dara2.pdf') 
lines = format_text_in_array(unformatted_text)
classes = [s for s in lines if is_class(s)]
grades = [s for s in lines if not is_class(s)]

merged = [(classes[i], grades[i]) for i in range(0, len(classes))]
passed_classes = [class_and_grade for class_and_grade in merged if passed_class(class_and_grade)]