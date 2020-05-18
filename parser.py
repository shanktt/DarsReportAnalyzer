from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO
import re
from dataclasses import dataclass
from minor import minor

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
    text = unformatted_text.decode('utf-8')
    return text

# @profile
def format_text_in_array(unformatted_text):
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




unformatted_text = pdf_to_text('test.pdf') 
print (unformatted_text.decode('utf-8'))\
# print (unformatted_text)