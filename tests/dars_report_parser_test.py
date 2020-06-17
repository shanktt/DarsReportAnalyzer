import pytest
from sys import path
path.append('/Users/ameyagharpure/DarsReportAnalyzer')
import dars_parser
import dars_filter
from os import linesep

class TestENGReports:
    class TestAmeya:
        def test_pdf_conversion(self):
            report = dars_parser.convert_pdf_text('dars_pdfs/ameya.pdf')
            pdf = linesep.join([s for s in report.splitlines() if s]) # remove all blank lines
            assert pdf != '' # ensure that ocr was used to read report

        def test_get_courses(self):
            report = dars_parser.convert_pdf_text('dars_pdfs/ameya.pdf')
            courses = dars_parser.get_courses_from_text(report)

            courses = '\t'.join(courses) # convert list into long string to make searching easier
            
            # assert all classes from summary of course list are present
            assert 'MATH 241' in courses
            assert 'CS 100' in courses
            assert 'CS 101' in courses
            assert 'CS 125' in courses
            assert 'CS 126' in courses
            assert 'CS 173' in courses
            assert 'ECON 1--' in courses
            assert 'ENG 100' in courses
            assert 'HIST 1--' in courses
            assert 'IB 150' in courses
            assert 'MATH 220' in courses
            assert 'MATH 231' in courses
            assert 'MATH 415' in courses
            assert 'MCB 150' in courses
            assert 'PHYS 2--' in courses
            assert 'PSYC 100' in courses
            assert 'RHET 105' in courses
            assert 'RST 242' in courses
            assert 'THEA 101' in courses
            assert 'CS 225' in courses
            assert 'CS 233' in courses
            assert 'CS 357' in courses
            assert 'KIN 249' in courses
            assert 'NRES 102' in courses
            assert 'CS 210' in courses
            assert 'CS 241' in courses
            assert 'CS 357' in courses
            assert 'REL 110' in courses

        def test_formatted_courses(self):
            report = dars_parser.convert_pdf_text('dars_pdfs/ameya.pdf')
            unformatted_courses = dars_parser.get_courses_from_text(report)
            courses = dars_parser.get_courses_num_grade_and_hours(unformatted_courses)

            # ensure course list is correct size
            assert len(courses) == 35

            # check all course info
            assert ('MATH', '241', '4.0', 'B+') in courses
            assert ('CS', '100', '1.0', 'A') in courses
            assert ('CS', '101', '3.0', 'PS') in courses
            assert ('CS', '125', '4.0', 'PS') in courses
            assert ('CS', '126', '3.0', 'A') in courses
            assert ('CS', '173', '3.0', 'B-') in courses
            assert ('ECON', '1--', '3.0', 'PS') in courses
            assert ('ENG', '100', '0.0', 'S') in courses
            assert ('HIST', '1--', '3.0', 'PS') in courses
            assert ('MATH', '220', '5.0', 'PS') in courses
            assert ('MATH', '231', '3.0', 'PS') in courses
            assert ('MATH', '415', '3.0', 'A') in courses
            assert ('MCB', '150', '4.0', 'PS') in courses
            assert ('PHYS', '2--', '4.0', 'PS') in courses
            assert ('PSYC', '100', '4.0', 'PS') in courses
            assert ('RHET', '105', '4.0', 'PS') in courses
            assert ('RST', '242', '3.0', 'A') in courses
            assert ('THEA', '101', '3.0', 'A+') in courses
            assert ('CS', '225', '4.0', 'IP') in courses
            assert ('CS', '233', '4.0', 'IP') in courses
            assert ('CS', '357', '3.0', 'IP') in courses
            assert ('KIN', '249', '3.0', 'IP') in courses
            assert ('NRES', '102', '3.0', 'IP') in courses
            assert ('CS', '210', '2.0', 'IP') in courses
            assert ('CS', '241', '4.0', 'IP') in courses
            assert ('CS', '357', '3.0', 'IP') in courses
            assert ('REL', '110', '3.0', 'IP') in courses
        
        def test_filter_invalid(self):
            report = dars_parser.convert_pdf_text('dars_pdfs/ameya.pdf')
            unformatted_courses = dars_parser.get_courses_from_text(report)
            unfiltered_courses = dars_parser.get_courses_num_grade_and_hours(unformatted_courses)
            courses = dars_filter.filter_classes(unfiltered_courses)

            assert len(courses) == 24 # should remove 7 invalid courses/4 duplicate
            assert len(courses) == len(set(courses)) # should remove duplicates (there are two ECON 1--)

            assert ('ECON', '1--', '3.0', 'PS') not in courses
            assert ('HIST', '1--', '3.0', 'PS') not in courses
            assert ('PHYS', '2--', '3.0', 'PS') not in courses

        def test_filter_into_courses(self):
            report = dars_parser.convert_pdf_text('dars_pdfs/ameya.pdf')
            unformatted_courses = dars_parser.get_courses_from_text(report)
            unfiltered_courses = dars_parser.get_courses_num_grade_and_hours(unformatted_courses)
            courses = dars_filter.filter_classes(unfiltered_courses)
            courses = dars_filter.put_into_courses(courses)

            assert len(courses) == 24 # ensure no data is lost

            assert ('MATH 241', 4.0) in courses
            assert ('CS 100', 1.0) in courses
            assert ('CS 101', 3.0) in courses
            assert ('CS 125', 4.0) in courses
            assert ('CS 126', 3.0) in courses
            assert ('CS 173', 3.0) in courses
            assert ('ENG 100', 0.0) in courses
            assert ('MATH 220', 5.0) in courses
            assert ('MATH 231', 3.0) in courses
            assert ('MATH 415', 3.0) in courses
            assert ('MCB 150', 4.0) in courses
            assert ('PSYC 100', 4.0) in courses
            assert ('RHET 105', 4.0) in courses
            assert ('RST 242', 3.0) in courses
            assert ('THEA 101', 3.0) in courses
            assert ('CS 225', 4.0) in courses
            assert ('CS 233', 4.0) in courses
            assert ('CS 357', 3.0) in courses
            assert ('KIN 249', 3.0) in courses
            assert ('NRES 102', 3.0) in courses
            assert ('CS 210', 2.0) in courses
            assert ('CS 241', 4.0) in courses
            assert ('CS 357', 3.0) in courses
            assert ('REL 110', 3.0) in courses
    
    
    class TestAmrith:
        def test_pdf_conversion(self):
            report = dars_parser.convert_pdf_text('dars_pdfs/amrith.pdf')
            pdf = linesep.join([s for s in report.splitlines() if s]) # remove all blank lines
            assert pdf != '' # ensure that ocr was used to read report

        def test_get_courses(self):
            report = dars_parser.convert_pdf_text('dars_pdfs/amrith.pdf')
            courses = dars_parser.get_courses_from_text(report)

            courses = '\t'.join(courses) # convert list into long string to make searching easier
            
            # assert all classes from summary of course list are present
            assert 'MATH 241' in courses
            assert 'CHEM 102' in courses
            assert 'CHEM 104' in courses
            assert 'CS 100' in courses
            assert 'CS 101' in courses
            assert 'CS 125' in courses
            assert 'CS 126' in courses
            assert 'CS 173' in courses
            assert 'CS 196' in courses
            assert 'ENG 100' in courses
            assert 'GEOG 1--' in courses
            assert 'HIST 1--' in courses
            assert 'MATH 220' in courses
            assert 'MATH 231' in courses
            assert 'MATH 415' in courses
            assert 'PHYS 211' in courses
            assert 'PHYS 212' in courses
            assert 'PSYC 100' in courses
            assert 'RHET 105' in courses
            assert 'RST 242' in courses
            assert 'THEA 101' in courses
            assert 'CS 225' in courses
            assert 'CS 233' in courses
            assert 'CS 357' in courses
            assert 'KIN 249' in courses
            assert 'ANSC 205' in courses
            assert 'CS 210' in courses
            assert 'CS 241' in courses
            assert 'CS 361' in courses
            assert 'SHS 222' in courses

        def test_formatted_courses(self):
            report = dars_parser.convert_pdf_text('dars_pdfs/amrith.pdf')
            unformatted_courses = dars_parser.get_courses_from_text(report)
            courses = dars_parser.get_courses_num_grade_and_hours(unformatted_courses)

            # ensure course list is correct size
            assert len(courses) == 34

            # check all course info
            assert ('MATH', '241', '4.0', 'A') in courses
            assert ('CHEM', '102', '3.0', 'PS') in courses
            assert ('CHEM', '104', '3.0', 'PS') in courses
            assert ('CS', '100', '1.0', 'A') in courses
            assert ('CS', '101', '3.0', 'PS') in courses
            assert ('CS', '125', '4.0', 'PS') in courses
            assert ('CS', '126', '3.0', 'A-') in courses
            assert ('CS', '173', '3.0', 'A') in courses
            assert ('CS', '196', '1.0', 'A') in courses
            assert ('ENG', '100', '0.0', 'S') in courses
            assert ('GEOG', '1--', '3.0', 'PS') in courses
            assert ('HIST', '1--', '3.0', 'PS') in courses
            assert ('MATH', '220', '5.0', 'PS') in courses
            assert ('MATH', '231', '3.0', 'PS') in courses
            assert ('MATH', '415', '3.0', 'A') in courses
            assert ('PHYS', '211', '4.0', 'PS') in courses
            assert ('PHYS', '212', '4.0', 'PS') in courses
            assert ('PSYC', '100', '4.0', 'PS') in courses
            assert ('RHET', '105', '4.0', 'PS') in courses
            assert ('RST', '242', '3.0', 'A') in courses
            assert ('THEA', '101', '3.0', 'A+') in courses
            assert ('CS', '225', '4.0', 'IP') in courses
            assert ('CS', '233', '4.0', 'IP') in courses
            assert ('CS', '357', '3.0', 'IP') in courses
            assert ('KIN', '249', '3.0', 'A+') in courses
            assert ('ANSC', '205', '3.0', 'IP') in courses
            assert ('CS', '210', '2.0', 'IP') in courses
            assert ('CS', '241', '4.0', 'IP') in courses
            assert ('CS', '361', '3.0', 'IP') in courses
            assert ('SHS', '222', '3.0', 'IP') in courses
        
        def test_filter_invalid(self):
            report = dars_parser.convert_pdf_text('dars_pdfs/amrith.pdf')
            unformatted_courses = dars_parser.get_courses_from_text(report)
            unfiltered_courses = dars_parser.get_courses_num_grade_and_hours(unformatted_courses)
            courses = dars_filter.filter_classes(unfiltered_courses)

            assert len(courses) == 28 # should remove 2 invalid courses/4 duplicate
            assert len(courses) == len(set(courses)) # should remove duplicates (there are two ECON 1--)

            assert ('GEOG', '1--', '3.0', 'PS') not in courses
            assert ('HIST', '1--', '3.0', 'PS') not in courses

        def test_filter_into_courses(self):
            report = dars_parser.convert_pdf_text('dars_pdfs/amrith.pdf')
            unformatted_courses = dars_parser.get_courses_from_text(report)
            unfiltered_courses = dars_parser.get_courses_num_grade_and_hours(unformatted_courses)
            courses = dars_filter.filter_classes(unfiltered_courses)
            courses = dars_filter.put_into_courses(courses)

            assert len(courses) == 28 # ensure no data is lost

            assert ('MATH 241', 4.0) in courses
            assert ('CHEM 102', 3.0) in courses
            assert ('CHEM 104', 3.0) in courses
            assert ('CS 100', 1.0) in courses
            assert ('CS 101', 3.0) in courses
            assert ('CS 125', 4.0) in courses
            assert ('CS 126', 3.0) in courses
            assert ('CS 173', 3.0) in courses
            assert ('CS 196', 1.0) in courses
            assert ('ENG 100', 0.0) in courses
            assert ('MATH 220', 5.0) in courses
            assert ('MATH 231', 3.0) in courses
            assert ('MATH 415', 3.0) in courses
            assert ('PHYS 211', 4.0) in courses
            assert ('PHYS 212', 4.0) in courses
            assert ('PSYC 100', 4.0) in courses
            assert ('RHET 105', 4.0) in courses
            assert ('RST 242', 3.0) in courses
            assert ('THEA 101', 3.0) in courses
            assert ('CS 225', 4.0) in courses
            assert ('CS 233', 4.0) in courses
            assert ('CS 357', 3.0) in courses
            assert ('KIN 249', 3.0) in courses
            assert ('ANSC 205', 3.0) in courses
            assert ('CS 210', 2.0) in courses
            assert ('CS 241', 4.0) in courses
            assert ('CS 361', 3.0) in courses
            assert ('SHS 222', 3.0) in courses

class TestLASReports:
    class TestAlex: 
        def test_pdf_conversion(self):
            report = dars_parser.convert_pdf_text('dars_pdfs/roe.pdf')
            pdf = linesep.join([s for s in report.splitlines() if s]) # remove all blank lines
            assert pdf != '' # ensure that ocr was used to read report

        def test_get_courses(self):
            report = dars_parser.convert_pdf_text('dars_pdfs/roe.pdf')
            courses = dars_parser.get_courses_from_text(report)

            courses = '\t'.join(courses) # convert list into long string to make searching easier
            
            # assert all classes from summary of course list are present
            
            assert 'MATH 241' in courses
            assert 'CS 100' in courses
            assert 'CS 101' in courses
            assert 'CS 125' in courses
            assert 'CS 126' in courses
            assert 'CS 173' in courses
            assert 'GEOG 1--' in courses
            assert 'HIST 1--' in courses
            assert 'HIST 142' in courses
            assert 'JAPN 203' in courses
            assert 'JAPN 204' in courses
            assert 'JAPN 305' in courses
            assert 'JAPN 306' in courses
            assert 'LAS 101' in courses
            assert 'LING 111' in courses
            assert 'MATH 220' in courses
            assert 'MATH 231' in courses
            assert 'MATH 347' in courses
            assert 'PHYS 211' in courses
            assert 'PHYS 212' in courses
            assert 'PSYC 1--' in courses
            assert 'PSYC 100' in courses
            assert 'RHET 105' in courses
            assert 'CS 225' in courses
            assert 'CS 233' in courses
            assert 'MATH 441' in courses
            assert 'STAT 200' in courses
            assert 'MATH 416' in courses
            assert 'MATH 461' in courses
            assert 'CS 241' in courses
            assert 'MATH 413' in courses
            assert 'MATH 453' in courses
            assert 'MATH 484' in courses

        def test_formatted_courses(self):
            report = dars_parser.convert_pdf_text('dars_pdfs/roe.pdf')
            unformatted_courses = dars_parser.get_courses_from_text(report)
            courses = dars_parser.get_courses_num_grade_and_hours(unformatted_courses)

            # ensure course list is correct size

            # ensure course list is correct size
            assert len(courses) == 34

            # check all course info
            assert ('MATH', '241', '4.0', 'A') in courses
            assert ('CS', '100', '1.0', 'A') in courses
            assert ('CS', '125', '4.0', 'PS') in courses
            assert ('CS', '126', '3.0', 'A+') in courses
            assert ('CS', '173', '3.0', 'PS') in courses
            assert ('GEOG', '1--', '3.0', 'PS') in courses
            assert ('HIST', '1--', '3.0', 'PS') in courses
            assert ('HIST', '142', '3.0', 'PS') in courses
            assert ('JAPN', '203', '5.0', 'PS') in courses
            assert ('JAPN', '204', '5.0', 'PS') in courses
            assert ('JAPN', '305', '5.0', 'PS') in courses
            assert ('JAPN', '306', '5.0', 'PS') in courses
            assert ('LAS', '101', '1.0', 'A+') in courses
            assert ('LING', '111', '3.0', 'B+') in courses
            assert ('MATH', '220', '5.0', 'PS') in courses
            assert ('MATH', '231', '3.0', 'PS') in courses
            assert ('MATH', '347', '3.0', 'B+') in courses
            assert ('PHYS', '211', '4.0', 'PS') in courses
            assert ('PHYS', '212', '4.0', 'PS') in courses
            assert ('PSYC', '1--', '3.0', 'PS') in courses
            assert ('PSYC', '100', '4.0', 'A-') in courses
            assert ('RHET', '105', '4.0', 'PS') in courses
            assert ('CS', '225', '4.0', 'IP') in courses
            assert ('CS', '233', '4.0', 'IP') in courses
            assert ('MATH', '441', '3.0', 'IP') in courses
            assert ('STAT', '200', '3.0', 'IP') in courses
            assert ('MATH', '416', '3.0', 'IP') in courses
            assert ('MATH', '461', '3.0', 'IP') in courses
            assert ('CS', '241', '4.0', 'IP') in courses
            assert ('CS', '450', '3.0', 'IP') in courses
            assert ('MATH', '413', '3.0', 'IP') in courses
            assert ('MATH', '453', '3.0', 'IP') in courses
            assert ('MATH', '484', '3.0', 'IP') in courses
        
        def test_filter_invalid(self):
            report = dars_parser.convert_pdf_text('dars_pdfs/roe.pdf')
            unformatted_courses = dars_parser.get_courses_from_text(report)
            unfiltered_courses = dars_parser.get_courses_num_grade_and_hours(unformatted_courses)
            courses = dars_filter.filter_classes(unfiltered_courses)

            assert len(courses) == 31 # should remove 3 invalid courses/1 duplicate
            assert len(courses) == len(set(courses)) # should remove duplicates (there are two ECON 1--)

            assert ('GEOG', '1--', '3.0', 'PS') not in courses
            assert ('HIST', '1--', '3.0', 'PS') not in courses
            assert ('PSYC', '1--', '3.0', 'PS') not in courses

        def test_filter_into_courses(self):
            report = dars_parser.convert_pdf_text('dars_pdfs/roe.pdf')
            unformatted_courses = dars_parser.get_courses_from_text(report)
            unfiltered_courses = dars_parser.get_courses_num_grade_and_hours(unformatted_courses)
            courses = dars_filter.filter_classes(unfiltered_courses)
            courses = dars_filter.put_into_courses(courses)

            assert len(courses) == 31 # ensure no data is lost

            assert ('MATH 241', 4.0) in courses
            assert ('CS 100', 1.0) in courses
            assert ('CS 125', 4.0) in courses
            assert ('CS 126', 3.0) in courses
            assert ('CS 173', 3.0) in courses
            assert ('HIST 142', 3.0) in courses
            assert ('JAPN 203', 5.0) in courses
            assert ('JAPN 204', 5.0) in courses
            assert ('JAPN 305', 5.0) in courses
            assert ('JAPN 306', 5.0) in courses
            assert ('LAS 101', 1.0) in courses
            assert ('LING 111', 3.0) in courses
            assert ('MATH 220', 5.0) in courses
            assert ('MATH 231', 3.0) in courses
            assert ('MATH 347', 3.0) in courses
            assert ('PHYS 211', 4.0) in courses
            assert ('PHYS 212', 4.0) in courses
            assert ('PSYC 100', 4.0) in courses
            assert ('RHET 105', 4.0) in courses
            assert ('CS 225', 4.0) in courses
            assert ('CS 233', 4.0) in courses
            assert ('MATH 441', 3.0) in courses
            assert ('STAT 200', 3.0) in courses
            assert ('MATH 416', 3.0) in courses
            assert ('MATH 461', 3.0) in courses
            assert ('CS 241', 4.0) in courses
            assert ('CS 450', 3.0) in courses
            assert ('MATH 413', 3.0) in courses
            assert ('MATH 453', 3.0) in courses
            assert ('MATH 484', 3.0) in courses
            
    class TestRaj:
        def test_pdf_conversion(self):
            report = dars_parser.convert_pdf_text('dars_pdfs/raj.pdf')
            pdf = linesep.join([s for s in report.splitlines() if s]) # remove all blank lines
            assert pdf != '' # ensure that ocr was used to read report

        def test_get_courses(self):
            report = dars_parser.convert_pdf_text('dars_pdfs/raj.pdf')
            courses = dars_parser.get_courses_from_text(report)

            courses = '\t'.join(courses) # convert list into long string to make searching easier
            
            # assert all classes from summary of course list are present
            assert 'CS 105' in courses
            assert 'ECON 202' in courses
            assert 'CMN 275' in courses
            assert 'CS 100' in courses
            assert 'CS 101' in courses
            assert 'CS 125' in courses
            assert 'LAS 101' in courses
            assert 'MATH 220' in courses
            assert 'MATH 231' in courses
            assert 'MATH 299' in courses
            assert 'RHET 105' in courses
            assert 'SOCW 240' in courses
            assert 'ASTR 100' in courses
            assert 'CS 126' in courses
            assert 'CS 173' in courses
            assert 'MATH 241' in courses
            assert 'REL 110' in courses
            assert 'CS 225' in courses
            assert 'CS 233' in courses
            assert 'MATH 415' in courses

        def test_formatted_courses(self):
            report = dars_parser.convert_pdf_text('dars_pdfs/raj.pdf')
            unformatted_courses = dars_parser.get_courses_from_text(report)
            courses = dars_parser.get_courses_num_grade_and_hours(unformatted_courses)

            assert len(courses) == 21

            # check all course info
            assert ('CS', '105', '4.0', 'TR') in courses
            assert ('ECON', '202', '4.0', 'TR') in courses
            assert ('CMN', '275', '3.0', 'A-') in courses
            assert ('CS', '100', '1.0', 'A') in courses
            assert ('CS', '101', '3.0', 'PS') in courses
            assert ('CS', '125', '4.0', 'PS') in courses
            assert ('LAS', '101', '1.0', 'A+') in courses
            assert ('MATH', '220', '5.0', 'PS') in courses
            assert ('MATH', '231', '3.0', 'B+') in courses
            assert ('MATH', '299', '1.0', 'B+') in courses
            assert ('RHET', '105', '4.0', 'PS') in courses
            assert ('SOCW', '240', '3.0', 'B+') in courses
            assert ('ASTR', '100', '3.0', 'A') in courses
            assert ('CS', '126', '3.0', 'A-') in courses
            assert ('CS', '173', '3.0', 'PP') in courses
            assert ('MATH', '241', '4.0', 'CR') in courses
            assert ('CS', '225', '4.0', 'IP') in courses
            assert ('CS', '233', '4.0', 'IP') in courses
            assert ('MATH', '415', '3.0', 'IP') in courses
            assert ('STAT', '400', '4.0', 'IP') in courses
            
        def test_filter_invalid(self):
            report = dars_parser.convert_pdf_text('dars_pdfs/raj.pdf')
            unformatted_courses = dars_parser.get_courses_from_text(report)
            unfiltered_courses = dars_parser.get_courses_num_grade_and_hours(unformatted_courses)
            courses = dars_filter.filter_classes(unfiltered_courses)

            assert len(courses) == 21 # nothing should change
            assert len(courses) == len(set(courses)) # should be the same

        def test_filter_into_courses(self):
            report = dars_parser.convert_pdf_text('dars_pdfs/raj.pdf')
            unformatted_courses = dars_parser.get_courses_from_text(report)
            unfiltered_courses = dars_parser.get_courses_num_grade_and_hours(unformatted_courses)
            courses = dars_filter.filter_classes(unfiltered_courses)
            courses = dars_filter.put_into_courses(courses)

            assert len(courses) == 21 # ensure no data is lost

            assert ('CS 105', 4.0) in courses
            assert ('ECON 202', 4.0) in courses
            assert ('CMN 275', 3.0) in courses
            assert ('CS 100', 1.0) in courses
            assert ('CS 101', 3.0) in courses
            assert ('CS 125', 4.0) in courses
            assert ('LAS 101', 1.0) in courses
            assert ('MATH 220', 5.0) in courses
            assert ('MATH 231', 3.0) in courses
            assert ('MATH 299', 1.0) in courses
            assert ('RHET 105', 4.0) in courses
            assert ('SOCW 240', 3.0) in courses
            assert ('ASTR 100', 3.0) in courses
            assert ('CS 126', 3.0) in courses
            assert ('CS 173', 3.0) in courses
            assert ('MATH 241', 4.0) in courses
            assert ('CS 225', 4.0) in courses
            assert ('CS 233', 4.0) in courses
            assert ('MATH 415', 3.0) in courses
            assert ('STAT 400', 4.0) in courses

class TestBusinessReports:
    class TestSunil:
        def test_pdf_conversion(self):
            report = dars_parser.convert_pdf_text('dars_pdfs/sunil.pdf')
            pdf = linesep.join([s for s in report.splitlines() if s]) # remove all blank lines
            assert pdf != '' # ensure the pdf is getting converted

        def test_get_courses(self):
            report = dars_parser.convert_pdf_text('dars_pdfs/sunil.pdf')
            courses = dars_parser.get_courses_from_text(report)

            courses = '\t'.join(courses) # convert list into long string to make searching easier
            
            # assert all classes from summary of course list are present
            assert 'BUS 101' in courses
            assert 'CI 210' in courses
            assert 'CMN 111' in courses
            assert 'ECON 1-- 3' in courses
            assert 'ECON 1-- 4' in courses
            assert 'ECON 102' in courses
            assert 'GEOG 1-- 7' in courses
            assert 'MATH 220' in courses
            assert 'RHET 1--' in courses
            assert 'RST 242' in courses
            assert 'STAT 1--' in courses
            assert 'CMN 112' in courses
            assert 'CS 105' in courses
            assert 'ECON 103' in courses
            assert 'FIN 221' in courses
            assert 'THEA 101' in courses
            assert 'ACCY 201' in courses
            assert 'BADM 310' in courses
            assert 'BADM 320' in courses
            assert 'BUS 201' in courses
            assert 'CLCV 224' in courses
            assert 'FSHN 120' in courses
            assert 'MATH 234' in courses

        def test_formatted_courses(self):
            report = dars_parser.convert_pdf_text('dars_pdfs/sunil.pdf')
            unformatted_courses = dars_parser.get_courses_from_text(report)
            courses = dars_parser.get_courses_num_grade_and_hours(unformatted_courses)

            # ensure course list is correct size
            assert len(courses) == 23

            # check all course info
            assert ('BUS', '101', '3.0', 'A') in courses
            assert ('CI', '210', '3.0', 'A') in courses
            assert ('CMN', '111', '3.0', 'A') in courses
            assert ('ECON', '1--', '3.0', 'PS') in courses
            assert ('ECON', '102', '3.0', 'A-') in courses
            assert ('GEOG', '1--', '3.0', 'PS') in courses
            assert ('MATH', '220', '5.0', 'PS') in courses
            assert ('RHET', '1--', '3.0', 'PS') in courses
            assert ('RST', '242', '3.0', 'A') in courses
            assert ('STAT', '1--', '3.0', 'PS') in courses
            assert ('CMN', '112', '3.0', 'IP') in courses
            assert ('CS', '105', '3.0', 'IP') in courses
            assert ('ECON', '103', '3.0', 'IP') in courses
            assert ('FIN', '221', '3.0', 'IP') in courses
            assert ('THEA', '101', '3.0', 'IP') in courses
            assert ('BADM', '310', '3.0', 'IP') in courses
            assert ('BADM', '320', '3.0', 'IP') in courses
            assert ('BUS', '201', '3.0', 'IP') in courses
            assert ('CLCV', '224', '3.0', 'IP') in courses
            assert ('FSHN', '120', '3.0', 'IP') in courses
            assert ('MATH', '234', '4.0', 'PS') in courses

        def test_filter_invalid(self):
            report = dars_parser.convert_pdf_text('dars_pdfs/sunil.pdf')
            unformatted_courses = dars_parser.get_courses_from_text(report)
            unfiltered_courses = dars_parser.get_courses_num_grade_and_hours(unformatted_courses)
            courses = dars_filter.filter_classes(unfiltered_courses)

            assert len(courses) == 18 # should remove 5 invalid courses
            assert len(courses) == len(set(courses)) # should remove duplicates (there are two ECON 1--)

            assert ('ECON', '1--', '3.0', 'PS') not in courses
            assert ('GEOG', '1--', '3.0', 'PS') not in courses
            assert ('RHET', '1--', '3.0', 'PS') not in courses
            assert ('STAT', '1--', '3.0', 'PS') not in courses
        
        def test_filter_into_courses(self):
            report = dars_parser.convert_pdf_text('dars_pdfs/sunil.pdf')
            unformatted_courses = dars_parser.get_courses_from_text(report)
            unfiltered_courses = dars_parser.get_courses_num_grade_and_hours(unformatted_courses)
            courses = dars_filter.filter_classes(unfiltered_courses)
            courses = dars_filter.put_into_courses(courses)

            assert len(courses) == 18 # ensure no data is lost

            assert ('BUS 101', 3.0) in courses
            assert ('CI 210', 3.0) in courses
            assert ('CMN 111', 3.0) in courses
            assert ('ECON 102', 3.0) in courses
            assert ('MATH 220', 5.0) in courses
            assert ('RST 242', 3.0) in courses
            assert ('CMN 112', 3.0) in courses
            assert ('CS 105', 3.0) in courses
            assert ('ECON 103', 3.0) in courses
            assert ('FIN 221', 3.0) in courses
            assert ('THEA 101', 3.0) in courses
            assert ('ACCY 201', 3.0) in courses
            assert ('BADM 310', 3.0) in courses
            assert ('BADM 320', 3.0) in courses
            assert ('BUS 201', 3.0) in courses
            assert ('CLCV 224', 3.0) in courses
            assert ('FSHN 120', 3.0) in courses
            assert ('MATH 234', 4.0) in courses



        



report = dars_parser.convert_pdf_text('dars_pdfs/amrith.pdf')
unformatted_courses = dars_parser.get_courses_from_text(report)
unfiltered_courses = dars_parser.get_courses_num_grade_and_hours(unformatted_courses)
courses = dars_filter.filter_classes(unfiltered_courses)
courses = dars_filter.put_into_courses(courses)

print(*unfiltered_courses, sep='\n')
        
    

