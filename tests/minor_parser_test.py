# .raises ex: with pytest.raises(RuntimeError) as excinfo:
# pytest if in directory or pytest --pyargs tests/
import pytest
from sys import path
path.append('/Users/ameyagharpure/DarsReportAnalyzer')
import minor_parser

dataframe = minor_parser.create_pd('/Users/ameyagharpure/DarsReportAnalyzer/minor_data/minor_data.csv')
minors = minor_parser.create_minors(dataframe)

class TestAdultDevelopment:
    minor = minors[0]

    def test_required_groups(self):
        group_list = TestAdultDevelopment.minor.required_groups

        assert len(group_list) == 2

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 3
        
        assert ('HDFS 225', False) in group.courses
        assert ('HDFS 425', False) in group.courses
        assert ('HDFS 426', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'H'
        assert group.goal_num == 6

        assert len(group.courses) == 12
        
        assert ('AGED 490', False) in group.courses
        assert ('CMN 336', False) in group.courses
        assert ('CMN 368', False) in group.courses
        assert ('HDFS 404', True) in group.courses
        assert ('PSYC 361', False) in group.courses
        assert ('RST 316', False) in group.courses
        assert ('SOCW 240', False) in group.courses
        assert ('SOCW 315', False) in group.courses
        assert ('HDFS 294', False) in group.courses
        assert ('HDFS 450', False) in group.courses
        assert ('HDFS 494', False) in group.courses

        assert len(group.repl_courses) == 1
        assert ('HDFS 404', 'CHLH 404') in group.repl_courses

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestAdultDevelopment.minor.required_courses

        # test length of the list
        assert len(courses) == 3

        # test for (course, if replacement course is available)
        assert ('HDFS 105', False) in courses
        assert ('HDFS 120', False) in courses
        assert ('HDFS 310', False) in courses

    def test_repl_courses(self):
        courses = TestAdultDevelopment.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestAdultDevelopment.minor.name
        credit = TestAdultDevelopment.minor.total_credits

        assert name == 'ADULT DEVELOPMENT'
        assert credit == 18

class TestAging:
    minor = minors[1]

    def test_required_groups(self):
        group_list = TestAging.minor.required_groups

        assert len(group_list) == 1

        # test first group
        group = group_list[0]

        assert group.goal_type == 'H'
        assert group.goal_num == 9

        assert len(group.courses) == 10
        
        assert ('KIN 459', False) in group.courses
        assert ('SOCW 240', False) in group.courses
        assert ('SOCW 315', False) in group.courses
        assert ('CHLH 494', False) in group.courses
        assert ('RST 316', False) in group.courses
        assert ('RST 335', False) in group.courses
        assert ('SHS 271', False) in group.courses
        assert ('KIN 386', False) in group.courses
        assert ('EPSY 407', False) in group.courses
        assert ('UP 340', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestAging.minor.required_courses

        # test length of the list
        assert len(courses) == 3

        # test for (course, if replacement course is available)
        assert ('IHLT 240', False) in courses
        assert ('CHLH 404', False) in courses
        assert ('PSYC 361', False) in courses

    def test_repl_courses(self):
        courses = TestAging.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestAging.minor.name
        credit = TestAging.minor.total_credits

        assert name == 'AGING'
        assert credit == 18

class TestAgriculturalSafetyAndHealth:
    minor = minors[2]

    def test_required_groups(self):
        group_list = TestAgriculturalSafetyAndHealth.minor.required_groups

        assert len(group_list) == 2

        # test first group
        group = group_list[0]

        assert group.goal_type == 'H'
        assert group.goal_num == 3

        assert len(group.courses) == 3
        
        assert ('TSM 293', False) in group.courses
        assert ('TSM 295', False) in group.courses
        assert ('TSM 496', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'H'
        assert group.goal_num == 6

        assert len(group.courses) == 14
        
        assert ('CHLH 101', False) in group.courses
        assert ('CHLH 244', False) in group.courses
        assert ('CHLH 274', False) in group.courses
        assert ('CHLH 304', False) in group.courses
        assert ('CHLH 469', False) in group.courses
        assert ('CHLH 474', False) in group.courses
        assert ('CHLH 540', False) in group.courses
        assert ('FSHN 480', False) in group.courses
        assert ('HDFS 105', False) in group.courses
        assert ('KIN 262', False) in group.courses
        assert ('PSYC 100', False) in group.courses
        assert ('PSYC 103', False) in group.courses
        assert ('PSYC 358', False) in group.courses
        assert ('PSYC 456', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestAgriculturalSafetyAndHealth.minor.required_courses

        # test length of the list
        assert len(courses) == 3

        # test for (course, if replacement course is available)
        assert ('TSM 421', False) in courses
        assert ('TSM 422', False) in courses
        assert ('TSM 425', False) in courses

    def test_repl_courses(self):
        courses = TestAgriculturalSafetyAndHealth.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestAgriculturalSafetyAndHealth.minor.name
        credit = TestAgriculturalSafetyAndHealth.minor.total_credits

        assert name == 'Agricultural Safety & Health'.upper()
        assert credit == 18

class TestAnimalSciences:
    minor = minors[3]

    def test_required_groups(self):
        group_list = TestAnimalSciences.minor.required_groups

        assert len(group_list) == 2

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 2

        assert len(group.courses) == 4
        
        assert ('ANSC 223', False) in group.courses
        assert ('ANSC 224', False) in group.courses
        assert ('ANSC 221', False) in group.courses
        assert ('ANSC 222', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'C'
        assert group.goal_num == 2

        assert len(group.courses) == 49

        assert ('ANSC 301', False) in group.courses
        assert ('ANSC 305', False) in group.courses
        assert ('ANSC 306', False) in group.courses
        assert ('ANSC 307', False) in group.courses
        assert ('ANSC 309', False) in group.courses
        assert ('ANSC 310', False) in group.courses
        assert ('ANSC 312', False) in group.courses
        assert ('ANSC 313', False) in group.courses
        assert ('ANSC 314', False) in group.courses
        assert ('ANSC 322', False) in group.courses
        assert ('ANSC 331', False) in group.courses
        assert ('ANSC 350', False) in group.courses
        assert ('ANSC 363', False) in group.courses
        assert ('ANSC 366', False) in group.courses
        assert ('ANSC 370', False) in group.courses
        assert ('ANSC 396', False) in group.courses
        assert ('ANSC 400', False) in group.courses
        assert ('ANSC 401', False) in group.courses
        assert ('ANSC 402', False) in group.courses
        assert ('ANSC 403', False) in group.courses
        assert ('ANSC 404', False) in group.courses
        assert ('ANSC 405', False) in group.courses
        assert ('ANSC 406', False) in group.courses
        assert ('ANSC 407', False) in group.courses
        assert ('ANSC 409', False) in group.courses
        assert ('ANSC 420', False) in group.courses
        assert ('ANSC 421', False) in group.courses
        assert ('ANSC 422', False) in group.courses
        assert ('ANSC 423', False) in group.courses
        assert ('ANSC 424', False) in group.courses
        assert ('ANSC 431', False) in group.courses
        assert ('ANSC 435', False) in group.courses
        assert ('ANSC 437', False) in group.courses
        assert ('ANSC 438', False) in group.courses
        assert ('ANSC 440', False) in group.courses
        assert ('ANSC 441', False) in group.courses
        assert ('ANSC 444', False) in group.courses
        assert ('ANSC 445', False) in group.courses
        assert ('ANSC 446', False) in group.courses
        assert ('ANSC 447', False) in group.courses
        assert ('ANSC 448', False) in group.courses
        assert ('ANSC 449', False) in group.courses
        assert ('ANSC 450', False) in group.courses
        assert ('ANSC 451', False) in group.courses
        assert ('ANSC 452', False) in group.courses
        assert ('ANSC 453', False) in group.courses
        assert ('ANSC 467', False) in group.courses
        assert ('ANSC 471', False) in group.courses
        assert ('ANSC 498', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 2

        assert 'ANSC 398' in group.unallowed_courses
        assert 'ANSC 499' in group.unallowed_courses

    def test_required_courses(self):
        courses = TestAnimalSciences.minor.required_courses

        # test length of the list
        assert len(courses) == 2

        # test for (course, if replacement course is available)
        assert ('ANSC 100', False) in courses
        assert ('ANSC 101', False) in courses

    def test_repl_courses(self):
        courses = TestAnimalSciences.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestAnimalSciences.minor.name
        credit = TestAnimalSciences.minor.total_credits

        assert name == 'Animal Sciences'.upper()
        assert credit == 20

class TestAnthropology:
    minor = minors[4]

    def test_required_groups(self):
        group_list = TestAnthropology.minor.required_groups

        assert len(group_list) == 3

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 2

        assert len(group.courses) == 4
        
        assert ('ANTH 220', False) in group.courses
        assert ('ANTH 230', False) in group.courses
        assert ('ANTH 240', False) in group.courses
        assert ('ANTH 270', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'H'
        assert group.goal_num == 6


        assert len(group.courses) == 78

        assert ('ANTH 340', False) in group.courses
        assert ('ANTH 341', False) in group.courses
        assert ('ANTH 342', False) in group.courses
        assert ('ANTH 343', False) in group.courses
        assert ('ANTH 346', False) in group.courses
        assert ('ANTH 347', False) in group.courses
        assert ('ANTH 358', False) in group.courses
        assert ('ANTH 360', False) in group.courses
        assert ('ANTH 361', False) in group.courses
        assert ('ANTH 362', False) in group.courses
        assert ('ANTH 363', False) in group.courses
        assert ('ANTH 364', False) in group.courses
        assert ('ANTH 368', False) in group.courses
        assert ('ANTH 370', False) in group.courses
        assert ('ANTH 372', False) in group.courses
        assert ('ANTH 373', False) in group.courses
        assert ('ANTH 374', False) in group.courses
        assert ('ANTH 375', False) in group.courses
        assert ('ANTH 379', False) in group.courses
        assert ('ANTH 380', False) in group.courses
        assert ('ANTH 390', False) in group.courses
        assert ('ANTH 393', False) in group.courses
        assert ('ANTH 399', False) in group.courses
        assert ('ANTH 402', False) in group.courses
        assert ('ANTH 403', False) in group.courses
        assert ('ANTH 404', False) in group.courses
        assert ('ANTH 405', False) in group.courses
        assert ('ANTH 408', False) in group.courses
        assert ('ANTH 411', False) in group.courses
        assert ('ANTH 414', False) in group.courses
        assert ('ANTH 416', False) in group.courses
        assert ('ANTH 420', False) in group.courses
        assert ('ANTH 421', False) in group.courses
        assert ('ANTH 423', False) in group.courses
        assert ('ANTH 425', False) in group.courses
        assert ('ANTH 430', False) in group.courses
        assert ('ANTH 432', False) in group.courses
        assert ('ANTH 435', False) in group.courses
        assert ('ANTH 436', False) in group.courses
        assert ('ANTH 437', False) in group.courses
        assert ('ANTH 438', False) in group.courses
        assert ('ANTH 440', False) in group.courses
        assert ('ANTH 441', False) in group.courses
        assert ('ANTH 443', False) in group.courses
        assert ('ANTH 444', False) in group.courses
        assert ('ANTH 445', False) in group.courses
        assert ('ANTH 446', False) in group.courses
        assert ('ANTH 447', False) in group.courses
        assert ('ANTH 448', False) in group.courses
        assert ('ANTH 449', False) in group.courses
        assert ('ANTH 451', False) in group.courses
        assert ('ANTH 452', False) in group.courses
        assert ('ANTH 453', False) in group.courses
        assert ('ANTH 454', False) in group.courses
        assert ('ANTH 455', False) in group.courses
        assert ('ANTH 459', False) in group.courses
        assert ('ANTH 460', False) in group.courses
        assert ('ANTH 461', False) in group.courses
        assert ('ANTH 462', False) in group.courses
        assert ('ANTH 463', False) in group.courses
        assert ('ANTH 464', False) in group.courses
        assert ('ANTH 465', False) in group.courses
        assert ('ANTH 466', False) in group.courses
        assert ('ANTH 467', False) in group.courses
        assert ('ANTH 469', False) in group.courses
        assert ('ANTH 471', False) in group.courses
        assert ('ANTH 472', False) in group.courses
        assert ('ANTH 477', False) in group.courses
        assert ('ANTH 479', False) in group.courses
        assert ('ANTH 481', False) in group.courses
        assert ('ANTH 486', False) in group.courses
        assert ('ANTH 488', False) in group.courses
        assert ('ANTH 494', False) in group.courses
        assert ('ANTH 495', False) in group.courses
        assert ('ANTH 496', False) in group.courses
        assert ('ANTH 497', False) in group.courses
        assert ('ANTH 498', False) in group.courses
        assert ('ANTH 499', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test third group
        group = group_list[2]

        assert group.goal_type == 'H'
        assert group.goal_num == 6

        
        assert len(group.courses) == 151

        assert ('ANTH 101', False) in group.courses
        assert ('ANTH 102', False) in group.courses
        assert ('ANTH 103', False) in group.courses
        assert ('ANTH 104', False) in group.courses
        assert ('ANTH 105', False) in group.courses
        assert ('ANTH 106', False) in group.courses
        assert ('ANTH 108', False) in group.courses
        assert ('ANTH 109', False) in group.courses
        assert ('ANTH 130', False) in group.courses
        assert ('ANTH 143', False) in group.courses
        assert ('ANTH 157', False) in group.courses
        assert ('ANTH 160', False) in group.courses
        assert ('ANTH 165', False) in group.courses
        assert ('ANTH 175', False) in group.courses
        assert ('ANTH 180', False) in group.courses
        assert ('ANTH 182', False) in group.courses
        assert ('ANTH 199', False) in group.courses
        assert ('ANTH 209', False) in group.courses
        assert ('ANTH 210', False) in group.courses
        assert ('ANTH 220', False) in group.courses
        assert ('ANTH 222', False) in group.courses
        assert ('ANTH 223', False) in group.courses
        assert ('ANTH 224', False) in group.courses
        assert ('ANTH 225', False) in group.courses
        assert ('ANTH 230', False) in group.courses
        assert ('ANTH 240', False) in group.courses
        assert ('ANTH 241', False) in group.courses
        assert ('ANTH 242', False) in group.courses
        assert ('ANTH 243', False) in group.courses
        assert ('ANTH 246', False) in group.courses
        assert ('ANTH 247', False) in group.courses
        assert ('ANTH 249', False) in group.courses
        assert ('ANTH 250', False) in group.courses
        assert ('ANTH 258', False) in group.courses
        assert ('ANTH 259', False) in group.courses
        assert ('ANTH 261', False) in group.courses
        assert ('ANTH 262', False) in group.courses
        assert ('ANTH 266', False) in group.courses
        assert ('ANTH 268', False) in group.courses
        assert ('ANTH 270', False) in group.courses
        assert ('ANTH 271', False) in group.courses
        assert ('ANTH 272', False) in group.courses
        assert ('ANTH 277', False) in group.courses
        assert ('ANTH 278', False) in group.courses
        assert ('ANTH 285', False) in group.courses
        assert ('ANTH 286', False) in group.courses
        assert ('ANTH 287', False) in group.courses
        assert ('ANTH 288', False) in group.courses
        assert ('ANTH 290', False) in group.courses
        assert ('ANTH 340', False) in group.courses
        assert ('ANTH 341', False) in group.courses
        assert ('ANTH 342', False) in group.courses
        assert ('ANTH 343', False) in group.courses
        assert ('ANTH 346', False) in group.courses
        assert ('ANTH 347', False) in group.courses
        assert ('ANTH 358', False) in group.courses
        assert ('ANTH 360', False) in group.courses
        assert ('ANTH 361', False) in group.courses
        assert ('ANTH 362', False) in group.courses
        assert ('ANTH 363', False) in group.courses
        assert ('ANTH 364', False) in group.courses
        assert ('ANTH 368', False) in group.courses
        assert ('ANTH 370', False) in group.courses
        assert ('ANTH 372', False) in group.courses
        assert ('ANTH 373', False) in group.courses
        assert ('ANTH 374', False) in group.courses
        assert ('ANTH 375', False) in group.courses
        assert ('ANTH 379', False) in group.courses
        assert ('ANTH 380', False) in group.courses
        assert ('ANTH 390', False) in group.courses
        assert ('ANTH 393', False) in group.courses
        assert ('ANTH 399', False) in group.courses 
        assert ('ANTH 402', False) in group.courses
        assert ('ANTH 403', False) in group.courses
        assert ('ANTH 404', False) in group.courses
        assert ('ANTH 405', False) in group.courses
        assert ('ANTH 408', False) in group.courses
        assert ('ANTH 411', False) in group.courses
        assert ('ANTH 414', False) in group.courses
        assert ('ANTH 416', False) in group.courses
        assert ('ANTH 420', False) in group.courses
        assert ('ANTH 421', False) in group.courses
        assert ('ANTH 423', False) in group.courses
        assert ('ANTH 425', False) in group.courses
        assert ('ANTH 430', False) in group.courses
        assert ('ANTH 432', False) in group.courses
        assert ('ANTH 435', False) in group.courses
        assert ('ANTH 436', False) in group.courses
        assert ('ANTH 437', False) in group.courses
        assert ('ANTH 438', False) in group.courses
        assert ('ANTH 440', False) in group.courses
        assert ('ANTH 441', False) in group.courses
        assert ('ANTH 443', False) in group.courses
        assert ('ANTH 444', False) in group.courses
        assert ('ANTH 445', False) in group.courses
        assert ('ANTH 446', False) in group.courses
        assert ('ANTH 447', False) in group.courses
        assert ('ANTH 448', False) in group.courses
        assert ('ANTH 449', False) in group.courses
        assert ('ANTH 451', False) in group.courses
        assert ('ANTH 452', False) in group.courses
        assert ('ANTH 453', False) in group.courses
        assert ('ANTH 454', False) in group.courses
        assert ('ANTH 455', False) in group.courses
        assert ('ANTH 459', False) in group.courses
        assert ('ANTH 460', False) in group.courses
        assert ('ANTH 461', False) in group.courses
        assert ('ANTH 462', False) in group.courses
        assert ('ANTH 463', False) in group.courses
        assert ('ANTH 464', False) in group.courses
        assert ('ANTH 465', False) in group.courses
        assert ('ANTH 466', False) in group.courses
        assert ('ANTH 467', False) in group.courses
        assert ('ANTH 469', False) in group.courses
        assert ('ANTH 471', False) in group.courses
        assert ('ANTH 472', False) in group.courses
        assert ('ANTH 477', False) in group.courses
        assert ('ANTH 479', False) in group.courses
        assert ('ANTH 481', False) in group.courses
        assert ('ANTH 486', False) in group.courses
        assert ('ANTH 488', False) in group.courses
        assert ('ANTH 494', False) in group.courses
        assert ('ANTH 495', False) in group.courses
        assert ('ANTH 496', False) in group.courses
        assert ('ANTH 497', False) in group.courses
        assert ('ANTH 498', False) in group.courses
        assert ('ANTH 499', False) in group.courses
        assert ('ANTH 503', False) in group.courses
        assert ('ANTH 504', False) in group.courses
        assert ('ANTH 508', False) in group.courses
        assert ('ANTH 511', False) in group.courses
        assert ('ANTH 512', False) in group.courses
        assert ('ANTH 514', False) in group.courses
        assert ('ANTH 515', False) in group.courses
        assert ('ANTH 517', False) in group.courses
        assert ('ANTH 518', False) in group.courses
        assert ('ANTH 523', False) in group.courses
        assert ('ANTH 532', False) in group.courses
        assert ('ANTH 540', False) in group.courses
        assert ('ANTH 543', False) in group.courses
        assert ('ANTH 552', False) in group.courses
        assert ('ANTH 555', False) in group.courses
        assert ('ANTH 557', False) in group.courses
        assert ('ANTH 560', False) in group.courses
        assert ('ANTH 561', False) in group.courses
        assert ('ANTH 562', False) in group.courses
        assert ('ANTH 565', False) in group.courses
        assert ('ANTH 570', False) in group.courses
        assert ('ANTH 589', False) in group.courses
        assert ('ANTH 590', False) in group.courses
        assert ('ANTH 594', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestAnthropology.minor.required_courses

        # test length of the list
        assert len(courses) == 0

    def test_repl_courses(self):
        courses = TestAnthropology.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestAnthropology.minor.name
        credit = TestAnthropology.minor.total_credits

        assert name == 'Anthropology'.upper()
        assert credit == 18

class TestArchitecturalStudies:
    minor = minors[5]

    def test_required_groups(self):
        group_list = TestArchitecturalStudies.minor.required_groups

        assert len(group_list) == 1

        # test first group
        group = group_list[0]

        assert group.goal_type == 'H'
        assert group.goal_num == 6

        assert len(group.courses) == 15

        assert ('ARCH 321', False) in group.courses
        assert ('ARCH 434', False) in group.courses
        assert ('ARCH 314', False) in group.courses
        assert ('ARCH 402', False) in group.courses
        assert ('ARCH 403', False) in group.courses
        assert ('ARCH 407', False) in group.courses
        assert ('ARCH 410', False) in group.courses
        assert ('ARCH 411', False) in group.courses
        assert ('ARCH 412', False) in group.courses
        assert ('ARCH 413', False) in group.courses
        assert ('ARCH 414', False) in group.courses
        assert ('ARCH 415', False) in group.courses
        assert ('ARCH 416', False) in group.courses
        assert ('ARCH 417', False) in group.courses
        assert ('ARCH 418', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestArchitecturalStudies.minor.required_courses

        # test length of the list
        assert len(courses) == 4

        # test for (course, if replacement course is available)
        assert ('ARCH 171', False) in courses
        assert ('ARCH 210', False) in courses
        assert ('ARCH 231', False) in courses
        assert ('ARCH 273', False) in courses
        

    def test_repl_courses(self):
        courses = TestArchitecturalStudies.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestArchitecturalStudies.minor.name
        credit = TestArchitecturalStudies.minor.total_credits

        assert name == 'Architectural Studies'.upper()
        assert credit == 19

class TestAsianAmericanStudies:
    minor = minors[6]

    def test_required_groups(self):
        group_list = TestAsianAmericanStudies.minor.required_groups

        assert len(group_list) == 2

        # test first group
        group = group_list[0]

        assert group.goal_type == 'H'
        assert group.goal_num == 3

        assert len(group.courses) == 44

        assert ('AAS 100', False) in group.courses
        assert ('AAS 105', False) in group.courses
        assert ('AAS 120', False) in group.courses
        assert ('AAS 199', False) in group.courses
        assert ('AAS 200', False) in group.courses
        assert ('AAS 201', False) in group.courses
        assert ('AAS 211', False) in group.courses
        assert ('AAS 215', False) in group.courses
        assert ('AAS 224', False) in group.courses
        assert ('AAS 246', False) in group.courses
        assert ('AAS 258', False) in group.courses
        assert ('AAS 260', False) in group.courses
        assert ('AAS 265', False) in group.courses
        assert ('AAS 275', False) in group.courses
        assert ('AAS 281', False) in group.courses
        assert ('AAS 282', False) in group.courses
        assert ('AAS 283', False) in group.courses
        assert ('AAS 286', False) in group.courses
        assert ('AAS 287', False) in group.courses
        assert ('AAS 288', False) in group.courses
        assert ('AAS 290', False) in group.courses
        assert ('AAS 291', False) in group.courses
        assert ('AAS 297', False) in group.courses
        assert ('AAS 299', False) in group.courses
        assert ('AAS 300', False) in group.courses
        assert ('AAS 310', False) in group.courses
        assert ('AAS 315', False) in group.courses
        assert ('AAS 317', False) in group.courses
        assert ('AAS 328', False) in group.courses
        assert ('AAS 343', False) in group.courses
        assert ('AAS 346', False) in group.courses
        assert ('AAS 355', False) in group.courses
        assert ('AAS 365', False) in group.courses
        assert ('AAS 370', False) in group.courses
        assert ('AAS 375', False) in group.courses
        assert ('AAS 390', False) in group.courses
        assert ('AAS 395', False) in group.courses
        assert ('AAS 400', False) in group.courses
        assert ('AAS 402', False) in group.courses
        assert ('AAS 435', False) in group.courses
        assert ('AAS 464', False) in group.courses
        assert ('AAS 465', False) in group.courses
        assert ('AAS 479', False) in group.courses
        assert ('AAS 490', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'H'
        assert group.goal_num == 3

        assert len(group.courses) == 20

        assert ('AAS 300', False) in group.courses
        assert ('AAS 310', False) in group.courses
        assert ('AAS 315', False) in group.courses
        assert ('AAS 317', False) in group.courses
        assert ('AAS 328', False) in group.courses
        assert ('AAS 343', False) in group.courses
        assert ('AAS 346', False) in group.courses
        assert ('AAS 355', False) in group.courses
        assert ('AAS 365', False) in group.courses
        assert ('AAS 370', False) in group.courses
        assert ('AAS 375', False) in group.courses
        assert ('AAS 390', False) in group.courses
        assert ('AAS 395', False) in group.courses
        assert ('AAS 400', False) in group.courses
        assert ('AAS 402', False) in group.courses
        assert ('AAS 435', False) in group.courses
        assert ('AAS 464', False) in group.courses
        assert ('AAS 465', False) in group.courses
        assert ('AAS 479', False) in group.courses
        assert ('AAS 490', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestAsianAmericanStudies.minor.required_courses

        # test length of the list
        assert len(courses) == 4

        # test for (course, if replacement course is available)
        assert ('AAS 100', False) in courses
        assert ('AAS 200', False) in courses
        assert ('AAS 215', False) in courses
        assert ('AAS 300', False) in courses
        

    def test_repl_courses(self):
        courses = TestAsianAmericanStudies.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestAsianAmericanStudies.minor.name
        credit = TestAsianAmericanStudies.minor.total_credits

        assert name == 'Asian American Studies'.upper()
        assert credit == 18

class TestBusinessForNonMajors:
    minor = minors[7]

    def test_required_groups(self):
        group_list = TestBusinessForNonMajors.minor.required_groups

        assert len(group_list) == 1

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 2

        assert len(group.courses) == 13

        assert ('BADM 300', False) in group.courses
        assert ('BADM 311', False) in group.courses
        assert ('BADM 312', False) in group.courses
        assert ('BADM 313', False) in group.courses
        assert ('BADM 314', False) in group.courses
        assert ('BADM 323', False) in group.courses
        assert ('BADM 326', False) in group.courses
        assert ('BADM 340', False) in group.courses
        assert ('BADM 350', False) in group.courses
        assert ('BADM 367', False) in group.courses
        assert ('BADM 375', False) in group.courses
        assert ('BADM 380', False) in group.courses
        assert ('BADM 381', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestBusinessForNonMajors.minor.required_courses

        # test length of the list
        assert len(courses) == 4

        # test for (course, if replacement course is available)
        assert ('ACCY 200', False) in courses
        assert ('BAMD 310', False) in courses
        assert ('BADM 320', False) in courses
        assert ('FIN 221', False) in courses
        

    def test_repl_courses(self):
        courses = TestBusinessForNonMajors.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestBusinessForNonMajors.minor.name
        credit = TestBusinessForNonMajors.minor.total_credits

        assert name == 'Business Minor for Non-Business Majors'.upper()
        assert credit == 18

class TestCinemaStudies:
    minor = minors[8]

    def test_required_groups(self):
        group_list = TestCinemaStudies.minor.required_groups

        assert len(group_list) == 2

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 23

        assert ('MACS 207', False) in group.courses
        assert ('MACS 382', False) in group.courses
        assert ('MACS 383', False) in group.courses
        assert ('MACS 419', False) in group.courses
        assert ('MACS 466', False) in group.courses
        assert ('MACS 470', False) in group.courses
        assert ('MACS 490', False) in group.courses
        assert ('MACS 493', False) in group.courses
        assert ('ITAL 270', False) in group.courses
        assert ('MACS 205', False) in group.courses
        assert ('MACS 211', False) in group.courses
        assert ('MACS 250', False) in group.courses
        assert ('MACS 335', False) in group.courses
        assert ('MACS 356', False) in group.courses
        assert ('MACS 365', False) in group.courses
        assert ('MACS 375', False) in group.courses
        assert ('MACS 381', False) in group.courses
        assert ('MACS 432', False) in group.courses
        assert ('MACS 461', False) in group.courses
        assert ('MDIA 223', False) in group.courses
        assert ('MDIA 380', False) in group.courses
        assert ('ENGL 272', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 44

        assert ('MACS 300', False) in group.courses
        assert ('MACS 317', False) in group.courses
        assert ('MACS 320', False) in group.courses
        assert ('MACS 321', False) in group.courses
        assert ('MACS 322', False) in group.courses
        assert ('MACS 323', False) in group.courses
        assert ('MACS 326', False) in group.courses
        assert ('MACS 331', False) in group.courses
        assert ('MACS 335', False) in group.courses
        assert ('MACS 345', False) in group.courses
        assert ('MACS 346', False) in group.courses
        assert ('MACS 351', False) in group.courses
        assert ('MACS 352', False) in group.courses
        assert ('MACS 356', False) in group.courses
        assert ('MACS 361', False) in group.courses
        assert ('MACS 364', False) in group.courses
        assert ('MACS 365', False) in group.courses
        assert ('MACS 371', False) in group.courses
        assert ('MACS 373', False) in group.courses
        assert ('MACS 375', False) in group.courses
        assert ('MACS 377', False) in group.courses
        assert ('MACS 381', False) in group.courses
        assert ('MACS 382', False) in group.courses
        assert ('MACS 383', False) in group.courses
        assert ('MACS 389', False) in group.courses
        assert ('MACS 391', False) in group.courses
        assert ('MACS 395', False) in group.courses
        assert ('MACS 408', False) in group.courses
        assert ('MACS 410', False) in group.courses
        assert ('MACS 419', False) in group.courses
        assert ('MACS 423', False) in group.courses
        assert ('MACS 425', False) in group.courses
        assert ('MACS 389', False) in group.courses
        assert ('MACS 391', False) in group.courses
        assert ('MACS 395', False) in group.courses
        assert ('MACS 408', False) in group.courses
        assert ('MACS 410', False) in group.courses
        assert ('MACS 419', False) in group.courses
        assert ('MACS 423', False) in group.courses
        assert ('MACS 425', False) in group.courses
        assert ('MACS 432', False) in group.courses
        assert ('MACS 461', False) in group.courses
        assert ('MACS 464', False) in group.courses
        assert ('MACS 466', False) in group.courses
        assert ('MACS 470', False) in group.courses
        assert ('MACS 490', False) in group.courses
        assert ('MACS 492', False) in group.courses
        assert ('MACS 493', False) in group.courses
        assert ('MACS 494', False) in group.courses
        assert ('MACS 495', False) in group.courses
        assert ('MACS 496', False) in group.courses
        assert ('MACS 499', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestCinemaStudies.minor.required_courses

        # test length of the list
        assert len(courses) == 4

        # test for (course, if replacement course is available)
        assert ('MACS 203', False) in courses
        assert ('MACS 261', False) in courses
        assert ('MACS 262', False) in courses
        assert ('MACS 361', False) in courses
        

    def test_repl_courses(self):
        courses = TestCinemaStudies.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestCinemaStudies.minor.name
        credit = TestCinemaStudies.minor.total_credits

        assert name == 'Cinema Studies'.upper()
        assert credit == 18

class TestComputationalScienceAndEngineering:
    minor = minors[9]

    def test_required_groups(self):
        group_list = TestComputationalScienceAndEngineering.minor.required_groups

        assert len(group_list) == 4

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 5

        assert ('CS 101', False) in group.courses
        assert ('ECE 220', False) in group.courses
        assert ('CS 125', False) in group.courses
        assert ('LING 402', False) in group.courses
        assert ('CS 225', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 17

        assert ('MATH 441', False) in group.courses
        assert ('MATH 442', False) in group.courses
        assert ('MATH 489', False) in group.courses
        assert ('MATH 415', False) in group.courses
        assert ('ECE 493', False) in group.courses
        assert ('STAT 408', False) in group.courses
        assert ('STAT 409', False) in group.courses
        assert ('STAT 410', False) in group.courses
        assert ('STAT 420', False) in group.courses
        assert ('STAT 430', False) in group.courses
        assert ('STAT 461', False) in group.courses
        assert ('MATH 482', False) in group.courses
        assert ('MATH 484', False) in group.courses
        assert ('MATH 446', False) in group.courses
        assert ('MATH 448', False) in group.courses
        assert ('MATH 444', False) in group.courses
        assert ('MATH 447', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test third group
        group = group_list[2]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 8

        assert ('CS 450', True) in group.courses
        assert ('TAM 470', True) in group.courses
        assert ('ECE 448', True) in group.courses
        assert ('CS 411', False) in group.courses
        assert ('STAT 440', False) in group.courses
        assert ('LING 402', False) in group.courses
        assert ('CS 466', False) in group.courses
        assert ('GEOG 489', False) in group.courses
        
        assert len(group.repl_courses) == 3

        assert ('CS 450', 'CSE 401') in group.repl_courses
        assert ('TAM 470', 'CSE 450') in group.repl_courses
        assert ('ECE 448', 'CS 440') in group.repl_courses

        assert len(group.unallowed_courses) == 0

        # test fourth group
        group = group_list[3]

        assert group.goal_type == 'H'
        assert group.goal_num == 9

        assert len(group.courses) == 57

        
        assert ('CHEM 576', False) in group.courses
        assert ('CS 466', False) in group.courses
        assert ('CSE 564', True) in group.courses
        assert ('CSE 565', True) in group.courses
        assert ('CSE 566', True) in group.courses
        assert ('CHEM 550', False) in group.courses
        assert ('CSE 402', True) in group.courses
        assert ('CSE 422', True) in group.courses
        assert ('CSE 423', True) in group.courses
        assert ('CSE 426', True) in group.courses
        assert ('CSE 427', True) in group.courses
        assert ('CSE 429', True) in group.courses
        assert ('CSE 521', True) in group.courses
        assert ('CSE 522', True) in group.courses
        assert ('CSE 527', True) in group.courses
        assert ('CSE 530', True) in group.courses
        assert ('CSE 532', True) in group.courses
        assert ('CSE 450', True) in group.courses
        assert ('CSE 461', True) in group.courses
        assert ('CSE 560', True) in group.courses
        assert ('CSE 561', True) in group.courses
        assert ('CSE 566', True) in group.courses
        assert ('CSE 412', True) in group.courses
        assert ('CSE 401', True) in group.courses
        assert ('CSE 414', True) in group.courses
        assert ('CSE 441', True) in group.courses
        assert ('CSE 510', True) in group.courses
        assert ('CSE 511', True) in group.courses
        assert ('CSE 512', False) in group.courses
        assert ('CS 554', False) in group.courses
        assert ('CSE 513', True) in group.courses
        assert ('CSE 515', True) in group.courses
        assert ('CSE 517', True) in group.courses
        assert ('CSE 553', True) in group.courses
        assert ('CEE 528', False) in group.courses
        assert ('ASTR 510', False) in group.courses
        assert ('CSE 485', True) in group.courses
        assert ('CSE 441', True) in group.courses
        assert ('CSE 543', True) in group.courses
        assert ('ECE 513', False) in group.courses
        assert ('ECE 558', False) in group.courses
        assert ('CSE 450', True) in group.courses
        assert ('CSE 451', True) in group.courses
        assert ('CSE 517', True) in group.courses
        assert ('CSE 551', True) in group.courses
        assert ('CSE 552', True) in group.courses
        assert ('ME 570', False) in group.courses
        assert ('TAM 598', False) in group.courses
        assert ('CSE 428', True) in group.courses
        assert ('CSE 440', True) in group.courses
        assert ('CSE 448', True) in group.courses
        assert ('CSE 525', True) in group.courses
        assert ('CSE 531', True) in group.courses
        assert ('CSE 542', True) in group.courses
        assert ('STAT 430', False) in group.courses
        assert ('CS 412', False) in group.courses
        assert ('CS 410', False) in group.courses
        
        
        assert len(group.repl_courses) == 43


        assert ('CSE 564', 'CEE 534') in group.repl_courses
        assert ('CSE 565', 'CEE 557') in group.repl_courses
        assert ('CSE 566', 'ATMS 502', 'CS 505') in group.repl_courses
        assert ('CSE 402', 'CS 420', 'ECE 492') in group.repl_courses
        assert ('CSE 422', 'CS 433') in group.repl_courses
        assert ('CSE 423', 'CS 423') in group.repl_courses
        assert ('CSE 426', 'CS 427') in group.repl_courses
        assert ('CSE 427', 'CS 418') in group.repl_courses
        assert ('CSE 429', 'CS 428') in group.repl_courses
        assert ('CSE 521', 'ECE 511') in group.repl_courses
        assert ('CSE 522', 'CS 533') in group.repl_courses
        assert ('CSE 527', 'CS 519') in group.repl_courses
        assert ('CSE 530', 'ECE 540') in group.repl_courses
        assert ('CSE 532', 'ECE 552') in group.repl_courses
        assert ('CSE 450', 'TAM 470') in group.repl_courses
        assert ('CSE 461', 'AE 410') in group.repl_courses
        assert ('CSE 560', 'TAM 570') in group.repl_courses
        assert ('CSE 561', 'ME 554') in group.repl_courses
        assert ('CSE 566', 'ATMS 502') in group.repl_courses
        assert ('CSE 412', 'ME 412') in group.repl_courses
        assert ('CSE 401', 'CS 450', 'ECE 491', 'MATH 450') in group.repl_courses
        assert ('CSE 414', 'CS 473', 'MATH 473') in group.repl_courses
        assert ('CSE 441', 'ECE 490') in group.repl_courses
        assert ('CSE 510', 'CS 555') in group.repl_courses
        assert ('CSE 511', 'CS 556') in group.repl_courses
        assert ('CSE 513', 'CS 558') in group.repl_courses
        assert ('CSE 515', 'CS 573') in group.repl_courses
        assert ('CSE 517', 'TAM 574') in group.repl_courses
        assert ('CSE 553', 'CEE 577') in group.repl_courses
        assert ('CSE 485', 'MSE 485', 'PHYS 466') in group.repl_courses
        assert ('CSE 441', 'ECE 490') in group.repl_courses
        assert ('CSE 543', 'ECE 547') in group.repl_courses
        assert ('CSE 450', 'TAM 470') in group.repl_courses
        assert ('CSE 451', 'ME 471', 'AE 420') in group.repl_courses
        assert ('CSE 517', 'TAM 574') in group.repl_courses
        assert ('CSE 551', 'CEE 570') in group.repl_courses
        assert ('CSE 552', 'CEE 576') in group.repl_courses
        assert ('CSE 428', 'STAT 428') in group.repl_courses
        assert ('CSE 440', 'STAT 440') in group.repl_courses
        assert ('CSE 448', 'STAT 448') in group.repl_courses
        assert ('CSE 525', 'STAT 525') in group.repl_courses
        assert ('CSE 531', 'STAT 530') in group.repl_courses
        assert ('CSE 542', 'STAT 542') in group.repl_courses


        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestComputationalScienceAndEngineering.minor.required_courses

        # test length of the list
        assert len(courses) == 0

    def test_repl_courses(self):
        courses = TestComputationalScienceAndEngineering.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestComputationalScienceAndEngineering.minor.name
        credit = TestComputationalScienceAndEngineering.minor.total_credits

        assert name == 'Computational Science & Engineering'.upper()
        assert credit == 18

class TestComputerScience:
    minor = minors[10]

    def test_required_groups(self):
        group_list = TestComputerScience.minor.required_groups

        assert len(group_list) == 2

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 2

        assert len(group.courses) == 49

        assert ('CS 233', False) in group.courses
        assert ('CS 241', True) in group.courses
        assert ('CS 357', False) in group.courses
        assert ('CS 374', False) in group.courses
        assert ('CS 410', False) in group.courses
        assert ('CS 411', False) in group.courses
        assert ('CS 412', False) in group.courses
        assert ('CS 414', False) in group.courses
        assert ('CS 418', False) in group.courses
        assert ('CS 419', False) in group.courses
        assert ('CS 420', False) in group.courses
        assert ('CS 421', False) in group.courses
        assert ('CS 422', False) in group.courses
        assert ('CS 423', False) in group.courses
        assert ('CS 424', False) in group.courses
        assert ('CS 425', False) in group.courses
        assert ('CS 426', False) in group.courses
        assert ('CS 427', False) in group.courses
        assert ('CS 428', False) in group.courses
        assert ('CS 429', False) in group.courses
        assert ('CS 431', False) in group.courses
        assert ('CS 433', False) in group.courses
        assert ('CS 436', False) in group.courses
        assert ('CS 438', False) in group.courses
        assert ('CS 439', False) in group.courses
        assert ('CS 440', False) in group.courses
        assert ('CS 445', False) in group.courses
        assert ('CS 446', False) in group.courses
        assert ('CS 447', False) in group.courses
        assert ('CS 450', False) in group.courses
        assert ('CS 457', False) in group.courses
        assert ('CS 460', False) in group.courses
        assert ('CS 461', False) in group.courses
        assert ('CS 463', False) in group.courses
        assert ('CS 465', False) in group.courses
        assert ('CS 466', False) in group.courses
        assert ('CS 467', False) in group.courses
        assert ('CS 468', False) in group.courses
        assert ('CS 473', False) in group.courses
        assert ('CS 475', False) in group.courses
        assert ('CS 476', False) in group.courses
        assert ('CS 477', False) in group.courses
        assert ('CS 481', False) in group.courses
        assert ('CS 482', False) in group.courses
        assert ('CS 483', False) in group.courses
        assert ('CS 484', False) in group.courses
        assert ('CS 497', False) in group.courses
        assert ('CS 498', False) in group.courses
        assert ('CS 499', False) in group.courses
        
        assert len(group.repl_courses) == 1

        assert ('CS 241', 'ECE 391') in group.repl_courses

        assert len(group.unallowed_courses) == 5

        assert ['CS 413', 'CS 491', 'CS 492', 'CS 493', 'CS 494'] == group.unallowed_courses

        # test second group
        group = group_list[1]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 45

        assert ('CS 410', False) in group.courses
        assert ('CS 411', False) in group.courses
        assert ('CS 412', False) in group.courses
        assert ('CS 414', False) in group.courses
        assert ('CS 418', False) in group.courses
        assert ('CS 419', False) in group.courses
        assert ('CS 420', False) in group.courses
        assert ('CS 421', False) in group.courses
        assert ('CS 422', False) in group.courses
        assert ('CS 423', False) in group.courses
        assert ('CS 424', False) in group.courses
        assert ('CS 425', False) in group.courses
        assert ('CS 426', False) in group.courses
        assert ('CS 427', False) in group.courses
        assert ('CS 428', False) in group.courses
        assert ('CS 429', False) in group.courses
        assert ('CS 431', False) in group.courses
        assert ('CS 433', False) in group.courses
        assert ('CS 436', False) in group.courses
        assert ('CS 438', False) in group.courses
        assert ('CS 439', False) in group.courses
        assert ('CS 440', False) in group.courses
        assert ('CS 445', False) in group.courses
        assert ('CS 446', False) in group.courses
        assert ('CS 447', False) in group.courses
        assert ('CS 450', False) in group.courses
        assert ('CS 457', False) in group.courses
        assert ('CS 460', False) in group.courses
        assert ('CS 461', False) in group.courses
        assert ('CS 463', False) in group.courses
        assert ('CS 465', False) in group.courses
        assert ('CS 466', False) in group.courses
        assert ('CS 467', False) in group.courses
        assert ('CS 468', False) in group.courses
        assert ('CS 473', False) in group.courses
        assert ('CS 475', False) in group.courses
        assert ('CS 476', False) in group.courses
        assert ('CS 477', False) in group.courses
        assert ('CS 481', False) in group.courses
        assert ('CS 482', False) in group.courses
        assert ('CS 483', False) in group.courses
        assert ('CS 484', False) in group.courses
        assert ('CS 497', False) in group.courses
        assert ('CS 498', False) in group.courses
        assert ('CS 499', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 5

        assert ['CS 413', 'CS 491', 'CS 492', 'CS 493', 'CS 494'] == group.unallowed_courses

    def test_required_courses(self):
        courses = TestComputerScience.minor.required_courses

        # test length of the list
        assert len(courses) == 3

    def test_repl_courses(self):
        courses = TestComputerScience.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 2

        assert ('CS 125', 'ECE 220') in courses
        assert ('CS 173', 'MATH 213') in courses

    def test_minor(self):
        name = TestComputerScience.minor.name
        credit = TestComputerScience.minor.total_credits

        assert name == 'Computer Science'.upper()
        assert credit == 20

class TestCreativeWritingPoetryWriting:
    minor = minors[11]

    def test_required_groups(self):
        group_list = TestCreativeWritingPoetryWriting.minor.required_groups

        assert len(group_list) == 2

        # test first group
        group = group_list[0]

        assert group.goal_type == 'H'
        assert group.goal_num == 6

        assert len(group.courses) == 144

        assert ('ENGL 101', False) in group.courses
        assert ('ENGL 102', False) in group.courses
        assert ('ENGL 103', False) in group.courses
        assert ('ENGL 104', False) in group.courses
        assert ('ENGL 106', False) in group.courses
        assert ('ENGL 109', False) in group.courses
        assert ('ENGL 112', False) in group.courses
        assert ('ENGL 114', False) in group.courses
        assert ('ENGL 115', False) in group.courses
        assert ('ENGL 116', False) in group.courses
        assert ('ENGL 117', False) in group.courses
        assert ('ENGL 119', False) in group.courses
        assert ('ENGL 120', False) in group.courses
        assert ('ENGL 121', False) in group.courses
        assert ('ENGL 122', False) in group.courses
        assert ('ENGL 150', False) in group.courses
        assert ('ENGL 199', False) in group.courses
        assert ('ENGL 200', False) in group.courses
        assert ('ENGL 202', False) in group.courses
        assert ('ENGL 204', False) in group.courses
        assert ('ENGL 206', False) in group.courses
        assert ('ENGL 207', False) in group.courses
        assert ('ENGL 208', False) in group.courses
        assert ('ENGL 209', False) in group.courses
        assert ('ENGL 210', False) in group.courses
        assert ('ENGL 211', False) in group.courses
        assert ('ENGL 213', False) in group.courses
        assert ('ENGL 216', False) in group.courses
        assert ('ENGL 218', False) in group.courses
        assert ('ENGL 219', False) in group.courses
        assert ('ENGL 220', False) in group.courses
        assert ('ENGL 221', False) in group.courses
        assert ('ENGL 222', False) in group.courses
        assert ('ENGL 223', False) in group.courses
        assert ('ENGL 224', False) in group.courses
        assert ('ENGL 225', False) in group.courses
        assert ('ENGL 241', False) in group.courses
        assert ('ENGL 242', False) in group.courses
        assert ('ENGL 245', False) in group.courses
        assert ('ENGL 247', False) in group.courses
        assert ('ENGL 248', False) in group.courses
        assert ('ENGL 250', False) in group.courses
        assert ('ENGL 251', False) in group.courses
        assert ('ENGL 253', False) in group.courses
        assert ('ENGL 255', False) in group.courses
        assert ('ENGL 256', False) in group.courses
        assert ('ENGL 259', False) in group.courses
        assert ('ENGL 260', False) in group.courses
        assert ('ENGL 261', False) in group.courses
        assert ('ENGL 265', False) in group.courses
        assert ('ENGL 266', False) in group.courses
        assert ('ENGL 267', False) in group.courses
        assert ('ENGL 268', False) in group.courses
        assert ('ENGL 269', False) in group.courses
        assert ('ENGL 270', False) in group.courses
        assert ('ENGL 272', False) in group.courses
        assert ('ENGL 273', False) in group.courses
        assert ('ENGL 275', False) in group.courses
        assert ('ENGL 276', False) in group.courses
        assert ('ENGL 277', False) in group.courses
        assert ('ENGL 280', False) in group.courses
        assert ('ENGL 281', False) in group.courses
        assert ('ENGL 283', False) in group.courses
        assert ('ENGL 284', False) in group.courses
        assert ('ENGL 285', False) in group.courses
        assert ('ENGL 286', False) in group.courses
        assert ('ENGL 290', False) in group.courses
        assert ('ENGL 293', False) in group.courses
        assert ('ENGL 301', False) in group.courses
        assert ('ENGL 310', False) in group.courses
        assert ('ENGL 311', False) in group.courses
        assert ('ENGL 322', False) in group.courses
        assert ('ENGL 323', False) in group.courses
        assert ('ENGL 325', False) in group.courses
        assert ('ENGL 330', False) in group.courses
        assert ('ENGL 333', False) in group.courses
        assert ('ENGL 350', False) in group.courses
        assert ('ENGL 359', False) in group.courses
        assert ('ENGL 360', False) in group.courses
        assert ('ENGL 373', False) in group.courses
        assert ('ENGL 374', False) in group.courses
        assert ('ENGL 378', False) in group.courses
        assert ('ENGL 380', False) in group.courses
        assert ('ENGL 390', False) in group.courses
        assert ('ENGL 391', False) in group.courses
        assert ('ENGL 396', False) in group.courses
        assert ('ENGL 397', False) in group.courses
        assert ('ENGL 398', False) in group.courses
        assert ('ENGL 400', False) in group.courses
        assert ('ENGL 402', False) in group.courses
        assert ('ENGL 404', False) in group.courses
        assert ('ENGL 407', False) in group.courses
        assert ('ENGL 411', False) in group.courses
        assert ('ENGL 412', False) in group.courses
        assert ('ENGL 416', False) in group.courses
        assert ('ENGL 418', False) in group.courses
        assert ('ENGL 421', False) in group.courses
        assert ('ENGL 423', False) in group.courses
        assert ('ENGL 427', False) in group.courses
        assert ('ENGL 428', False) in group.courses
        assert ('ENGL 429', False) in group.courses
        assert ('ENGL 431', False) in group.courses
        assert ('ENGL 435', False) in group.courses
        assert ('ENGL 441', False) in group.courses
        assert ('ENGL 442', False) in group.courses
        assert ('ENGL 449', False) in group.courses
        assert ('ENGL 450', False) in group.courses
        assert ('ENGL 451', False) in group.courses
        assert ('ENGL 452', False) in group.courses
        assert ('ENGL 455', False) in group.courses
        assert ('ENGL 458', False) in group.courses
        assert ('ENGL 459', False) in group.courses
        assert ('ENGL 460', False) in group.courses
        assert ('ENGL 461', False) in group.courses
        assert ('ENGL 462', False) in group.courses
        assert ('ENGL 467', False) in group.courses
        assert ('ENGL 470', False) in group.courses
        assert ('ENGL 475', False) in group.courses
        assert ('ENGL 476', False) in group.courses
        assert ('ENGL 477', False) in group.courses
        assert ('ENGL 481', False) in group.courses
        assert ('ENGL 482', False) in group.courses
        assert ('ENGL 485', False) in group.courses
        assert ('ENGL 486', False) in group.courses
        assert ('ENGL 498', False) in group.courses
        assert ('CW 100', False) in group.courses
        assert ('CW 104', False) in group.courses
        assert ('CW 106', False) in group.courses
        assert ('CW 200', False) in group.courses
        assert ('CW 202', False) in group.courses
        assert ('CW 204', False) in group.courses
        assert ('CW 206', False) in group.courses
        assert ('CW 208', False) in group.courses
        assert ('CW 243', False) in group.courses
        assert ('CW 404', False) in group.courses
        assert ('CW 406', False) in group.courses
        assert ('CW 455', False) in group.courses
        assert ('CW 460', False) in group.courses
        assert ('CW 463', False) in group.courses
        assert ('CMN 310', False) in group.courses
        assert ('CMN 423', False) in group.courses
        assert ('JOUR 475', False) in group.courses
        assert ('THEA 211', False) in group.courses
        assert ('IS 410', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'H'
        assert group.goal_num == 3

        assert len(group.courses) == 66

        assert ('ENGL 301', False) in group.courses
        assert ('ENGL 310', False) in group.courses
        assert ('ENGL 311', False) in group.courses
        assert ('ENGL 322', False) in group.courses
        assert ('ENGL 323', False) in group.courses
        assert ('ENGL 325', False) in group.courses
        assert ('ENGL 330', False) in group.courses
        assert ('ENGL 333', False) in group.courses
        assert ('ENGL 350', False) in group.courses
        assert ('ENGL 359', False) in group.courses
        assert ('ENGL 360', False) in group.courses
        assert ('ENGL 373', False) in group.courses
        assert ('ENGL 374', False) in group.courses
        assert ('ENGL 378', False) in group.courses
        assert ('ENGL 380', False) in group.courses
        assert ('ENGL 390', False) in group.courses
        assert ('ENGL 391', False) in group.courses
        assert ('ENGL 396', False) in group.courses
        assert ('ENGL 397', False) in group.courses
        assert ('ENGL 398', False) in group.courses
        assert ('ENGL 400', False) in group.courses
        assert ('ENGL 402', False) in group.courses
        assert ('ENGL 404', False) in group.courses
        assert ('ENGL 407', False) in group.courses
        assert ('ENGL 411', False) in group.courses
        assert ('ENGL 412', False) in group.courses
        assert ('ENGL 416', False) in group.courses
        assert ('ENGL 418', False) in group.courses
        assert ('ENGL 421', False) in group.courses
        assert ('ENGL 423', False) in group.courses
        assert ('ENGL 427', False) in group.courses
        assert ('ENGL 428', False) in group.courses
        assert ('ENGL 429', False) in group.courses
        assert ('ENGL 431', False) in group.courses
        assert ('ENGL 435', False) in group.courses
        assert ('ENGL 441', False) in group.courses
        assert ('ENGL 442', False) in group.courses
        assert ('ENGL 449', False) in group.courses
        assert ('ENGL 450', False) in group.courses
        assert ('ENGL 451', False) in group.courses
        assert ('ENGL 452', False) in group.courses
        assert ('ENGL 455', False) in group.courses
        assert ('ENGL 458', False) in group.courses
        assert ('ENGL 459', False) in group.courses
        assert ('ENGL 460', False) in group.courses
        assert ('ENGL 461', False) in group.courses
        assert ('ENGL 462', False) in group.courses
        assert ('ENGL 467', False) in group.courses
        assert ('ENGL 470', False) in group.courses
        assert ('ENGL 475', False) in group.courses
        assert ('ENGL 476', False) in group.courses
        assert ('ENGL 477', False) in group.courses
        assert ('ENGL 481', False) in group.courses
        assert ('ENGL 482', False) in group.courses
        assert ('ENGL 485', False) in group.courses
        assert ('ENGL 486', False) in group.courses
        assert ('ENGL 498', False) in group.courses
        assert ('CW 404', False) in group.courses
        assert ('CW 406', False) in group.courses
        assert ('CW 455', False) in group.courses
        assert ('CW 460', False) in group.courses
        assert ('CW 463', False) in group.courses
        assert ('CMN 310', False) in group.courses
        assert ('CMN 423', False) in group.courses
        assert ('JOUR 475', False) in group.courses
        assert ('IS 410', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestCreativeWritingPoetryWriting.minor.required_courses

        # test length of the list
        assert len(courses) == 4

        assert [('CW 100', False), ('CW 106', False), ('CW 206', False), ('CW 406', False)] == courses

    def test_repl_courses(self):
        courses = TestCreativeWritingPoetryWriting.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestCreativeWritingPoetryWriting.minor.name
        credit = TestCreativeWritingPoetryWriting.minor.total_credits

        assert name == 'Creative Writing-Poetry Writing'.upper()
        assert credit == 18

class TestCreativeWritingNarrativeWriting:
    minor = minors[12]

    def test_required_groups(self):
        group_list = TestCreativeWritingNarrativeWriting.minor.required_groups

        assert len(group_list) == 2

        # test first group
        group = group_list[0]

        assert group.goal_type == 'H'
        assert group.goal_num == 6

        assert len(group.courses) == 144

        assert ('ENGL 101', False) in group.courses
        assert ('ENGL 102', False) in group.courses
        assert ('ENGL 103', False) in group.courses
        assert ('ENGL 104', False) in group.courses
        assert ('ENGL 106', False) in group.courses
        assert ('ENGL 109', False) in group.courses
        assert ('ENGL 112', False) in group.courses
        assert ('ENGL 114', False) in group.courses
        assert ('ENGL 115', False) in group.courses
        assert ('ENGL 116', False) in group.courses
        assert ('ENGL 117', False) in group.courses
        assert ('ENGL 119', False) in group.courses
        assert ('ENGL 120', False) in group.courses
        assert ('ENGL 121', False) in group.courses
        assert ('ENGL 122', False) in group.courses
        assert ('ENGL 150', False) in group.courses
        assert ('ENGL 199', False) in group.courses
        assert ('ENGL 200', False) in group.courses
        assert ('ENGL 202', False) in group.courses
        assert ('ENGL 204', False) in group.courses
        assert ('ENGL 206', False) in group.courses
        assert ('ENGL 207', False) in group.courses
        assert ('ENGL 208', False) in group.courses
        assert ('ENGL 209', False) in group.courses
        assert ('ENGL 210', False) in group.courses
        assert ('ENGL 211', False) in group.courses
        assert ('ENGL 213', False) in group.courses
        assert ('ENGL 216', False) in group.courses
        assert ('ENGL 218', False) in group.courses
        assert ('ENGL 219', False) in group.courses
        assert ('ENGL 220', False) in group.courses
        assert ('ENGL 221', False) in group.courses
        assert ('ENGL 222', False) in group.courses
        assert ('ENGL 223', False) in group.courses
        assert ('ENGL 224', False) in group.courses
        assert ('ENGL 225', False) in group.courses
        assert ('ENGL 241', False) in group.courses
        assert ('ENGL 242', False) in group.courses
        assert ('ENGL 245', False) in group.courses
        assert ('ENGL 247', False) in group.courses
        assert ('ENGL 248', False) in group.courses
        assert ('ENGL 250', False) in group.courses
        assert ('ENGL 251', False) in group.courses
        assert ('ENGL 253', False) in group.courses
        assert ('ENGL 255', False) in group.courses
        assert ('ENGL 256', False) in group.courses
        assert ('ENGL 259', False) in group.courses
        assert ('ENGL 260', False) in group.courses
        assert ('ENGL 261', False) in group.courses
        assert ('ENGL 265', False) in group.courses
        assert ('ENGL 266', False) in group.courses
        assert ('ENGL 267', False) in group.courses
        assert ('ENGL 268', False) in group.courses
        assert ('ENGL 269', False) in group.courses
        assert ('ENGL 270', False) in group.courses
        assert ('ENGL 272', False) in group.courses
        assert ('ENGL 273', False) in group.courses
        assert ('ENGL 275', False) in group.courses
        assert ('ENGL 276', False) in group.courses
        assert ('ENGL 277', False) in group.courses
        assert ('ENGL 280', False) in group.courses
        assert ('ENGL 281', False) in group.courses
        assert ('ENGL 283', False) in group.courses
        assert ('ENGL 284', False) in group.courses
        assert ('ENGL 285', False) in group.courses
        assert ('ENGL 286', False) in group.courses
        assert ('ENGL 290', False) in group.courses
        assert ('ENGL 293', False) in group.courses
        assert ('ENGL 301', False) in group.courses
        assert ('ENGL 310', False) in group.courses
        assert ('ENGL 311', False) in group.courses
        assert ('ENGL 322', False) in group.courses
        assert ('ENGL 323', False) in group.courses
        assert ('ENGL 325', False) in group.courses
        assert ('ENGL 330', False) in group.courses
        assert ('ENGL 333', False) in group.courses
        assert ('ENGL 350', False) in group.courses
        assert ('ENGL 359', False) in group.courses
        assert ('ENGL 360', False) in group.courses
        assert ('ENGL 373', False) in group.courses
        assert ('ENGL 374', False) in group.courses
        assert ('ENGL 378', False) in group.courses
        assert ('ENGL 380', False) in group.courses
        assert ('ENGL 390', False) in group.courses
        assert ('ENGL 391', False) in group.courses
        assert ('ENGL 396', False) in group.courses
        assert ('ENGL 397', False) in group.courses
        assert ('ENGL 398', False) in group.courses
        assert ('ENGL 400', False) in group.courses
        assert ('ENGL 402', False) in group.courses
        assert ('ENGL 404', False) in group.courses
        assert ('ENGL 407', False) in group.courses
        assert ('ENGL 411', False) in group.courses
        assert ('ENGL 412', False) in group.courses
        assert ('ENGL 416', False) in group.courses
        assert ('ENGL 418', False) in group.courses
        assert ('ENGL 421', False) in group.courses
        assert ('ENGL 423', False) in group.courses
        assert ('ENGL 427', False) in group.courses
        assert ('ENGL 428', False) in group.courses
        assert ('ENGL 429', False) in group.courses
        assert ('ENGL 431', False) in group.courses
        assert ('ENGL 435', False) in group.courses
        assert ('ENGL 441', False) in group.courses
        assert ('ENGL 442', False) in group.courses
        assert ('ENGL 449', False) in group.courses
        assert ('ENGL 450', False) in group.courses
        assert ('ENGL 451', False) in group.courses
        assert ('ENGL 452', False) in group.courses
        assert ('ENGL 455', False) in group.courses
        assert ('ENGL 458', False) in group.courses
        assert ('ENGL 459', False) in group.courses
        assert ('ENGL 460', False) in group.courses
        assert ('ENGL 461', False) in group.courses
        assert ('ENGL 462', False) in group.courses
        assert ('ENGL 467', False) in group.courses
        assert ('ENGL 470', False) in group.courses
        assert ('ENGL 475', False) in group.courses
        assert ('ENGL 476', False) in group.courses
        assert ('ENGL 477', False) in group.courses
        assert ('ENGL 481', False) in group.courses
        assert ('ENGL 482', False) in group.courses
        assert ('ENGL 485', False) in group.courses
        assert ('ENGL 486', False) in group.courses
        assert ('ENGL 498', False) in group.courses
        assert ('CW 100', False) in group.courses
        assert ('CW 104', False) in group.courses
        assert ('CW 106', False) in group.courses
        assert ('CW 200', False) in group.courses
        assert ('CW 202', False) in group.courses
        assert ('CW 204', False) in group.courses
        assert ('CW 206', False) in group.courses
        assert ('CW 208', False) in group.courses
        assert ('CW 243', False) in group.courses
        assert ('CW 404', False) in group.courses
        assert ('CW 406', False) in group.courses
        assert ('CW 455', False) in group.courses
        assert ('CW 460', False) in group.courses
        assert ('CW 463', False) in group.courses
        assert ('CMN 310', False) in group.courses
        assert ('CMN 423', False) in group.courses
        assert ('JOUR 475', False) in group.courses
        assert ('THEA 211', False) in group.courses
        assert ('IS 410', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'H'
        assert group.goal_num == 3

        assert len(group.courses) == 66

        assert ('ENGL 301', False) in group.courses
        assert ('ENGL 310', False) in group.courses
        assert ('ENGL 311', False) in group.courses
        assert ('ENGL 322', False) in group.courses
        assert ('ENGL 323', False) in group.courses
        assert ('ENGL 325', False) in group.courses
        assert ('ENGL 330', False) in group.courses
        assert ('ENGL 333', False) in group.courses
        assert ('ENGL 350', False) in group.courses
        assert ('ENGL 359', False) in group.courses
        assert ('ENGL 360', False) in group.courses
        assert ('ENGL 373', False) in group.courses
        assert ('ENGL 374', False) in group.courses
        assert ('ENGL 378', False) in group.courses
        assert ('ENGL 380', False) in group.courses
        assert ('ENGL 390', False) in group.courses
        assert ('ENGL 391', False) in group.courses
        assert ('ENGL 396', False) in group.courses
        assert ('ENGL 397', False) in group.courses
        assert ('ENGL 398', False) in group.courses
        assert ('ENGL 400', False) in group.courses
        assert ('ENGL 402', False) in group.courses
        assert ('ENGL 404', False) in group.courses
        assert ('ENGL 407', False) in group.courses
        assert ('ENGL 411', False) in group.courses
        assert ('ENGL 412', False) in group.courses
        assert ('ENGL 416', False) in group.courses
        assert ('ENGL 418', False) in group.courses
        assert ('ENGL 421', False) in group.courses
        assert ('ENGL 423', False) in group.courses
        assert ('ENGL 427', False) in group.courses
        assert ('ENGL 428', False) in group.courses
        assert ('ENGL 429', False) in group.courses
        assert ('ENGL 431', False) in group.courses
        assert ('ENGL 435', False) in group.courses
        assert ('ENGL 441', False) in group.courses
        assert ('ENGL 442', False) in group.courses
        assert ('ENGL 449', False) in group.courses
        assert ('ENGL 450', False) in group.courses
        assert ('ENGL 451', False) in group.courses
        assert ('ENGL 452', False) in group.courses
        assert ('ENGL 455', False) in group.courses
        assert ('ENGL 458', False) in group.courses
        assert ('ENGL 459', False) in group.courses
        assert ('ENGL 460', False) in group.courses
        assert ('ENGL 461', False) in group.courses
        assert ('ENGL 462', False) in group.courses
        assert ('ENGL 467', False) in group.courses
        assert ('ENGL 470', False) in group.courses
        assert ('ENGL 475', False) in group.courses
        assert ('ENGL 476', False) in group.courses
        assert ('ENGL 477', False) in group.courses
        assert ('ENGL 481', False) in group.courses
        assert ('ENGL 482', False) in group.courses
        assert ('ENGL 485', False) in group.courses
        assert ('ENGL 486', False) in group.courses
        assert ('ENGL 498', False) in group.courses
        assert ('CW 404', False) in group.courses
        assert ('CW 406', False) in group.courses
        assert ('CW 455', False) in group.courses
        assert ('CW 460', False) in group.courses
        assert ('CW 463', False) in group.courses
        assert ('CMN 310', False) in group.courses
        assert ('CMN 423', False) in group.courses
        assert ('JOUR 475', False) in group.courses
        assert ('IS 410', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestCreativeWritingNarrativeWriting.minor.required_courses

        # test length of the list
        assert len(courses) == 4

        assert [('CW 100', False), ('CW 104', False), ('CW 204', False), ('CW 404', False)] == courses

    def test_repl_courses(self):
        courses = TestCreativeWritingNarrativeWriting.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestCreativeWritingNarrativeWriting.minor.name
        credit = TestCreativeWritingNarrativeWriting.minor.total_credits

        assert name == 'Creative Writing-Narrative Writing'.upper()
        assert credit == 18

class TestCriminologyLawAndSociety:

    minor = minors[13]

    def test_required_groups(self):
        group_list = TestCriminologyLawAndSociety.minor.required_groups

        assert len(group_list) == 4

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 2

        assert ('SOC 100', False) in group.courses
        assert ('SOC 163', False) in group.courses
        
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 3

        assert ('SOC 378', False) in group.courses
        assert ('SOC 477', False) in group.courses
        assert ('SOC 479', False) in group.courses

        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test third group
        group = group_list[2]

        assert group.goal_type == 'H'
        assert group.goal_num == 9

        assert len(group.courses) == 13

        assert ('SOC 101', False) in group.courses
        assert ('SOC 225', False) in group.courses
        assert ('SOC 310', False) in group.courses
        assert ('SOC 373', False) in group.courses
        assert ('SOC 375', False) in group.courses
        assert ('SOC 378', False) in group.courses
        assert ('SOC 390', False) in group.courses
        assert ('SOC 396', False) in group.courses
        assert ('SOC 400', False) in group.courses
        assert ('SOC 477', False) in group.courses
        assert ('SOC 479', False) in group.courses
        assert ('SOC 490', False) in group.courses
        assert ('SOC 496', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test fourth group
        group = group_list[3]

        assert group.goal_type == 'H'
        assert group.goal_num == 3

        assert len(group.courses) == 11

        assert ('SOC 310', False) in group.courses
        assert ('SOC 373', False) in group.courses
        assert ('SOC 375', False) in group.courses
        assert ('SOC 378', False) in group.courses
        assert ('SOC 390', False) in group.courses
        assert ('SOC 396', False) in group.courses
        assert ('SOC 400', False) in group.courses
        assert ('SOC 477', False) in group.courses
        assert ('SOC 479', False) in group.courses
        assert ('SOC 490', False) in group.courses
        assert ('SOC 496', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestCriminologyLawAndSociety.minor.required_courses

        # test length of the list
        assert len(courses) == 1

        assert [('SOC 275', False)] == courses

    def test_repl_courses(self):
        courses = TestCriminologyLawAndSociety.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestCriminologyLawAndSociety.minor.name
        credit = TestCriminologyLawAndSociety.minor.total_credits

        assert name == 'Criminology, Law, & Society'.upper()
        assert credit == 18

class TestCropAndSoilManagement:
    minor = minors[14]

    def test_required_groups(self):
        group_list = TestCropAndSoilManagement.minor.required_groups

        assert len(group_list) == 2

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 4

        assert ('NRES 438', False) in group.courses
        assert ('NRES 471', False) in group.courses
        assert ('NRES 474', False) in group.courses
        assert ('NRES 475', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'H'
        assert group.goal_num == 3

        assert len(group.courses) == 75

        assert ('CPSC 102', False) in group.courses
        assert ('CPSC 103', False) in group.courses
        assert ('CPSC 112', False) in group.courses
        assert ('CPSC 113', False) in group.courses
        assert ('CPSC 116', False) in group.courses
        assert ('CPSC 117', False) in group.courses
        assert ('CPSC 131', False) in group.courses
        assert ('CPSC 180', False) in group.courses
        assert ('CPSC 190', False) in group.courses
        assert ('CPSC 199', False) in group.courses
        assert ('CPSC 213', False) in group.courses
        assert ('CPSC 215', False) in group.courses
        assert ('CPSC 226', False) in group.courses
        assert ('CPSC 241', False) in group.courses
        assert ('CPSC 261', False) in group.courses
        assert ('CPSC 265', False) in group.courses
        assert ('CPSC 266', False) in group.courses
        assert ('CPSC 270', False) in group.courses
        assert ('CPSC 293', False) in group.courses
        assert ('CPSC 294', False) in group.courses
        assert ('CPSC 295', False) in group.courses
        assert ('CPSC 336', False) in group.courses
        assert ('CPSC 352', False) in group.courses
        assert ('CPSC 382', False) in group.courses
        assert ('CPSC 396', False) in group.courses
        assert ('CPSC 407', False) in group.courses
        assert ('CPSC 408', False) in group.courses
        assert ('CPSC 412', False) in group.courses
        assert ('CPSC 413', False) in group.courses
        assert ('CPSC 414', False) in group.courses
        assert ('CPSC 415', False) in group.courses
        assert ('CPSC 416', False) in group.courses
        assert ('CPSC 417', False) in group.courses
        assert ('HORT 100', False) in group.courses
        assert ('HORT 105', False) in group.courses
        assert ('HORT 106', False) in group.courses
        assert ('HORT 107', False) in group.courses
        assert ('HORT 180', False) in group.courses
        assert ('HORT 199', False) in group.courses
        assert ('HORT 205', False) in group.courses
        assert ('HORT 223', False) in group.courses
        assert ('HORT 226', False) in group.courses
        assert ('HORT 240', False) in group.courses
        assert ('HORT 261', False) in group.courses
        assert ('HORT 293', False) in group.courses
        assert ('HORT 294', False) in group.courses
        assert ('HORT 295', False) in group.courses
        assert ('HORT 298', False) in group.courses
        assert ('HORT 301', False) in group.courses
        assert ('HORT 341', False) in group.courses
        assert ('HORT 344', False) in group.courses
        assert ('HORT 360', False) in group.courses
        assert ('HORT 361', False) in group.courses
        assert ('HORT 362', False) in group.courses
        assert ('HORT 363', False) in group.courses
        assert ('HORT 396', False) in group.courses
        assert ('HORT 421', False) in group.courses
        assert ('HORT 430', False) in group.courses
        assert ('HORT 434', False) in group.courses
        assert ('HORT 435', False) in group.courses
        assert ('HORT 442', False) in group.courses
        assert ('HORT 447', False) in group.courses
        assert ('HORT 453', False) in group.courses
        assert ('HORT 466', False) in group.courses
        assert ('HORT 475', False) in group.courses
        assert ('HORT 499', False) in group.courses
        assert ('PLPA 200', False) in group.courses
        assert ('PLPA 204', False) in group.courses
        assert ('PLPA 295', False) in group.courses
        assert ('PLPA 401', False) in group.courses
        assert ('PLPA 402', False) in group.courses
        assert ('PLPA 404', False) in group.courses
        assert ('PLPA 405', False) in group.courses
        assert ('PLPA 406', False) in group.courses
        assert ('PLPA 407', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 5

        assert ['CPSC 393', 'HORT 393', 'CPSC 395', 'HORT 395', 'PLPA 395'] == group.unallowed_courses

    def test_required_courses(self):
        courses = TestCropAndSoilManagement.minor.required_courses

        # test length of the list
        assert len(courses) == 4

        assert [('CPSC 112', False), ('CPSC 418', False), ('NRES 201', False), ('NRES 488', False)] == courses

    def test_repl_courses(self):
        courses = TestCropAndSoilManagement.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestCropAndSoilManagement.minor.name
        credit = TestCropAndSoilManagement.minor.total_credits

        assert name == 'Crop & Soil Management'.upper()
        assert credit == 20

class TestDisabilityStudies:

    minor = minors[15]

    def test_required_groups(self):
        group_list = TestDisabilityStudies.minor.required_groups

        assert len(group_list) == 2

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 4

        assert ('RST 260', False) in group.courses
        assert ('SHS 352', False) in group.courses
        assert ('CHLH 404', False) in group.courses
        assert ('KIN 360', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'H'
        assert group.goal_num == 9

        assert len(group.courses) == 14
        
        assert ('ARTD 420', False) in group.courses
        assert ('CMN 260', False) in group.courses
        assert ('CMN 462', False) in group.courses
        assert ('CMN 463', False) in group.courses
        assert ('CMN 467', False) in group.courses
        assert ('HDFS 208', False) in group.courses
        assert ('GWS 366', False) in group.courses
        assert ('REHB 435', False) in group.courses
        assert ('RST 230', False) in group.courses
        assert ('SHS 222', False) in group.courses
        assert ('SHS 271', False) in group.courses
        assert ('SHS 380', False) in group.courses
        assert ('SOCW 370', False) in group.courses
        assert ('SPED 322', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestDisabilityStudies.minor.required_courses

        # test length of the list
        assert len(courses) == 2

        assert [('REHB 330', False), ('REHB 402', False)] == courses

    def test_repl_courses(self):
        courses = TestDisabilityStudies.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestDisabilityStudies.minor.name
        credit = TestDisabilityStudies.minor.total_credits

        assert name == 'Disability Studies'.upper()
        assert credit == 19

class TestEastAsianLanguagesAndCultures:
    minor = minors[16]

    def test_required_groups(self):
        group_list = TestEastAsianLanguagesAndCultures.minor.required_groups

        assert len(group_list) == 3

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 3

        assert ('CHIN 204', False) in group.courses
        assert ('JAPN 204', False) in group.courses
        assert ('KOR 204', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'H'
        assert group.goal_num == 6

        assert len(group.courses) == 32
        
        assert ('CHIN 407', False) in group.courses
        assert ('CHIN 408', False) in group.courses
        assert ('CHIN 409', False) in group.courses
        assert ('CHIN 440', False) in group.courses
        assert ('CHIN 441', False) in group.courses
        assert ('CHIN 490', False) in group.courses
        assert ('CHIN 499', False) in group.courses
        assert ('JAPN 407', False) in group.courses
        assert ('JAPN 408', False) in group.courses
        assert ('JAPN 440', False) in group.courses
        assert ('JAPN 441', False) in group.courses
        assert ('JAPN 490', False) in group.courses
        assert ('JAPN 499', False) in group.courses
        assert ('KOR 440', False) in group.courses
        assert ('KOR 441', False) in group.courses
        assert ('EALC 402', False) in group.courses
        assert ('EALC 403', False) in group.courses
        assert ('EALC 411', False) in group.courses
        assert ('EALC 412', False) in group.courses
        assert ('EALC 415', False) in group.courses
        assert ('EALC 420', False) in group.courses
        assert ('EALC 421', False) in group.courses
        assert ('EALC 425', False) in group.courses
        assert ('EALC 426', False) in group.courses
        assert ('EALC 427', False) in group.courses
        assert ('EALC 430', False) in group.courses
        assert ('EALC 466', False) in group.courses
        assert ('EALC 476', False) in group.courses
        assert ('EALC 484', False) in group.courses
        assert ('EALC 488', False) in group.courses
        assert ('EALC 490', False) in group.courses
        assert ('EALC 495', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test third group
        group = group_list[2]

        assert group.goal_type == 'H'
        assert group.goal_num == 6

        assert len(group.courses) == 85
        
        assert ('CHIN 199', False) in group.courses
        assert ('CHIN 201', False) in group.courses
        assert ('CHIN 202', False) in group.courses
        assert ('CHIN 203', False) in group.courses
        assert ('CHIN 204', False) in group.courses
        assert ('CHIN 241', False) in group.courses
        assert ('CHIN 242', False) in group.courses
        assert ('CHIN 305', False) in group.courses
        assert ('CHIN 306', False) in group.courses
        assert ('CHIN 407', False) in group.courses
        assert ('CHIN 408', False) in group.courses
        assert ('CHIN 409', False) in group.courses
        assert ('CHIN 440', False) in group.courses
        assert ('CHIN 441', False) in group.courses
        assert ('CHIN 490', False) in group.courses
        assert ('CHIN 499', False) in group.courses
        assert ('JAPN 199', False) in group.courses
        assert ('JAPN 201', False) in group.courses
        assert ('JAPN 202', False) in group.courses
        assert ('JAPN 203', False) in group.courses
        assert ('JAPN 204', False) in group.courses
        assert ('JAPN 305', False) in group.courses
        assert ('JAPN 306', False) in group.courses
        assert ('JAPN 407', False) in group.courses
        assert ('JAPN 408', False) in group.courses
        assert ('JAPN 440', False) in group.courses
        assert ('JAPN 441', False) in group.courses
        assert ('JAPN 490', False) in group.courses
        assert ('JAPN 499', False) in group.courses
        assert ('KOR 201', False) in group.courses
        assert ('KOR 202', False) in group.courses
        assert ('KOR 203', False) in group.courses
        assert ('KOR 204', False) in group.courses
        assert ('KOR 221', False) in group.courses
        assert ('KOR 222', False) in group.courses
        assert ('KOR 241', False) in group.courses
        assert ('KOR 242', False) in group.courses
        assert ('KOR 305', False) in group.courses
        assert ('KOR 306', False) in group.courses
        assert ('KOR 440', False) in group.courses
        assert ('KOR 441', False) in group.courses
        assert ('EALC 114', False) in group.courses
        assert ('EALC 120', False) in group.courses
        assert ('EALC 122', False) in group.courses
        assert ('EALC 130', False) in group.courses
        assert ('EALC 132', False) in group.courses
        assert ('EALC 199', False) in group.courses
        assert ('EALC 220', False) in group.courses
        assert ('EALC 221', False) in group.courses
        assert ('EALC 222', False) in group.courses
        assert ('EALC 226', False) in group.courses
        assert ('EALC 227', False) in group.courses
        assert ('EALC 240', False) in group.courses
        assert ('EALC 250', False) in group.courses
        assert ('EALC 275', False) in group.courses
        assert ('EALC 276', False) in group.courses
        assert ('EALC 285', False) in group.courses
        assert ('EALC 287', False) in group.courses
        assert ('EALC 288', False) in group.courses
        assert ('EALC 305', False) in group.courses
        assert ('EALC 306', False) in group.courses
        assert ('EALC 307', False) in group.courses
        assert ('EALC 308', False) in group.courses
        assert ('EALC 343', False) in group.courses
        assert ('EALC 365', False) in group.courses
        assert ('EALC 367', False) in group.courses
        assert ('EALC 390', False) in group.courses
        assert ('EALC 398', False) in group.courses
        assert ('EALC 402', False) in group.courses
        assert ('EALC 403', False) in group.courses
        assert ('EALC 411', False) in group.courses
        assert ('EALC 412', False) in group.courses
        assert ('EALC 415', False) in group.courses
        assert ('EALC 420', False) in group.courses
        assert ('EALC 421', False) in group.courses
        assert ('EALC 425', False) in group.courses
        assert ('EALC 426', False) in group.courses
        assert ('EALC 427', False) in group.courses
        assert ('EALC 430', False) in group.courses
        assert ('EALC 466', False) in group.courses
        assert ('EALC 476', False) in group.courses
        assert ('EALC 484', False) in group.courses
        assert ('EALC 488', False) in group.courses
        assert ('EALC 490', False) in group.courses
        assert ('EALC 495', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestEastAsianLanguagesAndCultures.minor.required_courses

        # test length of the list
        assert len(courses) == 1

        assert [('EALC 120', False)] == courses

    def test_repl_courses(self):
        courses = TestEastAsianLanguagesAndCultures.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestEastAsianLanguagesAndCultures.minor.name
        credit = TestEastAsianLanguagesAndCultures.minor.total_credits

        assert name == 'East Asian Languages & Cultures'.upper()
        assert credit == 20

class TestEcologyAndConservationBiology:
    minor = minors[17]

    def test_required_groups(self):
        group_list = TestEcologyAndConservationBiology.minor.required_groups

        assert len(group_list) == 1

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 2

        assert len(group.courses) == 9

        assert ('IB 348', False) in group.courses
        assert ('IB 362', False) in group.courses
        assert ('IB 431', False) in group.courses
        assert ('IB 440', False) in group.courses
        assert ('IB 443', False) in group.courses
        assert ('IB 444', False) in group.courses
        assert ('IB 451', False) in group.courses
        assert ('IB 452', False) in group.courses
        assert ('IB 453', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestEcologyAndConservationBiology.minor.required_courses

        # test length of the list
        assert len(courses) == 3

        assert [('IB 150', False), ('IB 203', False), ('IB 204', False)] == courses

    def test_repl_courses(self):
        courses = TestEcologyAndConservationBiology.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestEcologyAndConservationBiology.minor.name
        credit = TestEcologyAndConservationBiology.minor.total_credits

        assert name == 'Ecology & Conservation Biology'.upper()
        assert credit == 17

class TestEconomicsMacroeconomicsTrack:
    minor = minors[18]

    def test_required_groups(self):
        group_list = TestEconomicsMacroeconomicsTrack.minor.required_groups

        assert len(group_list) == 1

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 4

        assert ('ECON 420', False) in group.courses
        assert ('ECON 452', False) in group.courses
        assert ('ECON 462', False) in group.courses
        assert ('ECON 490', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestEconomicsMacroeconomicsTrack.minor.required_courses

        # test length of the list
        assert len(courses) == 6

        assert [('ECON 102', False), ('ECON 202', False), ('ECON 203', False), ('ECON 302', False), ('ECON 103', False), ('ECON 303', False)] == courses

    def test_repl_courses(self):
        courses = TestEconomicsMacroeconomicsTrack.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestEconomicsMacroeconomicsTrack.minor.name
        credit = TestEconomicsMacroeconomicsTrack.minor.total_credits

        assert name == 'Economics-Macroeconomics Track'.upper()
        assert credit == 18

class TestEconomicsMicroeconomicsTrack:
    minor = minors[19]

    def test_required_groups(self):
        group_list = TestEconomicsMicroeconomicsTrack.minor.required_groups

        assert len(group_list) == 1

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 2

        assert len(group.courses) == 12

        assert ('ECON 411', False) in group.courses
        assert ('ECON 414', False) in group.courses
        assert ('ECON 440', False) in group.courses
        assert ('ECON 450', False) in group.courses
        assert ('ECON 451', False) in group.courses
        assert ('ECON 452', False) in group.courses
        assert ('ECON 480', False) in group.courses
        assert ('ECON 481', False) in group.courses
        assert ('ECON 482', False) in group.courses
        assert ('ECON 483', False) in group.courses
        assert ('ECON 484', False) in group.courses
        assert ('ECON 490', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestEconomicsMicroeconomicsTrack.minor.required_courses

        # test length of the list
        assert len(courses) == 4

        assert [('ECON 102', False), ('ECON 202', False), ('ECON 203', False), ('ECON 302', False)] == courses

    def test_repl_courses(self):
        courses = TestEconomicsMicroeconomicsTrack.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestEconomicsMicroeconomicsTrack.minor.name
        credit = TestEconomicsMicroeconomicsTrack.minor.total_credits

        assert name == 'Economics-Microeconomics Track'.upper()
        assert credit == 18

class TestEconomicsEconometricsTrack:
    minor = minors[20]

    def test_required_groups(self):
        group_list = TestEconomicsEconometricsTrack.minor.required_groups

        assert len(group_list) == 1

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 2

        assert len(group.courses) == 2

        assert ('ECON 465', False) in group.courses
        assert ('ECON 490', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestEconomicsEconometricsTrack.minor.required_courses

        # test length of the list
        assert len(courses) == 5

        assert [('ECON 102', False), ('ECON 202', False), ('ECON 203', False), ('ECON 302', False), ('ECON 471', False)] == courses

    def test_repl_courses(self):
        courses = TestEconomicsEconometricsTrack.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestEconomicsEconometricsTrack.minor.name
        credit = TestEconomicsEconometricsTrack.minor.total_credits

        assert name == 'Economics-Econometrics Track'.upper()
        assert credit == 18
# contains the AND CASE
class TestElectrialAndComputerEngineeringEEOption:
    minor = minors[21]

    def test_required_groups(self):
        group_list = TestElectrialAndComputerEngineeringEEOption.minor.required_groups

        assert len(group_list) == 5

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 2

        assert ('ECE 110', False) in group.courses
        assert ('ECE 205', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 2
        
        assert ('CS 101', False) in group.courses
        assert ('CS 125', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test third group
        group = group_list[2]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 7
        
        assert ('ECE 313', True) in group.courses
        assert ('IE 300', False) in group.courses
        assert ('BIOE 310', False) in group.courses
        assert ('MATH 461', False) in group.courses
        assert ('MATH 463', True) in group.courses
        assert ('CEE 202', False) in group.courses
        assert ('CS 361', True) in group.courses

        assert len(group.repl_courses) == 3

        assert [('ECE 313', 'MATH 362'), ('MATH 463', 'STAT 400'), ('CS 361', 'STAT 361')]

        assert len(group.unallowed_courses) == 0

        # test fourth group
        group = group_list[3]

        assert group.goal_type == 'C'
        assert group.goal_num == 2

        assert len(group.courses) == 5
        
        assert ('ECE 310', False) in group.courses
        assert ('ECE 329', False) in group.courses
        assert ('ECE 330', False) in group.courses
        assert ('ECE 340', False) in group.courses
        assert ('ECE 342 AND ECE 343', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test fifth group
        group = group_list[4]

        assert group.goal_type == 'H'
        assert group.goal_num == 18

        assert len(group.courses) == 111
        
        assert ('ECE 101', False) in group.courses
        assert ('ECE 110', False) in group.courses
        assert ('ECE 120', False) in group.courses
        assert ('ECE 198', False) in group.courses
        assert ('ECE 199', False) in group.courses
        assert ('ECE 200', False) in group.courses
        assert ('ECE 205', False) in group.courses
        assert ('ECE 206', False) in group.courses
        assert ('ECE 210', False) in group.courses
        assert ('ECE 211', False) in group.courses
        assert ('ECE 220', False) in group.courses
        assert ('ECE 297', False) in group.courses
        assert ('ECE 298', False) in group.courses
        assert ('ECE 304', False) in group.courses
        assert ('ECE 307', False) in group.courses
        assert ('ECE 310', False) in group.courses
        assert ('ECE 311', False) in group.courses
        assert ('ECE 313', False) in group.courses
        assert ('ECE 314', False) in group.courses
        assert ('ECE 316', False) in group.courses
        assert ('ECE 317', False) in group.courses
        assert ('ECE 329', False) in group.courses
        assert ('ECE 330', False) in group.courses
        assert ('ECE 333', False) in group.courses
        assert ('ECE 340', False) in group.courses
        assert ('ECE 342', False) in group.courses
        assert ('ECE 343', False) in group.courses
        assert ('ECE 345', False) in group.courses
        assert ('ECE 350', False) in group.courses
        assert ('ECE 365', False) in group.courses
        assert ('ECE 374', False) in group.courses
        assert ('ECE 380', False) in group.courses
        assert ('ECE 385', False) in group.courses
        assert ('ECE 391', False) in group.courses
        assert ('ECE 395', False) in group.courses
        assert ('ECE 396', False) in group.courses
        assert ('ECE 397', False) in group.courses
        assert ('ECE 398', False) in group.courses
        assert ('ECE 399', False) in group.courses
        assert ('ECE 401', False) in group.courses
        assert ('ECE 402', False) in group.courses
        assert ('ECE 403', False) in group.courses
        assert ('ECE 408', False) in group.courses
        assert ('ECE 411', False) in group.courses
        assert ('ECE 412', False) in group.courses
        assert ('ECE 414', False) in group.courses
        assert ('ECE 415', False) in group.courses
        assert ('ECE 416', False) in group.courses
        assert ('ECE 417', False) in group.courses
        assert ('ECE 418', False) in group.courses
        assert ('ECE 419', False) in group.courses
        assert ('ECE 420', False) in group.courses
        assert ('ECE 422', False) in group.courses
        assert ('ECE 424', False) in group.courses
        assert ('ECE 425', False) in group.courses
        assert ('ECE 428', False) in group.courses
        assert ('ECE 431', False) in group.courses
        assert ('ECE 432', False) in group.courses
        assert ('ECE 435', False) in group.courses
        assert ('ECE 437', False) in group.courses
        assert ('ECE 438', False) in group.courses
        assert ('ECE 439', False) in group.courses
        assert ('ECE 441', False) in group.courses
        assert ('ECE 443', False) in group.courses
        assert ('ECE 444', False) in group.courses
        assert ('ECE 445', False) in group.courses
        assert ('ECE 446', False) in group.courses
        assert ('ECE 447', False) in group.courses
        assert ('ECE 448', False) in group.courses
        assert ('ECE 451', False) in group.courses
        assert ('ECE 452', False) in group.courses
        assert ('ECE 453', False) in group.courses
        assert ('ECE 454', False) in group.courses
        assert ('ECE 455', False) in group.courses
        assert ('ECE 456', False) in group.courses
        assert ('ECE 457', False) in group.courses
        assert ('ECE 458', False) in group.courses
        assert ('ECE 459', False) in group.courses
        assert ('ECE 460', False) in group.courses
        assert ('ECE 461', False) in group.courses
        assert ('ECE 462', False) in group.courses
        assert ('ECE 463', False) in group.courses
        assert ('ECE 464', False) in group.courses
        assert ('ECE 465', False) in group.courses
        assert ('ECE 466', False) in group.courses
        assert ('ECE 467', False) in group.courses
        assert ('ECE 468', False) in group.courses
        assert ('ECE 469', False) in group.courses
        assert ('ECE 470', False) in group.courses
        assert ('ECE 472', False) in group.courses
        assert ('ECE 473', False) in group.courses
        assert ('ECE 476', False) in group.courses
        assert ('ECE 478', False) in group.courses
        assert ('ECE 480', False) in group.courses
        assert ('ECE 481', False) in group.courses
        assert ('ECE 482', False) in group.courses
        assert ('ECE 483', False) in group.courses
        assert ('ECE 484', False) in group.courses
        assert ('ECE 485', False) in group.courses
        assert ('ECE 486', False) in group.courses
        assert ('ECE 487', False) in group.courses
        assert ('ECE 488', False) in group.courses
        assert ('ECE 489', False) in group.courses
        assert ('ECE 490', False) in group.courses
        assert ('ECE 491', False) in group.courses
        assert ('ECE 492', False) in group.courses
        assert ('ECE 493', False) in group.courses
        assert ('ECE 495', False) in group.courses
        assert ('ECE 496', False) in group.courses
        assert ('ECE 498', False) in group.courses
        assert ('ECE 499', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestElectrialAndComputerEngineeringEEOption.minor.required_courses

        # test length of the list
        assert len(courses) == 1

        assert [('ECE 210', False)] == courses

    def test_repl_courses(self):
        courses = TestElectrialAndComputerEngineeringEEOption.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestElectrialAndComputerEngineeringEEOption.minor.name
        credit = TestElectrialAndComputerEngineeringEEOption.minor.total_credits

        assert name == 'Electrical & Computer Engineering, EE Option'.upper()
        assert credit == 19

class TestEceCeOption:
    minor = minors[22]

    def test_required_groups(self):
        group_list = TestEceCeOption.minor.required_groups

        assert len(group_list) == 5

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 2

        assert ('ECE 110', False) in group.courses
        assert ('ECE 205', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 2
        
        assert ('CS 101', False) in group.courses
        assert ('CS 125', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test third group
        group = group_list[2]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 7
        
        assert ('ECE 313', True) in group.courses
        assert ('IE 300', False) in group.courses
        assert ('BIOE 310', False) in group.courses
        assert ('MATH 461', False) in group.courses
        assert ('MATH 463', True) in group.courses
        assert ('CEE 202', False) in group.courses
        assert ('CS 361', True) in group.courses

        assert len(group.repl_courses) == 3

        assert [('ECE 313', 'MATH 362'), ('MATH 463', 'STAT 400'), ('CS 361', 'STAT 361')]

        assert len(group.unallowed_courses) == 0

        # test fourth group
        group = group_list[3]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 3
        
        assert ('ECE 385', False) in group.courses
        assert ('ECE 391', False) in group.courses
        assert ('ECE 411', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test fifth group
        group = group_list[4]

        assert group.goal_type == 'H'
        assert group.goal_num == 18

        assert len(group.courses) == 111
        
        assert ('ECE 101', False) in group.courses
        assert ('ECE 110', False) in group.courses
        assert ('ECE 120', False) in group.courses
        assert ('ECE 198', False) in group.courses
        assert ('ECE 199', False) in group.courses
        assert ('ECE 200', False) in group.courses
        assert ('ECE 205', False) in group.courses
        assert ('ECE 206', False) in group.courses
        assert ('ECE 210', False) in group.courses
        assert ('ECE 211', False) in group.courses
        assert ('ECE 220', False) in group.courses
        assert ('ECE 297', False) in group.courses
        assert ('ECE 298', False) in group.courses
        assert ('ECE 304', False) in group.courses
        assert ('ECE 307', False) in group.courses
        assert ('ECE 310', False) in group.courses
        assert ('ECE 311', False) in group.courses
        assert ('ECE 313', False) in group.courses
        assert ('ECE 314', False) in group.courses
        assert ('ECE 316', False) in group.courses
        assert ('ECE 317', False) in group.courses
        assert ('ECE 329', False) in group.courses
        assert ('ECE 330', False) in group.courses
        assert ('ECE 333', False) in group.courses
        assert ('ECE 340', False) in group.courses
        assert ('ECE 342', False) in group.courses
        assert ('ECE 343', False) in group.courses
        assert ('ECE 345', False) in group.courses
        assert ('ECE 350', False) in group.courses
        assert ('ECE 365', False) in group.courses
        assert ('ECE 374', False) in group.courses
        assert ('ECE 380', False) in group.courses
        assert ('ECE 385', False) in group.courses
        assert ('ECE 391', False) in group.courses
        assert ('ECE 395', False) in group.courses
        assert ('ECE 396', False) in group.courses
        assert ('ECE 397', False) in group.courses
        assert ('ECE 398', False) in group.courses
        assert ('ECE 399', False) in group.courses
        assert ('ECE 401', False) in group.courses
        assert ('ECE 402', False) in group.courses
        assert ('ECE 403', False) in group.courses
        assert ('ECE 408', False) in group.courses
        assert ('ECE 411', False) in group.courses
        assert ('ECE 412', False) in group.courses
        assert ('ECE 414', False) in group.courses
        assert ('ECE 415', False) in group.courses
        assert ('ECE 416', False) in group.courses
        assert ('ECE 417', False) in group.courses
        assert ('ECE 418', False) in group.courses
        assert ('ECE 419', False) in group.courses
        assert ('ECE 420', False) in group.courses
        assert ('ECE 422', False) in group.courses
        assert ('ECE 424', False) in group.courses
        assert ('ECE 425', False) in group.courses
        assert ('ECE 428', False) in group.courses
        assert ('ECE 431', False) in group.courses
        assert ('ECE 432', False) in group.courses
        assert ('ECE 435', False) in group.courses
        assert ('ECE 437', False) in group.courses
        assert ('ECE 438', False) in group.courses
        assert ('ECE 439', False) in group.courses
        assert ('ECE 441', False) in group.courses
        assert ('ECE 443', False) in group.courses
        assert ('ECE 444', False) in group.courses
        assert ('ECE 445', False) in group.courses
        assert ('ECE 446', False) in group.courses
        assert ('ECE 447', False) in group.courses
        assert ('ECE 448', False) in group.courses
        assert ('ECE 451', False) in group.courses
        assert ('ECE 452', False) in group.courses
        assert ('ECE 453', False) in group.courses
        assert ('ECE 454', False) in group.courses
        assert ('ECE 455', False) in group.courses
        assert ('ECE 456', False) in group.courses
        assert ('ECE 457', False) in group.courses
        assert ('ECE 458', False) in group.courses
        assert ('ECE 459', False) in group.courses
        assert ('ECE 460', False) in group.courses
        assert ('ECE 461', False) in group.courses
        assert ('ECE 462', False) in group.courses
        assert ('ECE 463', False) in group.courses
        assert ('ECE 464', False) in group.courses
        assert ('ECE 465', False) in group.courses
        assert ('ECE 466', False) in group.courses
        assert ('ECE 467', False) in group.courses
        assert ('ECE 468', False) in group.courses
        assert ('ECE 469', False) in group.courses
        assert ('ECE 470', False) in group.courses
        assert ('ECE 472', False) in group.courses
        assert ('ECE 473', False) in group.courses
        assert ('ECE 476', False) in group.courses
        assert ('ECE 478', False) in group.courses
        assert ('ECE 480', False) in group.courses
        assert ('ECE 481', False) in group.courses
        assert ('ECE 482', False) in group.courses
        assert ('ECE 483', False) in group.courses
        assert ('ECE 484', False) in group.courses
        assert ('ECE 485', False) in group.courses
        assert ('ECE 486', False) in group.courses
        assert ('ECE 487', False) in group.courses
        assert ('ECE 488', False) in group.courses
        assert ('ECE 489', False) in group.courses
        assert ('ECE 490', False) in group.courses
        assert ('ECE 491', False) in group.courses
        assert ('ECE 492', False) in group.courses
        assert ('ECE 493', False) in group.courses
        assert ('ECE 495', False) in group.courses
        assert ('ECE 496', False) in group.courses
        assert ('ECE 498', False) in group.courses
        assert ('ECE 499', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestEceCeOption.minor.required_courses

        # test length of the list
        assert len(courses) == 2

        assert [('ECE 120', False), ('ECE 220', False)] == courses

    def test_repl_courses(self):
        courses = TestEceCeOption.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestEceCeOption.minor.name
        credit = TestEceCeOption.minor.total_credits

        assert name == 'ECE, CE Option'.upper()
        assert credit == 19

class TestEnglishAsASecondLanguage:

    minor = minors[23]

    def test_required_groups(self):
        group_list = TestEnglishAsASecondLanguage.minor.required_groups

        assert len(group_list) == 2

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 3

        assert ('LING 100', False) in group.courses
        assert ('LING 400', False) in group.courses
        assert ('EIL 486', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'C'
        assert group.goal_num == 3

        assert len(group.courses) == 6
        
        assert ('EIL 422', False) in group.courses
        assert ('EIL 445', False) in group.courses
        assert ('EIL 456', False) in group.courses
        assert ('EIL 460', False) in group.courses
        assert ('EIL 487', False) in group.courses
        assert ('EIL 488', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestEnglishAsASecondLanguage.minor.required_courses

        # test length of the list
        assert len(courses) == 2

        assert [('LING 489', False), ('EIL 411', False)] == courses

    def test_repl_courses(self):
        courses = TestEnglishAsASecondLanguage.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestEnglishAsASecondLanguage.minor.name
        credit = TestEnglishAsASecondLanguage.minor.total_credits

        assert name == 'English as a Second Language'.upper()
        assert credit == 18

class TestEnglishAsASecondLanguageTeacherEducation:
    minor = minors[24]

    def test_required_groups(self):
        group_list = TestEnglishAsASecondLanguageTeacherEducation.minor.required_groups

        assert len(group_list) == 2

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 2

        assert ('EIL 214', False) in group.courses
        assert ('EIL 215', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 2
        
        assert ('EIL 456', False) in group.courses
        assert ('CI 446', False) in group.courses
          
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestEnglishAsASecondLanguageTeacherEducation.minor.required_courses

        # test length of the list
        assert len(courses) == 6

        assert [('EIL 422', False), ('EIL 411', False), ('EIL 460', False), ('EIL 448', False), ('LING 489', False), ('LING 100', False)] == courses

    def test_repl_courses(self):
        courses = TestEnglishAsASecondLanguageTeacherEducation.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestEnglishAsASecondLanguageTeacherEducation.minor.name
        credit = TestEnglishAsASecondLanguageTeacherEducation.minor.total_credits

        assert name == 'English As A Second Language, Teacher Education'.upper()
        assert credit == 23

class TestEnvironmentalEconomicsAndLaw:
    minor = minors[25]

    def test_required_groups(self):
        group_list = TestEnvironmentalEconomicsAndLaw.minor.required_groups

        assert len(group_list) == 3

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 2

        assert ('ACE 100', False) in group.courses
        assert ('ECON 102', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'C'
        assert group.goal_num == 2

        assert len(group.courses) == 5
        
        assert ('ACE 306', False) in group.courses
        assert ('ACE 403', False) in group.courses
        assert ('ACE 406', False) in group.courses
        assert ('ACE 456', False) in group.courses
        assert ('BADM 300', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test third group
        group = group_list[2]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 4
        
        assert ('ACE 411', False) in group.courses
        assert ('CEE 434', False) in group.courses
        assert ('ECON 414', True) in group.courses
        assert ('ECON 484', False) in group.courses

        assert len(group.repl_courses) == 1

        assert [('ECON 414', 'FIN 414')] == group.repl_courses

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestEnvironmentalEconomicsAndLaw.minor.required_courses

        # test length of the list
        assert len(courses) == 2

        assert [('ACE 210', True), ('ACE 310', True)] == courses

    def test_repl_courses(self):
        courses = TestEnvironmentalEconomicsAndLaw.minor.repl_courses

        assert len(courses) == 2

        assert [('ACE 210', 'ECON 210', 'ENVS 210', 'NRES 210', 'UP 210'), ('ACE 310', 'ENVS 310', 'NRES 310')]

    def test_minor(self):
        name = TestEnvironmentalEconomicsAndLaw.minor.name
        credit = TestEnvironmentalEconomicsAndLaw.minor.total_credits

        assert name == 'Environmental Economics & Law'.upper()
        assert credit == 18

class TestFoodAndAgribusinessManagement:
    minor = minors[26]

    def test_required_groups(self):
        group_list = TestFoodAndAgribusinessManagement.minor.required_groups

        assert len(group_list) == 2

        # test first group
        group = group_list[0]

        assert group.goal_type == 'H'
        assert group.goal_num == 3

        assert len(group.courses) == 5

        assert ('ACE 210', False) in group.courses
        assert ('ACE 251', False) in group.courses
        assert ('ACE 306', False) in group.courses
        assert ('ACE 335', False) in group.courses
        assert ('ACE 345', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'C'
        assert group.goal_num == 2

        assert len(group.courses) == 7
        
        assert ('ACE 427', False) in group.courses
        assert ('ACE 428', False) in group.courses
        assert ('ACE 430', True) in group.courses
        assert ('ACE 431', True) in group.courses
        assert ('ACE 435', False) in group.courses
        assert ('ACE 436', True) in group.courses
        assert ('ACE 444', False) in group.courses
        
        assert len(group.repl_courses) == 3

        assert [('ACE 430', 'FSHN 425'), ('ACE 431', 'BADM 438'), ('ACE 436', 'BADM 436')]

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestFoodAndAgribusinessManagement.minor.required_courses

        # test length of the list
        assert len(courses) == 3

        assert [('ACE 100', True), ('ACE 222', False), ('ACE 231', False)] == courses

    def test_repl_courses(self):
        courses = TestFoodAndAgribusinessManagement.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 1

        assert [('ACE 100', 'ECON 102')] == courses

    def test_minor(self):
        name = TestFoodAndAgribusinessManagement.minor.name
        credit = TestFoodAndAgribusinessManagement.minor.total_credits

        assert name == 'Food & Agribusiness Management'.upper()
        assert credit == 18

class TestFoodAndEnvironmentalSystems:
    minor = minors[27]

    def test_required_groups(self):
        group_list = TestFoodAndEnvironmentalSystems.minor.required_groups

        assert len(group_list) == 2

        # test first group
        group = group_list[0]

        assert group.goal_type == 'H'
        assert group.goal_num == 3

        assert len(group.courses) == 26

        assert ('ANSC 100', False) in group.courses
        assert ('ANSC 101', False) in group.courses
        assert ('ANSC 110', False) in group.courses
        assert ('ANSC 223', False) in group.courses
        assert ('ANSC 224', False) in group.courses
        assert ('ANSC 250', False) in group.courses
        assert ('ACE 100', False) in group.courses
        assert ('ACE 210', False) in group.courses
        assert ('ACE 222', False) in group.courses
        assert ('ACE 231', False) in group.courses
        assert ('ACE 232', False) in group.courses
        assert ('ACE 251', False) in group.courses
        assert ('CPSC 112', False) in group.courses
        assert ('CPSC 116', False) in group.courses
        assert ('CPSC 226', False) in group.courses
        assert ('FSHN 120', True) in group.courses
        assert ('FSHN 232', False) in group.courses
        assert ('FSHN 260', False) in group.courses
        assert ('HORT 105', False) in group.courses
        assert ('HORT 106', False) in group.courses
        assert ('NRES 109', False) in group.courses
        assert ('NRES 201', False) in group.courses
        assert ('NRES 219', False) in group.courses
        assert ('NRES 287', False) in group.courses
        assert ('PLPA 204', False) in group.courses
        assert ('TSM 100', False) in group.courses
        
        assert len(group.repl_courses) == 1

        assert [('FSHN 120', 'FSHN 220')] == group.repl_courses

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'H'
        assert group.goal_num == 6

        assert len(group.courses) == 57
        
        assert ('ACE 306', False) in group.courses
        assert ('ACE 310', False) in group.courses
        assert ('ACE 346', False) in group.courses
        assert ('ACE 403', False) in group.courses
        assert ('ACE 406', False) in group.courses
        assert ('ACE 411', False) in group.courses
        assert ('ACE 430', False) in group.courses
        assert ('ACE 431', False) in group.courses
        assert ('ACE 432', False) in group.courses
        assert ('ACE 435', False) in group.courses
        assert ('ACE 436', False) in group.courses
        assert ('ACE 451', False) in group.courses
        assert ('ACE 456', False) in group.courses
        assert ('ANSC 305', False) in group.courses
        assert ('ANSC 306', False) in group.courses
        assert ('ANSC 309', False) in group.courses
        assert ('ANSC 322', False) in group.courses
        assert ('ANSC 363', False) in group.courses
        assert ('ANSC 400', False) in group.courses
        assert ('ANSC 401', False) in group.courses
        assert ('ANSC 402', False) in group.courses
        assert ('ANSC 403', False) in group.courses
        assert ('ANSC 404', False) in group.courses
        assert ('ANSC 405', False) in group.courses
        assert ('ANSC 406', False) in group.courses
        assert ('ANSC 407', False) in group.courses
        assert ('ANSC 409', False) in group.courses
        assert ('ANSC 422', False) in group.courses
        assert ('ANSC 423', False) in group.courses
        assert ('ANSC 431', False) in group.courses
        assert ('ANSC 438', False) in group.courses
        assert ('ANSC 444', False) in group.courses
        assert ('ANSC 446', False) in group.courses
        assert ('ANSC 450', False) in group.courses
        assert ('ANSC 451', False) in group.courses
        assert ('ANSC 452', False) in group.courses
        assert ('ANSC 467', False) in group.courses
        assert ('CPSC 407', False) in group.courses
        assert ('CPSC 418', False) in group.courses
        assert ('CPSC 431', False) in group.courses
        assert ('FSHN 302', False) in group.courses
        assert ('FSHN 322', False) in group.courses
        assert ('FSHN 425', False) in group.courses
        assert ('FSHN 428', False) in group.courses
        assert ('NRES 325', False) in group.courses
        assert ('NRES 330', False) in group.courses
        assert ('NRES 348', False) in group.courses
        assert ('NRES 370', False) in group.courses
        assert ('NRES 409', False) in group.courses
        assert ('NRES 419', False) in group.courses
        assert ('NRES 420', False) in group.courses
        assert ('NRES 430', False) in group.courses
        assert ('NRES 431', False) in group.courses
        assert ('NRES 474', False) in group.courses
        assert ('NRES 488', False) in group.courses
        assert ('PLPA 407', False) in group.courses
        assert ('TSM 311', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestFoodAndEnvironmentalSystems.minor.required_courses

        # test length of the list
        assert len(courses) == 3

        assert [('ACES 102', False), ('FSHN 101', False), ('NRES 100', False)] == courses

    def test_repl_courses(self):
        courses = TestFoodAndEnvironmentalSystems.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestFoodAndEnvironmentalSystems.minor.name
        credit = TestFoodAndEnvironmentalSystems.minor.total_credits

        assert name == 'Food & Environmental Systems'.upper()
        assert credit == 18

class TestFoodScience:
    minor = minors[28]

    def test_required_groups(self):
        group_list = TestFoodScience.minor.required_groups

        assert len(group_list) == 2

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 2

        assert ('FSHN 465', False) in group.courses
        assert ('FSHN 461 AND FSHN 462', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 10
        
        assert ('FSHN 232', False) in group.courses
        assert ('FSHN 260', False) in group.courses
        assert ('FSHN 302', False) in group.courses
        assert ('FSHN 416', False) in group.courses
        assert ('FSHN 418', False) in group.courses
        assert ('FSHN 460', False) in group.courses
        assert ('FSHN 466', False) in group.courses
        assert ('ANSC 350', False) in group.courses
        assert ('MCB 450', False) in group.courses
        assert ('ABE 483', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestFoodScience.minor.required_courses

        # test length of the list
        assert len(courses) == 3

        assert [('FSHN 101', False), ('FSHN 414', False), ('FSHN 471', False)] == courses

    def test_repl_courses(self):
        courses = TestFoodScience.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestFoodScience.minor.name
        credit = TestFoodScience.minor.total_credits

        assert name == 'Food Science'.upper()
        assert credit == 18

class TestFrench:
    minor = minors[29]

    def test_required_groups(self):
        group_list = TestFrench.minor.required_groups

        assert len(group_list) == 3

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 3

        assert ('FR 335', False) in group.courses
        assert ('FR 336', False) in group.courses
        assert ('FR 337', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 2
        
        assert ('FR 205', False) in group.courses
        assert ('FR 213', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test third group
        group = group_list[2]

        assert group.goal_type == 'C'
        assert group.goal_num == 2

        assert len(group.courses) == 31
        
        assert ('FR 301', False) in group.courses
        assert ('FR 309', False) in group.courses
        assert ('FR 311', False) in group.courses
        assert ('FR 312', False) in group.courses
        assert ('FR 314', False) in group.courses
        assert ('FR 319', False) in group.courses
        assert ('FR 322', False) in group.courses
        assert ('FR 323', False) in group.courses
        assert ('FR 324', False) in group.courses
        assert ('FR 335', False) in group.courses
        assert ('FR 336', False) in group.courses
        assert ('FR 337', False) in group.courses
        assert ('FR 385', False) in group.courses
        assert ('FR 387', False) in group.courses
        assert ('FR 389', False) in group.courses
        assert ('FR 390', False) in group.courses
        assert ('FR 410', False) in group.courses
        assert ('FR 413', False) in group.courses
        assert ('FR 416', False) in group.courses
        assert ('FR 417', False) in group.courses
        assert ('FR 418', False) in group.courses
        assert ('FR 419', False) in group.courses
        assert ('FR 421', False) in group.courses
        assert ('FR 443', False) in group.courses
        assert ('FR 460', False) in group.courses
        assert ('FR 462', False) in group.courses
        assert ('FR 479', False) in group.courses
        assert ('FR 481', False) in group.courses
        assert ('FR 485', False) in group.courses
        assert ('FR 486', False) in group.courses
        assert ('FR 492', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestFrench.minor.required_courses

        # test length of the list
        assert len(courses) == 3

        assert [('FR 207', False), ('FR 211', False), ('FR 212', False)] == courses

    def test_repl_courses(self):
        courses = TestFrench.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestFrench.minor.name
        credit = TestFrench.minor.total_credits

        assert name == 'French'.upper()
        assert credit == 20

class TestGeographyAndGIS:
    minor = minors[30]

    def test_required_groups(self):
        group_list = TestGeographyAndGIS.minor.required_groups

        assert len(group_list) == 5

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 2

        assert len(group.courses) == 7

        assert ('GEOG 100', True) in group.courses
        assert ('GEOG 101', False) in group.courses
        assert ('GEOG 103', False) in group.courses
        assert ('GEOG 104', False) in group.courses
        assert ('GEOG 105', False) in group.courses
        assert ('GEOG 106', False) in group.courses
        assert ('GEOG 221', False) in group.courses
        
        assert len(group.repl_courses) == 1

        assert [('GEOG 100', 'ATMS 100')] == group.repl_courses

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 14
        
        assert ('GEOG 204', False) in group.courses
        assert ('GEOG 205', False) in group.courses
        assert ('GEOG 224', False) in group.courses
        assert ('GEOG 350', False) in group.courses
        assert ('GEOG 356', False) in group.courses
        assert ('GEOG 384', False) in group.courses
        assert ('GEOG 405', False) in group.courses
        assert ('GEOG 410', False) in group.courses
        assert ('GEOG 438', False) in group.courses
        assert ('GEOG 455', False) in group.courses
        assert ('GEOG 466', False) in group.courses
        assert ('GEOG 471', False) in group.courses
        assert ('GEOG 483', False) in group.courses
        assert ('GEOG 484', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test third group
        group = group_list[2]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 10
        
        assert ('GEOG 210', False) in group.courses
        assert ('GEOG 222', False) in group.courses
        assert ('ESE 320', False) in group.courses
        assert ('NRES 401', True) in group.courses
        assert ('GEOG 405', False) in group.courses
        assert ('GEOG 406', False) in group.courses
        assert ('GEOG 408', False) in group.courses
        assert ('GEOG 412', False) in group.courses
        assert ('GEOG 459', False) in group.courses
        assert ('GEOG 496', False) in group.courses

        assert len(group.repl_courses) == 1

        assert [('NRES 401', 'GEOG 401')] == group.repl_courses

        assert len(group.unallowed_courses) == 0

        # test fourth group
        group = group_list[3]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 14
        
        assert ('GEOG 371', False) in group.courses
        assert ('GEOG 379', False) in group.courses
        assert ('GEOG 380', False) in group.courses
        assert ('GEOG 412', False) in group.courses
        assert ('GEOG 440', False) in group.courses
        assert ('PATH 439', False) in group.courses
        assert ('GEOG 460', False) in group.courses
        assert ('GEOG 468', False) in group.courses
        assert ('GEOG 473', False) in group.courses
        assert ('GEOG 476', False) in group.courses
        assert ('GEOG 477', False) in group.courses
        assert ('GEOG 478', False) in group.courses
        assert ('GEOG 479', False) in group.courses
        assert ('GEOG 480', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test fifth group
        group = group_list[4]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 39
        
        assert ('GEOG 221', False) in group.courses
        assert ('GEOG 204', False) in group.courses
        assert ('GEOG 205', False) in group.courses
        assert ('GEOG 224', False) in group.courses
        assert ('GEOG 350', False) in group.courses
        assert ('GEOG 356', False) in group.courses
        assert ('GEOG 384', False) in group.courses
        assert ('GEOG 405', False) in group.courses
        assert ('GEOG 410', False) in group.courses
        assert ('GEOG 438', False) in group.courses
        assert ('GEOG 455', False) in group.courses
        assert ('GEOG 466', False) in group.courses
        assert ('GEOG 471', False) in group.courses
        assert ('GEOG 483', False) in group.courses
        assert ('GEOG 484', False) in group.courses
        assert ('GEOG 210', False) in group.courses
        assert ('GEOG 222', False) in group.courses
        assert ('ESE 320', False) in group.courses
        assert ('NRES 401', True) in group.courses
        assert ('GEOG 405', False) in group.courses
        assert ('GEOG 406', False) in group.courses
        assert ('GEOG 408', False) in group.courses
        assert ('GEOG 412', False) in group.courses
        assert ('GEOG 459', False) in group.courses
        assert ('GEOG 496', False) in group.courses
        assert ('GEOG 371', False) in group.courses
        assert ('GEOG 379', False) in group.courses
        assert ('GEOG 380', False) in group.courses
        assert ('GEOG 412', False) in group.courses
        assert ('GEOG 440', False) in group.courses
        assert ('PATH 439', False) in group.courses
        assert ('GEOG 460', False) in group.courses
        assert ('GEOG 468', False) in group.courses
        assert ('GEOG 473', False) in group.courses
        assert ('GEOG 476', False) in group.courses
        assert ('GEOG 477', False) in group.courses
        assert ('GEOG 478', False) in group.courses
        assert ('GEOG 479', False) in group.courses
        assert ('GEOG 480', False) in group.courses

        assert len(group.repl_courses) == 1

        assert [('NRES 401', 'GEOG 401')] == group.repl_courses

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestGeographyAndGIS.minor.required_courses

        # test length of the list
        assert len(courses) == 0

    def test_repl_courses(self):
        courses = TestGeographyAndGIS.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestGeographyAndGIS.minor.name
        credit = TestGeographyAndGIS.minor.total_credits

        assert name == 'Geography & GIS'.upper()
        assert credit == 18

class TestGeology:
    minor = minors[31]

    def test_required_groups(self):
        group_list = TestGeology.minor.required_groups

        assert len(group_list) == 1

        # test first group
        group = group_list[0]

        assert group.goal_type == 'H'
        assert group.goal_num == 10

        assert len(group.courses) == 26

        assert ('GEOL 333', False) in group.courses
        assert ('GEOL 380', False) in group.courses
        assert ('GEOL 401', False) in group.courses
        assert ('GEOL 406', False) in group.courses
        assert ('GEOL 411', False) in group.courses
        assert ('GEOL 415', False) in group.courses
        assert ('GEOL 417', False) in group.courses
        assert ('GEOL 432', False) in group.courses
        assert ('GEOL 436', False) in group.courses
        assert ('GEOL 440', False) in group.courses
        assert ('GEOL 450', False) in group.courses
        assert ('GEOL 451', False) in group.courses
        assert ('GEOL 452', False) in group.courses
        assert ('GEOL 454', False) in group.courses
        assert ('GEOL 460', False) in group.courses
        assert ('GEOL 470', False) in group.courses
        assert ('GEOL 481', False) in group.courses
        assert ('GEOL 483', False) in group.courses
        assert ('GEOL 484', False) in group.courses
        assert ('GEOL 485', False) in group.courses
        assert ('GEOL 486', False) in group.courses
        assert ('GEOL 490', False) in group.courses
        assert ('GEOL 491', False) in group.courses
        assert ('GEOL 492', False) in group.courses
        assert ('GEOL 493', False) in group.courses
        assert ('GEOL 497', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestGeology.minor.required_courses

        # test length of the list
        assert len(courses) == 2

        assert [('GEOL 107', False), ('GEOL 208', False)] == courses

    def test_repl_courses(self):
        courses = TestGeology.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestGeology.minor.name
        credit = TestGeology.minor.total_credits

        assert name == 'Geology'.upper()
        assert credit == 18

class TestGerman:
    minor = minors[32]

    def test_required_groups(self):
        group_list = TestGerman.minor.required_groups

        assert len(group_list) == 1

        # test first group
        group = group_list[0]

        assert group.goal_type == 'H'
        assert group.goal_num == 11

        assert len(group.courses) == 20

        assert ('GER 103', False) in group.courses
        assert ('GER 104', False) in group.courses
        assert ('GER 201', False) in group.courses
        assert ('GER 205', False) in group.courses
        assert ('GER 212', False) in group.courses
        assert ('GER 250', True) in group.courses
        assert ('GER 260', True) in group.courses
        assert ('GER 270', False) in group.courses
        assert ('GER 331', False) in group.courses
        assert ('GER 332', False) in group.courses
        assert ('GER 401', False) in group.courses
        assert ('PS 485', False) in group.courses
        assert ('GER 403', False) in group.courses
        assert ('GER 465', False) in group.courses
        assert ('GER 470', False) in group.courses
        assert ('GER 471', False) in group.courses
        assert ('GER 472', False) in group.courses
        assert ('GER 473', False) in group.courses
        assert ('GER 493', False) in group.courses
        assert ('GER 494', False) in group.courses
        
        assert len(group.repl_courses) == 2

        assert [('GER 250', 'GER 251'), ('GER 260', 'GER 261')] == group.repl_courses

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestGerman.minor.required_courses

        # test length of the list
        assert len(courses) == 2

        assert [('GER 211', False), ('GER 420', False)] == courses

    def test_repl_courses(self):
        courses = TestGerman.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestGerman.minor.name
        credit = TestGerman.minor.total_credits

        assert name == 'German'.upper()
        assert credit == 18

class TestGlobalLaborStudies:
    minor = minors[33]

    def test_required_groups(self):
        group_list = TestGlobalLaborStudies.minor.required_groups

        assert len(group_list) == 2

        # test first group
        group = group_list[0]

        assert group.goal_type == 'H'
        assert group.goal_num == 6

        assert len(group.courses) == 3

        assert ('LER 300', False) in group.courses
        assert ('LER 320', False) in group.courses
        assert ('LER 330', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'H'
        assert group.goal_num == 6

        assert len(group.courses) == 4
        
        assert ('LER 200', False) in group.courses
        assert ('LER 330', False) in group.courses
        assert ('LER 240', False) in group.courses
        assert ('LER 410', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestGlobalLaborStudies.minor.required_courses

        # test length of the list
        assert len(courses) == 2

        assert [('LER 100', False), ('LER 130', False)] == courses

    def test_repl_courses(self):
        courses = TestGlobalLaborStudies.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestGlobalLaborStudies.minor.name
        credit = TestGlobalLaborStudies.minor.total_credits

        assert name == 'Global Labor Studies'.upper()
        assert credit == 18
    
class TestHindiStudies:
    minor = minors[34]

    def test_required_groups(self):
        group_list = TestHindiStudies.minor.required_groups

        assert len(group_list) == 2

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 2

        assert len(group.courses) == 3

        assert ('LING 111', False) in group.courses
        assert ('LING 115', False) in group.courses
        assert ('HNDI 412', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 7
        
        assert ('SNSK 201', False) in group.courses
        assert ('SNSK 202', False) in group.courses
        assert ('ARAB 201', False) in group.courses
        assert ('ARAB 202', False) in group.courses
        assert ('PERS 201', False) in group.courses
        assert ('PERS 202', False) in group.courses
        assert ('HNDI 408', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestHindiStudies.minor.required_courses

        # test length of the list
        assert len(courses) == 3

        assert [('HNDI 404', False), ('HNDI 405', False), ('HNDI 406', False)] == courses

    def test_repl_courses(self):
        courses = TestHindiStudies.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestHindiStudies.minor.name
        credit = TestHindiStudies.minor.total_credits

        assert name == 'Hindi Studies'.upper()
        assert credit == 19

class TestHorticulture:
    minor = minors[35]

    def test_required_groups(self):
        group_list = TestHorticulture.minor.required_groups

        assert len(group_list) == 2

        # test first group
        group = group_list[0]

        assert group.goal_type == 'H'
        assert group.goal_num == 2

        assert len(group.courses) == 9

        assert ('LAW 201', False) in group.courses
        assert ('LAW 301', False) in group.courses
        assert ('LAW 302', False) in group.courses
        assert ('LAW 303', False) in group.courses
        assert ('LAW 304', False) in group.courses
        assert ('LAW 305', False) in group.courses
        assert ('EPS 310', True) in group.courses
        assert ('SOC 479', False) in group.courses
        assert ('PS 323', False) in group.courses
        
        assert len(group.repl_courses) == 1

        assert [('EPS 310', 'AAS 310', 'AFRO 310', 'LLS 310')] == group.repl_courses

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'H'
        assert group.goal_num == 9

        assert len(group.courses) == 33
        
        assert ('HORT 100', False) in group.courses
        assert ('HORT 105', False) in group.courses
        assert ('HORT 106', False) in group.courses
        assert ('HORT 107', False) in group.courses
        assert ('HORT 180', False) in group.courses
        assert ('HORT 199', False) in group.courses
        assert ('HORT 205', False) in group.courses
        assert ('HORT 223', False) in group.courses
        assert ('HORT 226', False) in group.courses
        assert ('HORT 240', False) in group.courses
        assert ('HORT 261', False) in group.courses
        assert ('HORT 293', False) in group.courses
        assert ('HORT 294', False) in group.courses
        assert ('HORT 295', False) in group.courses
        assert ('HORT 298', False) in group.courses
        assert ('HORT 301', False) in group.courses
        assert ('HORT 341', False) in group.courses
        assert ('HORT 344', False) in group.courses
        assert ('HORT 360', False) in group.courses
        assert ('HORT 361', False) in group.courses
        assert ('HORT 362', False) in group.courses
        assert ('HORT 363', False) in group.courses
        assert ('HORT 396', False) in group.courses
        assert ('HORT 421', False) in group.courses
        assert ('HORT 430', False) in group.courses
        assert ('HORT 434', False) in group.courses
        assert ('HORT 435', False) in group.courses
        assert ('HORT 442', False) in group.courses
        assert ('HORT 447', False) in group.courses
        assert ('HORT 453', False) in group.courses
        assert ('HORT 466', False) in group.courses
        assert ('HORT 475', False) in group.courses
        assert ('HORT 499', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 2

        assert ['HORT 393', 'HORT 395'] == group.unallowed_courses

    def test_required_courses(self):
        courses = TestHorticulture.minor.required_courses

        # test length of the list
        assert len(courses) == 2

        assert [('HORT 100', False), ('HORT 341', False)] == courses

    def test_repl_courses(self):
        courses = TestHorticulture.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestHorticulture.minor.name
        credit = TestHorticulture.minor.total_credits

        assert name == 'Horticulture'.upper()
        assert credit == 18

class TestIntegrativeBiology:
    minor = minors[36]

    def test_required_groups(self):
        group_list = TestIntegrativeBiology.minor.required_groups

        assert len(group_list) == 3

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 3

        assert ('IB 150', False) in group.courses
        assert ('IB 103', False) in group.courses
        assert ('IB 104', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'C'
        assert group.goal_num == 2

        assert len(group.courses) == 4
        
        assert ('IB 202', False) in group.courses
        assert ('IB 203', False) in group.courses
        assert ('IB 204', False) in group.courses
        assert ('IB 302', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test third group
        group = group_list[2]

        assert group.goal_type == 'C'
        assert group.goal_num == 2

        assert len(group.courses) == 49
        
        assert ('IB 335', False) in group.courses
        assert ('IB 360', False) in group.courses
        assert ('IB 362', False) in group.courses
        assert ('IB 368', False) in group.courses
        assert ('IB 401', False) in group.courses
        assert ('IB 461', False) in group.courses
        assert ('IB 462', False) in group.courses
        assert ('IB 463', False) in group.courses
        assert ('IB 471', False) in group.courses
        assert ('IB 329', False) in group.courses
        assert ('IB 361', False) in group.courses
        assert ('IB 405', False) in group.courses
        assert ('IB 430', False) in group.courses
        assert ('IB 431', False) in group.courses
        assert ('IB 432', False) in group.courses
        assert ('IB 439', False) in group.courses
        assert ('IB 440', False) in group.courses
        assert ('IB 443', False) in group.courses
        assert ('IB 444', False) in group.courses
        assert ('IB 451', False) in group.courses
        assert ('IB 452', False) in group.courses
        assert ('IB 453', False) in group.courses
        assert ('IB 481', False) in group.courses
        assert ('IB 482', False) in group.courses
        assert ('IB 485', False) in group.courses
        assert ('IB 486', False) in group.courses
        assert ('IB 494', False) in group.courses
        assert ('IB 303', False) in group.courses
        assert ('IB 364', False) in group.courses
        assert ('IB 420', False) in group.courses
        assert ('IB 421', False) in group.courses
        assert ('IB 426', False) in group.courses
        assert ('IB 427', False) in group.courses
        assert ('IB 434', False) in group.courses
        assert ('IB 435', False) in group.courses
        assert ('IB 348', False) in group.courses
        assert ('IB 411', False) in group.courses
        assert ('IB 416', False) in group.courses
        assert ('IB 436', False) in group.courses
        assert ('IB 442', False) in group.courses
        assert ('IB 467', False) in group.courses
        assert ('IB 468', False) in group.courses
        assert ('IB 476', False) in group.courses
        assert ('IB 478', False) in group.courses
        assert ('IB 483', False) in group.courses
        assert ('IB 484', False) in group.courses
        assert ('IB 487', False) in group.courses
        assert ('IB 491', False) in group.courses
        assert ('IB 492', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestIntegrativeBiology.minor.required_courses

        # test length of the list
        assert len(courses) == 0

    def test_repl_courses(self):
        courses = TestIntegrativeBiology.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestIntegrativeBiology.minor.name
        credit = TestIntegrativeBiology.minor.total_credits

        assert name == 'Integrative Biology'.upper()
        assert credit == 16

class TestInterdisciplinaryMinorInAging:
    minor = minors[37]

    def test_required_groups(self):
        group_list = TestInterdisciplinaryMinorInAging.minor.required_groups

        assert len(group_list) == 1

        # test first group
        group = group_list[0]

        assert group.goal_type == 'H'
        assert group.goal_num == 9

        assert len(group.courses) == 10

        assert ('KIN 459', False) in group.courses
        assert ('SOCW 240', False) in group.courses
        assert ('SOCW 315', False) in group.courses
        assert ('CHLH 494', False) in group.courses
        assert ('RST 316', False) in group.courses
        assert ('RST 335', False) in group.courses
        assert ('SHS 271', False) in group.courses
        assert ('KIN 386', False) in group.courses
        assert ('EPSY 407', False) in group.courses
        assert ('UP 340', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestInterdisciplinaryMinorInAging.minor.required_courses

        # test length of the list
        assert len(courses) == 3

        assert [('IHLT 240', False), ('CHLH 404', False), ('PSYC 361', False)] == courses

    def test_repl_courses(self):
        courses = TestInterdisciplinaryMinorInAging.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestInterdisciplinaryMinorInAging.minor.name
        credit = TestInterdisciplinaryMinorInAging.minor.total_credits

        assert name == 'Interdisciplinary Minor In Aging'.upper()
        assert credit == 18

class TestInternationalDevelopmentEconomics:
    minor = minors[38]

    def test_required_groups(self):
        group_list = TestInternationalDevelopmentEconomics.minor.required_groups

        assert len(group_list) == 4

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 1

        assert ('ACE 100', True) in group.courses
        
        assert len(group.repl_courses) == 1

        assert [('ACE 100', 'ECON 102')] == group.repl_courses

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 4
        
        assert ('ACE 222', False) in group.courses
        assert ('ACE 254', False) in group.courses
        assert ('ACE 255', False) in group.courses
        assert ('ACE 270', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test third group
        group = group_list[2]

        assert group.goal_type == 'C'
        assert group.goal_num == 2

        assert len(group.courses) == 6
        
        assert ('ACE 411', False) in group.courses
        assert ('ACE 436', False) in group.courses
        assert ('ACE 451', False) in group.courses
        assert ('ACE 452', False) in group.courses
        assert ('ACE 454', False) in group.courses
        assert ('ACE 455', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test fourth group
        group = group_list[3]

        assert group.goal_type == 'H'
        assert group.goal_num == 12

        assert len(group.courses) == 10
        
        assert ('ACE 222', False) in group.courses
        assert ('ACE 254', False) in group.courses
        assert ('ACE 255', False) in group.courses
        assert ('ACE 270', False) in group.courses
        assert ('ACE 411', False) in group.courses
        assert ('ACE 436', False) in group.courses
        assert ('ACE 451', False) in group.courses
        assert ('ACE 452', False) in group.courses
        assert ('ACE 454', False) in group.courses
        assert ('ACE 455', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestInternationalDevelopmentEconomics.minor.required_courses

        # test length of the list
        assert len(courses) == 0

    def test_repl_courses(self):
        courses = TestInternationalDevelopmentEconomics.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestInternationalDevelopmentEconomics.minor.name
        credit = TestInternationalDevelopmentEconomics.minor.total_credits

        assert name == 'International Development Economics'.upper()
        assert credit == 18

class TestItalian:
    minor = minors[39]

    def test_required_groups(self):
        group_list = TestItalian.minor.required_groups

        assert len(group_list) == 2

        # test first group
        group = group_list[0]

        assert group.goal_type == 'H'
        assert group.goal_num == 15

        assert len(group.courses) == 18

        assert ('ITAL 200', False) in group.courses
        assert ('ITAL 210', False) in group.courses
        assert ('ITAL 220', False) in group.courses
        assert ('ITAL 240', False) in group.courses
        assert ('ITAL 270', False) in group.courses
        assert ('ITAL 310', False) in group.courses
        assert ('ITAL 380', False) in group.courses
        assert ('ITAL 390', False) in group.courses
        assert ('ITAL 406', False) in group.courses
        assert ('ITAL 413', False) in group.courses
        assert ('ITAL 414', False) in group.courses
        assert ('EURO 415', False) in group.courses
        assert ('ITAL 420', False) in group.courses
        assert ('ITAL 440', False) in group.courses
        assert ('ITAL 450', False) in group.courses
        assert ('ITAL 470', False) in group.courses
        assert ('ITAL 490', False) in group.courses
        assert ('ITAL 491', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'H'
        assert group.goal_num == 6

        assert len(group.courses) == 10
        
        assert ('ITAL 310', False) in group.courses
        assert ('ITAL 380', False) in group.courses
        assert ('ITAL 406', False) in group.courses
        assert ('ITAL 413', False) in group.courses
        assert ('ITAL 414', False) in group.courses
        assert ('ITAL 420', False) in group.courses
        assert ('ITAL 440', False) in group.courses
        assert ('ITAL 450', False) in group.courses
        assert ('ITAL 470', False) in group.courses
        assert ('ITAL 490', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestItalian.minor.required_courses

        # test length of the list
        assert len(courses) == 1

        assert [('ITAL 104', False)] == courses

    def test_repl_courses(self):
        courses = TestItalian.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestItalian.minor.name
        credit = TestItalian.minor.total_credits

        assert name == 'Italian'.upper()
        assert credit == 19

class TestJournalism:
    minor = minors[40]

    def test_required_groups(self):
        group_list = TestJournalism.minor.required_groups

        assert len(group_list) == 1

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 2

        assert len(group.courses) == 13

        assert ('JOUR 210', False) in group.courses
        assert ('JOUR 220', False) in group.courses
        assert ('JOUR 360', False) in group.courses
        assert ('JOUR 361', False) in group.courses
        assert ('JOUR 450', False) in group.courses
        assert ('JOUR 451', False) in group.courses
        assert ('JOUR 452', False) in group.courses
        assert ('JOUR 453', False) in group.courses
        assert ('JOUR 454', False) in group.courses
        assert ('JOUR 470', False) in group.courses
        assert ('JOUR 471', False) in group.courses
        assert ('JOUR 482', False) in group.courses
        assert ('JOUR 483', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestJournalism.minor.required_courses

        # test length of the list
        assert len(courses) == 4

        assert [('JOUR 200', False), ('JOUR 205', False), ('JOUR 250', False), ('JOUR 311', False)] == courses

    def test_repl_courses(self):
        courses = TestJournalism.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestJournalism.minor.name
        credit = TestJournalism.minor.total_credits

        assert name == 'Journalism'.upper()
        assert credit == 18

class TestKinesiologyExercisePsychologyAndHealthBehavior:
    minor = minors[41]

    def test_required_groups(self):
        group_list = TestKinesiologyExercisePsychologyAndHealthBehavior.minor.required_groups

        assert len(group_list) == 1

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 4

        assert ('KIN 247', False) in group.courses
        assert ('KIN 443', False) in group.courses
        assert ('KIN 447', False) in group.courses
        assert ('KIN 474', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestKinesiologyExercisePsychologyAndHealthBehavior.minor.required_courses

        # test length of the list
        assert len(courses) == 6

        assert [('KIN 122', False), ('KIN 140', False), ('KIN 160', False), ('KIN 201', False), ('KIN 340', False), ('KIN 448', False)] == courses

    def test_repl_courses(self):
        courses = TestKinesiologyExercisePsychologyAndHealthBehavior.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestKinesiologyExercisePsychologyAndHealthBehavior.minor.name
        credit = TestKinesiologyExercisePsychologyAndHealthBehavior.minor.total_credits

        assert name == 'Kinesiology-Exercise Psychology & Health Behavior'.upper()
        assert credit == 21

class TestKinesiologyExercisePhysiology:
    minor = minors[42]

    def test_required_groups(self):
        group_list = TestKinesiologyExercisePhysiology.minor.required_groups

        assert len(group_list) == 1

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 4

        assert ('KIN 451', False) in group.courses
        assert ('KIN 452', False) in group.courses
        assert ('KIN 453', False) in group.courses
        assert ('KIN 470', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestKinesiologyExercisePhysiology.minor.required_courses

        # test length of the list
        assert len(courses) == 6

        assert [('KIN 122', False), ('KIN 140', False), ('KIN 160', False), ('KIN 201', False), ('KIN 150', False), ('KIN 352', False)] == courses

    def test_repl_courses(self):
        courses = TestKinesiologyExercisePhysiology.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestKinesiologyExercisePhysiology.minor.name
        credit = TestKinesiologyExercisePhysiology.minor.total_credits

        assert name == 'Kinesiology-Exercise Physiology'.upper()
        assert credit == 21

class TestKinesiologyTeachingAndCoachingPhysicalActivity:
    minor = minors[43]

    def test_required_groups(self):
        group_list = TestKinesiologyTeachingAndCoachingPhysicalActivity.minor.required_groups

        assert len(group_list) == 1

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 4

        assert ('KIN 360', False) in group.courses
        assert ('KIN 363', False) in group.courses
        assert ('KIN 369', False) in group.courses
        assert ('KIN 460', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestKinesiologyTeachingAndCoachingPhysicalActivity.minor.required_courses

        # test length of the list
        assert len(courses) == 6

        assert [('KIN 122', False), ('KIN 140', False), ('KIN 160', False), ('KIN 201', False), ('KIN 361', False), ('KIN 362', False)] == courses

    def test_repl_courses(self):
        courses = TestKinesiologyTeachingAndCoachingPhysicalActivity.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestKinesiologyTeachingAndCoachingPhysicalActivity.minor.name
        credit = TestKinesiologyTeachingAndCoachingPhysicalActivity.minor.total_credits

        assert name == 'Kinesiology-Teaching & Coaching Physical Activity'.upper()
        assert credit == 21

class TestKinesiologyBiomechanics:
    minor = minors[44]

    def test_required_groups(self):
        group_list = TestKinesiologyBiomechanics.minor.required_groups

        assert len(group_list) == 1

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 2

        assert ('KIN 259', False) in group.courses
        assert ('KIN 473', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestKinesiologyBiomechanics.minor.required_courses

        # test length of the list
        assert len(courses) == 6

        assert [('KIN 122', False), ('KIN 140', False), ('KIN 160', False), ('KIN 201', False), ('KIN 355', False), ('KIN 457', False)] == courses

    def test_repl_courses(self):
        courses = TestKinesiologyBiomechanics.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestKinesiologyBiomechanics.minor.name
        credit = TestKinesiologyBiomechanics.minor.total_credits

        assert name == 'Kinesiology-Biomechanics'.upper()
        assert credit == 21

class TestKinesiologyCulturalAndInterpretiveStudies:
    minor = minors[45]

    def test_required_groups(self):
        group_list = TestKinesiologyCulturalAndInterpretiveStudies.minor.required_groups

        assert len(group_list) == 1

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 3

        assert ('KIN 401', False) in group.courses
        assert ('KIN 442', False) in group.courses
        assert ('KIN 473', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestKinesiologyCulturalAndInterpretiveStudies.minor.required_courses

        # test length of the list
        assert len(courses) == 6

        assert [('KIN 122', False), ('KIN 140', False), ('KIN 160', False), ('KIN 201', False), ('KIN 249', False), ('KIN 346', False)] == courses

    def test_repl_courses(self):
        courses = TestKinesiologyCulturalAndInterpretiveStudies.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestKinesiologyCulturalAndInterpretiveStudies.minor.name
        credit = TestKinesiologyCulturalAndInterpretiveStudies.minor.total_credits

        assert name == 'Kinesiology-Cultural & Interpretive Studies'.upper()
        assert credit == 21

class TestLandscapeStudies:
    minor = minors[46]

    def test_required_groups(self):
        group_list = TestLandscapeStudies.minor.required_groups

        assert len(group_list) == 3

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 1

        assert ('LA 101', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'H'
        assert group.goal_num == 6

        assert len(group.courses) == 4
        
        assert ('LA 212', False) in group.courses
        assert ('LA 250', False) in group.courses
        assert ('LA 270', False) in group.courses
        assert ('LA 370', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test third group
        group = group_list[2]

        assert group.goal_type == 'H'
        assert group.goal_num == 9

        assert len(group.courses) == 10
        
        assert ('LA 218', False) in group.courses
        assert ('LA 220', False) in group.courses
        assert ('LA 221', False) in group.courses
        assert ('LA 222', False) in group.courses
        assert ('LA 242', False) in group.courses
        assert ('LA 314', False) in group.courses
        assert ('LA 315', False) in group.courses
        assert ('LA 390', False) in group.courses
        assert ('LA 427', False) in group.courses
        assert ('LA 470', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestLandscapeStudies.minor.required_courses

        # test length of the list
        assert len(courses) == 0

    def test_repl_courses(self):
        courses = TestLandscapeStudies.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestLandscapeStudies.minor.name
        credit = TestLandscapeStudies.minor.total_credits

        assert name == 'Landscape Studies'.upper()
        assert credit == 17

class TestLeadershipStudies:
    minor = minors[47]

    def test_required_groups(self):
        group_list = TestLeadershipStudies.minor.required_groups

        assert len(group_list) == 1

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 2

        assert len(group.courses) == 30

        assert ('ACE 231', False) in group.courses
        assert ('ACE 291', False) in group.courses
        assert ('ACES 298', False) in group.courses
        assert ('AFAS 331', False) in group.courses
        assert ('AFAS 332', False) in group.courses
        assert ('AGCM 430', False) in group.courses
        assert ('LEAD 230', False) in group.courses
        assert ('LEAD 340', False) in group.courses
        assert ('AGED 360', False) in group.courses
        assert ('AHS 365', False) in group.courses
        assert ('ANSC 471', False) in group.courses
        assert ('BADM 310', False) in group.courses
        assert ('BADM 311', False) in group.courses
        assert ('BADM 314', False) in group.courses
        assert ('CMN 321', False) in group.courses
        assert ('ENG 315', False) in group.courses
        assert ('ENG 598', False) in group.courses
        assert ('IHLT 230', False) in group.courses
        assert ('JOUR 250', False) in group.courses
        assert ('KIN 369', False) in group.courses
        assert ('MILS 341', False) in group.courses
        assert ('MILS 342', False) in group.courses
        assert ('NS 303', False) in group.courses
        assert ('NS 308', False) in group.courses
        assert ('PHIL 436', False) in group.courses
        assert ('PS 304', False) in group.courses
        assert ('PSYC 455', False) in group.courses
        assert ('RST 200', False) in group.courses
        assert ('SE 361', False) in group.courses
        assert ('SOCW 321', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestLeadershipStudies.minor.required_courses

        # test length of the list
        assert len(courses) == 4

        assert [('LEAD 260', False), ('LEAD 380', False), ('PSYC 245', False), ('LEAD 480', False)] == courses

    def test_repl_courses(self):
        courses = TestLeadershipStudies.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestLeadershipStudies.minor.name
        credit = TestLeadershipStudies.minor.total_credits

        assert name == 'Leadership Studies'.upper()
        assert credit == 17

class TestLegalStudiesLawAndPoliticsTrack:
    minor = minors[48]

    def test_required_groups(self):
        group_list = TestLegalStudiesLawAndPoliticsTrack.minor.required_groups

        assert len(group_list) == 2

        # test first group
        group = group_list[0]

        assert group.goal_type == 'H'
        assert group.goal_num == 9

        assert len(group.courses) == 9

        assert ('LAW 201', False) in group.courses
        assert ('LAW 301', False) in group.courses
        assert ('LAW 302', False) in group.courses
        assert ('LAW 303', False) in group.courses
        assert ('LAW 304', False) in group.courses
        assert ('LAW 305', False) in group.courses
        assert ('EPS 310', True) in group.courses
        assert ('SOC 479', False) in group.courses
        assert ('PS 323', False) in group.courses
        
        assert len(group.repl_courses) == 1

        assert [('EPS 310', 'AAS 310', 'AFRO 310', 'LLS 310')] == group.repl_courses

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'H'
        assert group.goal_num == 9

        assert len(group.courses) == 6
        
        assert ('PS 301', False) in group.courses
        assert ('PS 302', False) in group.courses
        assert ('PS 305', False) in group.courses
        assert ('PS 306', False) in group.courses
        assert ('PS 322', False) in group.courses
        assert ('PS 386', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestLegalStudiesLawAndPoliticsTrack.minor.required_courses

        # test length of the list
        assert len(courses) == 0

    def test_repl_courses(self):
        courses = TestLegalStudiesLawAndPoliticsTrack.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestLegalStudiesLawAndPoliticsTrack.minor.name
        credit = TestLegalStudiesLawAndPoliticsTrack.minor.total_credits

        assert name == 'Legal Studies Law & Politics Track'.upper()
        assert credit == 18
    
class TestLegalStudiesLawAndCulturesTrack:
    minor = minors[49]

    def test_required_groups(self):
        group_list = TestLegalStudiesLawAndCulturesTrack.minor.required_groups

        assert len(group_list) == 3

        # test first group
        group = group_list[0]

        assert group.goal_type == 'H'
        assert group.goal_num == 9

        assert len(group.courses) == 9

        assert ('LAW 201', False) in group.courses
        assert ('LAW 301', False) in group.courses
        assert ('LAW 302', False) in group.courses
        assert ('LAW 303', False) in group.courses
        assert ('LAW 304', False) in group.courses
        assert ('LAW 305', False) in group.courses
        assert ('EPS 310', True) in group.courses
        assert ('SOC 479', False) in group.courses
        assert ('PS 323', False) in group.courses
        
        assert len(group.repl_courses) == 1

        assert [('EPS 310', 'AAS 310', 'AFRO 310', 'LLS 310')] == group.repl_courses

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'H'
        assert group.goal_num == 9

        assert len(group.courses) == 8
        
        assert ('AAS 370', True) in group.courses
        assert ('LLS 343', True) in group.courses
        assert ('LLS 473', False) in group.courses
        assert ('AFRO 378', True) in group.courses
        assert ('GLBL 220', False) in group.courses
        assert ('GLBL 260', False) in group.courses
        assert ('PS 201', True) in group.courses
        assert ('GWS 201', True) in group.courses

        assert len(group.repl_courses) == 5

        assert [('AAS 370', 'LLS 372'), ('LLS 343', 'AIS 343', 'AFRO 343', 'AAS 343', 'GWS 343'), 
        ('AFRO 378', 'HIST 389'), ('PS 201', 'AAS 201', 'AFRO 201', 'LLS 201'), ('GWS 201', 'SOC 201')] == group.repl_courses

        assert len(group.unallowed_courses) == 0

        # test third group
        group = group_list[2]

        assert group.goal_type == 'H'
        assert group.goal_num == 6

        assert len(group.courses) == 4
        
        assert ('AAS 370', True) in group.courses
        assert ('LLS 343', True) in group.courses
        assert ('LLS 473', False) in group.courses
        assert ('AFRO 378', True) in group.courses

        assert len(group.repl_courses) == 3

        assert [('AAS 370', 'LLS 372'), ('LLS 343', 'AIS 343', 'AFRO 343', 'AAS 343', 'GWS 343'), 
        ('AFRO 378', 'HIST 389')] == group.repl_courses

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestLegalStudiesLawAndCulturesTrack.minor.required_courses

        # test length of the list
        assert len(courses) == 0

    def test_repl_courses(self):
        courses = TestLegalStudiesLawAndCulturesTrack.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestLegalStudiesLawAndCulturesTrack.minor.name
        credit = TestLegalStudiesLawAndCulturesTrack.minor.total_credits

        assert name == 'Legal Studies Law & Cultures Track'.upper()
        assert credit == 18

class TestLegalStudiesLawAndEconomicsOfFoodSecurityTrack:
    minor = minors[50]

    def test_required_groups(self):
        group_list = TestLegalStudiesLawAndEconomicsOfFoodSecurityTrack.minor.required_groups

        assert len(group_list) == 3

        # test first group
        group = group_list[0]

        assert group.goal_type == 'H'
        assert group.goal_num == 9

        assert len(group.courses) == 9

        assert ('LAW 201', False) in group.courses
        assert ('LAW 301', False) in group.courses
        assert ('LAW 302', False) in group.courses
        assert ('LAW 303', False) in group.courses
        assert ('LAW 304', False) in group.courses
        assert ('LAW 305', False) in group.courses
        assert ('EPS 310', True) in group.courses
        assert ('SOC 479', False) in group.courses
        assert ('PS 323', False) in group.courses
        
        assert len(group.repl_courses) == 1

        assert [('EPS 310', 'AAS 310', 'AFRO 310', 'LLS 310')] == group.repl_courses

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'H'
        assert group.goal_num == 9

        assert len(group.courses) == 11
        
        assert ('ACE 210', False) in group.courses
        assert ('ACE 251', False) in group.courses
        assert ('ACE 255', False) in group.courses
        assert ('ACE 306', False) in group.courses
        assert ('ACE 310', False) in group.courses
        assert ('ACE 321', False) in group.courses
        assert ('ACE 403', False) in group.courses
        assert ('ACE 406', False) in group.courses
        assert ('ACE 410', False) in group.courses
        assert ('ACE 411', False) in group.courses
        assert ('ACE 456', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test third group
        group = group_list[2]

        assert group.goal_type == 'H'
        assert group.goal_num == 6

        assert len(group.courses) == 8
        
        assert ('ACE 306', False) in group.courses
        assert ('ACE 310', False) in group.courses
        assert ('ACE 321', False) in group.courses
        assert ('ACE 403', False) in group.courses
        assert ('ACE 406', False) in group.courses
        assert ('ACE 410', False) in group.courses
        assert ('ACE 411', False) in group.courses
        assert ('ACE 456', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestLegalStudiesLawAndEconomicsOfFoodSecurityTrack.minor.required_courses

        # test length of the list
        assert len(courses) == 0

    def test_repl_courses(self):
        courses = TestLegalStudiesLawAndEconomicsOfFoodSecurityTrack.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestLegalStudiesLawAndEconomicsOfFoodSecurityTrack.minor.name
        credit = TestLegalStudiesLawAndEconomicsOfFoodSecurityTrack.minor.total_credits

        assert name == 'Legal Studies Law & Economics of Food Security Track'.upper()
        assert credit == 18

class TestLinguistics:
    minor = minors[51]

    def test_required_groups(self):
        group_list = TestLinguistics.minor.required_groups

        assert len(group_list) == 3

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 2

        assert len(group.courses) == 3

        assert ('LING 301', False) in group.courses
        assert ('LING 302', False) in group.courses
        assert ('LING 307', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'H'
        assert group.goal_num == 6

        assert len(group.courses) == 9
        
        assert ('LING 301', False) in group.courses
        assert ('LING 302', False) in group.courses
        assert ('LING 307', False) in group.courses
        assert ('LING 210', False) in group.courses
        assert ('LING 225', False) in group.courses
        assert ('LING 250', False) in group.courses
        assert ('LING 400', False) in group.courses
        assert ('LING 401', False) in group.courses
        assert ('LING 406', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test third group
        group = group_list[2]

        assert group.goal_type == 'H'
        assert group.goal_num == 3

        assert len(group.courses) == 79
        
        assert ('LING 100', False) in group.courses
        assert ('LING 104', False) in group.courses
        assert ('LING 110', False) in group.courses
        assert ('LING 111', False) in group.courses
        assert ('LING 115', False) in group.courses
        assert ('LING 191', False) in group.courses
        assert ('LING 199', False) in group.courses
        assert ('LING 210', False) in group.courses
        assert ('LING 221', False) in group.courses
        assert ('LING 225', False) in group.courses
        assert ('LING 240', False) in group.courses
        assert ('LING 250', False) in group.courses
        assert ('LING 270', False) in group.courses
        assert ('LING 290', False) in group.courses
        assert ('LING 291', False) in group.courses
        assert ('LING 300', False) in group.courses
        assert ('LING 301', False) in group.courses
        assert ('LING 302', False) in group.courses
        assert ('LING 303', False) in group.courses
        assert ('LING 304', False) in group.courses
        assert ('LING 307', False) in group.courses
        assert ('LING 321', False) in group.courses
        assert ('LING 357', False) in group.courses
        assert ('LING 391', False) in group.courses
        assert ('LING 400', False) in group.courses
        assert ('LING 401', False) in group.courses
        assert ('LING 402', False) in group.courses
        assert ('LING 404', False) in group.courses
        assert ('LING 406', False) in group.courses
        assert ('LING 407', False) in group.courses
        assert ('LING 410', False) in group.courses
        assert ('LING 412', False) in group.courses
        assert ('LING 415', False) in group.courses
        assert ('LING 416', False) in group.courses
        assert ('LING 418', False) in group.courses
        assert ('LING 423', False) in group.courses
        assert ('LING 425', False) in group.courses
        assert ('LING 426', False) in group.courses
        assert ('LING 427', False) in group.courses
        assert ('LING 430', False) in group.courses
        assert ('LING 432', False) in group.courses
        assert ('LING 438', False) in group.courses
        assert ('LING 450', False) in group.courses
        assert ('LING 462', False) in group.courses
        assert ('LING 469', False) in group.courses
        assert ('LING 480', False) in group.courses
        assert ('LING 489', False) in group.courses
        assert ('LING 490', False) in group.courses
        assert ('LING 501', False) in group.courses
        assert ('LING 502', False) in group.courses
        assert ('LING 504', False) in group.courses
        assert ('LING 506', False) in group.courses
        assert ('LING 507', False) in group.courses
        assert ('LING 512', False) in group.courses
        assert ('LING 514', False) in group.courses
        assert ('LING 516', False) in group.courses
        assert ('LING 518', False) in group.courses
        assert ('LING 520', False) in group.courses
        assert ('LING 522', False) in group.courses
        assert ('LING 524', False) in group.courses
        assert ('LING 525', False) in group.courses
        assert ('LING 529', False) in group.courses
        assert ('LING 541', False) in group.courses
        assert ('LING 542', False) in group.courses
        assert ('LING 547', False) in group.courses
        assert ('LING 550', False) in group.courses
        assert ('LING 551', False) in group.courses
        assert ('LING 559', False) in group.courses
        assert ('LING 560', False) in group.courses
        assert ('LING 570', False) in group.courses
        assert ('LING 575', False) in group.courses
        assert ('LING 576', False) in group.courses
        assert ('LING 582', False) in group.courses
        assert ('LING 584', False) in group.courses
        assert ('LING 587', False) in group.courses
        assert ('LING 588', False) in group.courses
        assert ('LING 590', False) in group.courses
        assert ('LING 591', False) in group.courses
        assert ('LING 599', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestLinguistics.minor.required_courses

        # test length of the list
        assert len(courses) == 1

        assert [('LING 100', False)] == courses

    def test_repl_courses(self):
        courses = TestLinguistics.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestLinguistics.minor.name
        credit = TestLinguistics.minor.total_credits

        assert name == 'Linguistics'.upper()
        assert credit == 18

class TestMaterialsScienceAndEngineering:
    minor = minors[52]

    def test_required_groups(self):
        group_list = TestMaterialsScienceAndEngineering.minor.required_groups

        assert len(group_list) == 2

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 5

        assert ('MSE 304', False) in group.courses
        assert ('MSE 402', False) in group.courses
        assert ('MSE 403', False) in group.courses
        assert ('MSE 405', False) in group.courses
        assert ('MSE 406', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'H'
        assert group.goal_num == 9

        assert len(group.courses) == 29
        
        assert ('MSE 404', False) in group.courses
        assert ('MSE 420', False) in group.courses
        assert ('MSE 421', False) in group.courses
        assert ('MSE 422', False) in group.courses
        assert ('MSE 440', False) in group.courses
        assert ('MSE 441', False) in group.courses
        assert ('MSE 443', False) in group.courses
        assert ('MSE 445', False) in group.courses
        assert ('MSE 450', False) in group.courses
        assert ('MSE 453', False) in group.courses
        assert ('MSE 454', False) in group.courses
        assert ('MSE 455', False) in group.courses
        assert ('MSE 456', False) in group.courses
        assert ('MSE 457', False) in group.courses
        assert ('MSE 458', False) in group.courses
        assert ('MSE 460', False) in group.courses
        assert ('MSE 461', False) in group.courses
        assert ('MSE 466', False) in group.courses
        assert ('MSE 470', False) in group.courses
        assert ('MSE 473', False) in group.courses
        assert ('MSE 474', False) in group.courses
        assert ('MSE 480', False) in group.courses
        assert ('MSE 481', False) in group.courses
        assert ('MSE 484', False) in group.courses
        assert ('MSE 485', False) in group.courses
        assert ('MSE 487', False) in group.courses
        assert ('MSE 488', False) in group.courses
        assert ('MSE 489', False) in group.courses
        assert ('ECE 444', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestMaterialsScienceAndEngineering.minor.required_courses

        # test length of the list
        assert len(courses) == 2

        assert [('MSE 280', False), ('MSE 401', False)] == courses

    def test_repl_courses(self):
        courses = TestMaterialsScienceAndEngineering.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestMaterialsScienceAndEngineering.minor.name
        credit = TestMaterialsScienceAndEngineering.minor.total_credits

        assert name == 'Materials Science & Engineering'.upper()
        assert credit == 18

class TestMusicalTheatreForPerformingArtistsDanceMajors:
    minor = minors[53]

    def test_required_groups(self):
        group_list = TestMusicalTheatreForPerformingArtistsDanceMajors.minor.required_groups

        assert len(group_list) == 0

    def test_required_courses(self):
        courses = TestMusicalTheatreForPerformingArtistsDanceMajors.minor.required_courses

        # test length of the list
        assert len(courses) == 8

        assert [('MUS 103', False), ('MUS 222', False), ('THEA 170', False), ('MUS 107', False), ('MUS 181', False), 
        ('MUS 422', False), ('MUS 472', False), ('DANC 209', False)] == courses

    def test_repl_courses(self):
        courses = TestMusicalTheatreForPerformingArtistsDanceMajors.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestMusicalTheatreForPerformingArtistsDanceMajors.minor.name
        credit = TestMusicalTheatreForPerformingArtistsDanceMajors.minor.total_credits

        assert name == 'Musical Theatre for Performing Artists Dance Majors'.upper()
        assert credit == 21

class TestMusicalTheatreForPerformingArtistsActingConcentrationInTheatreMajors:
    minor = minors[54]

    def test_required_groups(self):
        group_list = TestMusicalTheatreForPerformingArtistsActingConcentrationInTheatreMajors.minor.required_groups

        assert len(group_list) == 0

    def test_required_courses(self):
        courses = TestMusicalTheatreForPerformingArtistsActingConcentrationInTheatreMajors.minor.required_courses

        # test length of the list
        assert len(courses) == 9

        assert [('MUS 103', False), ('MUS 222', False), ('DANC 101', False), ('DANC 107', False), ('MUS 107', False), ('MUS 181', False), 
        ('MUS 422', False), ('MUS 472', False), ('DANC 209', False)] == courses

    def test_repl_courses(self):
        courses = TestMusicalTheatreForPerformingArtistsActingConcentrationInTheatreMajors.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestMusicalTheatreForPerformingArtistsActingConcentrationInTheatreMajors.minor.name
        credit = TestMusicalTheatreForPerformingArtistsActingConcentrationInTheatreMajors.minor.total_credits

        assert name == 'Musical Theatre for Performing Artists Acting Concentration in Theatre Majors'.upper()
        assert credit == 22
    
class TestNaturalResourceConservation:
    minor = minors[55]

    def test_required_groups(self):
        group_list = TestNaturalResourceConservation.minor.required_groups

        assert len(group_list) == 2

        # test first group
        group = group_list[0]

        assert group.goal_type == 'H'
        assert group.goal_num == 12

        assert len(group.courses) == 32

        assert ('NRES 108', False) in group.courses
        assert ('NRES 109', False) in group.courses
        assert ('NRES 201', False) in group.courses
        assert ('ACE 210', False) in group.courses
        assert ('NRES 210', False) in group.courses
        assert ('NRES 219', False) in group.courses
        assert ('ACE 310', False) in group.courses
        assert ('NRES 310', False) in group.courses
        assert ('NRES 325', False) in group.courses
        assert ('NRES 340', False) in group.courses
        assert ('NRES 348', False) in group.courses
        assert ('NRES 351', False) in group.courses
        assert ('NRES 407', False) in group.courses
        assert ('NRES 409', False) in group.courses
        assert ('NRES 415', False) in group.courses
        assert ('NRES 419', False) in group.courses
        assert ('NRES 420', False) in group.courses
        assert ('NRES 421', False) in group.courses
        assert ('NRES 424', False) in group.courses
        assert ('NRES 425', False) in group.courses
        assert ('NRES 426', False) in group.courses
        assert ('NRES 427', False) in group.courses
        assert ('NRES 429', False) in group.courses
        assert ('NRES 438', False) in group.courses
        assert ('NRES 439', False) in group.courses
        assert ('NRES 454', False) in group.courses
        assert ('NRES 455', False) in group.courses
        assert ('NRES 471', False) in group.courses
        assert ('NRES 472', False) in group.courses
        assert ('NRES 474', False) in group.courses
        assert ('NRES 475', False) in group.courses
        assert ('NRES 488', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'H'
        assert group.goal_num == 6

        assert len(group.courses) == 20
        
        assert ('NRES 407', False) in group.courses
        assert ('NRES 409', False) in group.courses
        assert ('NRES 415', False) in group.courses
        assert ('NRES 419', False) in group.courses
        assert ('NRES 420', False) in group.courses
        assert ('NRES 421', False) in group.courses
        assert ('NRES 424', False) in group.courses
        assert ('NRES 425', False) in group.courses
        assert ('NRES 426', False) in group.courses
        assert ('NRES 427', False) in group.courses
        assert ('NRES 429', False) in group.courses
        assert ('NRES 438', False) in group.courses
        assert ('NRES 439', False) in group.courses
        assert ('NRES 454', False) in group.courses
        assert ('NRES 455', False) in group.courses
        assert ('NRES 471', False) in group.courses
        assert ('NRES 472', False) in group.courses
        assert ('NRES 474', False) in group.courses
        assert ('NRES 475', False) in group.courses
        assert ('NRES 488', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestNaturalResourceConservation.minor.required_courses

        # test length of the list
        assert len(courses) == 2

        assert [('NRES 102', True), ('NRES 287', False)] == courses

    def test_repl_courses(self):
        courses = TestNaturalResourceConservation.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 1

        assert [('NRES 102', 'NRES 100')] == courses

    def test_minor(self):
        name = TestNaturalResourceConservation.minor.name
        credit = TestNaturalResourceConservation.minor.total_credits

        assert name == 'Natural Resource Conservation'.upper()
        assert credit == 18

class TestNutrition:
    minor = minors[56]

    def test_required_groups(self):
        group_list = TestNutrition.minor.required_groups

        assert len(group_list) == 1

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 2

        assert len(group.courses) == 5

        assert ('ANSC 420', False) in group.courses
        assert ('FSHN 322', False) in group.courses
        assert ('FSHN 421', False) in group.courses
        assert ('FSHN 428', False) in group.courses
        assert ('FSHN 429', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestNutrition.minor.required_courses

        # test length of the list
        assert len(courses) == 4

        assert [('FSHN 220', False), ('FSHN 420', False), ('FSHN 426', False), ('FSHN 427', False)] == courses

    def test_repl_courses(self):
        courses = TestNutrition.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestNutrition.minor.name
        credit = TestNutrition.minor.total_credits

        assert name == 'Nutrition'.upper()
        assert credit == 19

class TestPhilosophy:
    minor = minors[57]

    def test_required_groups(self):
        group_list = TestPhilosophy.minor.required_groups

        assert len(group_list) == 2

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 2

        assert len(group.courses) == 35

        assert ('PHIL 307', False) in group.courses
        assert ('PHIL 316', False) in group.courses
        assert ('PHIL 351', False) in group.courses
        assert ('PHIL 380', False) in group.courses
        assert ('PHIL 390', False) in group.courses
        assert ('PHIL 404', False) in group.courses
        assert ('PHIL 407', False) in group.courses
        assert ('PHIL 410', False) in group.courses
        assert ('PHIL 411', False) in group.courses
        assert ('PHIL 412', False) in group.courses
        assert ('PHIL 414', False) in group.courses
        assert ('PHIL 419', False) in group.courses
        assert ('PHIL 420', False) in group.courses
        assert ('PHIL 421', False) in group.courses
        assert ('PHIL 422', False) in group.courses
        assert ('PHIL 424', False) in group.courses
        assert ('PHIL 425', False) in group.courses
        assert ('PHIL 426', False) in group.courses
        assert ('PHIL 429', False) in group.courses
        assert ('PHIL 430', False) in group.courses
        assert ('PHIL 433', False) in group.courses
        assert ('PHIL 435', False) in group.courses
        assert ('PHIL 436', False) in group.courses
        assert ('PHIL 438', False) in group.courses
        assert ('PHIL 439', False) in group.courses
        assert ('PHIL 441', False) in group.courses
        assert ('PHIL 443', False) in group.courses
        assert ('PHIL 453', False) in group.courses
        assert ('PHIL 454', False) in group.courses
        assert ('PHIL 458', False) in group.courses
        assert ('PHIL 471', False) in group.courses
        assert ('PHIL 472', False) in group.courses
        assert ('PHIL 477', False) in group.courses
        assert ('PHIL 492', False) in group.courses
        assert ('PHIL 499', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 58
        
        assert ('PHIL 100', False) in group.courses
        assert ('PHIL 101', False) in group.courses
        assert ('PHIL 102', False) in group.courses
        assert ('PHIL 103', False) in group.courses
        assert ('PHIL 104', False) in group.courses
        assert ('PHIL 105', False) in group.courses
        assert ('PHIL 106', False) in group.courses
        assert ('PHIL 107', False) in group.courses
        assert ('PHIL 108', False) in group.courses
        assert ('PHIL 109', False) in group.courses
        assert ('PHIL 110', False) in group.courses
        assert ('PHIL 198', False) in group.courses
        assert ('PHIL 199', False) in group.courses
        assert ('PHIL 201', False) in group.courses
        assert ('PHIL 202', False) in group.courses
        assert ('PHIL 203', False) in group.courses
        assert ('PHIL 206', False) in group.courses
        assert ('PHIL 210', False) in group.courses
        assert ('PHIL 214', False) in group.courses
        assert ('PHIL 230', False) in group.courses
        assert ('PHIL 231', False) in group.courses
        assert ('PHIL 250', False) in group.courses
        assert ('PHIL 270', False) in group.courses
        assert ('PHIL 307', False) in group.courses
        assert ('PHIL 316', False) in group.courses
        assert ('PHIL 351', False) in group.courses
        assert ('PHIL 380', False) in group.courses
        assert ('PHIL 390', False) in group.courses
        assert ('PHIL 404', False) in group.courses
        assert ('PHIL 407', False) in group.courses
        assert ('PHIL 410', False) in group.courses
        assert ('PHIL 411', False) in group.courses
        assert ('PHIL 412', False) in group.courses
        assert ('PHIL 414', False) in group.courses
        assert ('PHIL 419', False) in group.courses
        assert ('PHIL 420', False) in group.courses
        assert ('PHIL 421', False) in group.courses
        assert ('PHIL 422', False) in group.courses
        assert ('PHIL 424', False) in group.courses
        assert ('PHIL 425', False) in group.courses
        assert ('PHIL 426', False) in group.courses
        assert ('PHIL 429', False) in group.courses
        assert ('PHIL 430', False) in group.courses
        assert ('PHIL 433', False) in group.courses
        assert ('PHIL 435', False) in group.courses
        assert ('PHIL 436', False) in group.courses
        assert ('PHIL 438', False) in group.courses
        assert ('PHIL 439', False) in group.courses
        assert ('PHIL 441', False) in group.courses
        assert ('PHIL 443', False) in group.courses
        assert ('PHIL 453', False) in group.courses
        assert ('PHIL 454', False) in group.courses
        assert ('PHIL 458', False) in group.courses
        assert ('PHIL 471', False) in group.courses
        assert ('PHIL 472', False) in group.courses
        assert ('PHIL 477', False) in group.courses
        assert ('PHIL 492', False) in group.courses
        assert ('PHIL 499', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestPhilosophy.minor.required_courses

        # test length of the list
        assert len(courses) == 3

        assert [('PHIL 203', False), ('PHIL 206', False), ('PHIL 103', True)] == courses

    def test_repl_courses(self):
        courses = TestPhilosophy.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 1

        assert [('PHIL 103', 'PHIL 202')] == courses

    def test_minor(self):
        name = TestPhilosophy.minor.name
        credit = TestPhilosophy.minor.total_credits

        assert name == 'Philosophy'.upper()
        assert credit == 20

class TestPhysics:
    minor = minors[58]

    def test_required_groups(self):
        group_list = TestPhysics.minor.required_groups

        assert len(group_list) == 1

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 2

        assert len(group.courses) == 24

        assert ('PHYS 325', False) in group.courses
        assert ('PHYS 326', False) in group.courses
        assert ('PHYS 329', False) in group.courses
        assert ('PHYS 330', False) in group.courses
        assert ('PHYS 398', False) in group.courses
        assert ('PHYS 401', False) in group.courses
        assert ('PHYS 402', False) in group.courses
        assert ('PHYS 403', False) in group.courses
        assert ('PHYS 404', False) in group.courses
        assert ('PHYS 406', False) in group.courses
        assert ('PHYS 427', False) in group.courses
        assert ('PHYS 435', False) in group.courses
        assert ('PHYS 436', False) in group.courses
        assert ('PHYS 460', False) in group.courses
        assert ('PHYS 466', False) in group.courses
        assert ('PHYS 470', False) in group.courses
        assert ('PHYS 475', False) in group.courses
        assert ('PHYS 485', False) in group.courses
        assert ('PHYS 486', False) in group.courses
        assert ('PHYS 487', False) in group.courses
        assert ('PHYS 496', False) in group.courses
        assert ('PHYS 497', False) in group.courses
        assert ('PHYS 498', False) in group.courses
        assert ('PHYS 499', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 2

        assert ['PHYS 419', 'PHYS 420'] == group.unallowed_courses

    def test_required_courses(self):
        courses = TestPhysics.minor.required_courses

        # test length of the list
        assert len(courses) == 5

        assert [('PHYS 211', False), ('PHYS 212', False), ('PHYS 213', True), ('PHYS 225', False), ('PHYS 325', False)] == courses

    def test_repl_courses(self):
        courses = TestPhysics.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 1

        assert [('PHYS 213', 'PHYS 214')] == courses

    def test_minor(self):
        name = TestPhysics.minor.name
        credit = TestPhysics.minor.total_credits

        assert name == 'Physics'.upper()
        assert credit == 21

class TestPoliticalScience:
    minor = minors[59]

    def test_required_groups(self):
        group_list = TestPoliticalScience.minor.required_groups

        assert len(group_list) == 2

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 2

        assert len(group.courses) == 29

        assert ('PS 100', False) in group.courses
        assert ('PS 101', False) in group.courses
        assert ('PS 125', False) in group.courses
        assert ('PS 152', False) in group.courses
        assert ('PS 170', False) in group.courses
        assert ('PS 180', False) in group.courses
        assert ('PS 191', False) in group.courses
        assert ('PS 199', False) in group.courses
        assert ('PS 201', False) in group.courses
        assert ('PS 202', False) in group.courses
        assert ('PS 220', False) in group.courses
        assert ('PS 224', False) in group.courses
        assert ('PS 225', False) in group.courses
        assert ('PS 230', False) in group.courses
        assert ('PS 231', False) in group.courses
        assert ('PS 240', False) in group.courses
        assert ('PS 241', False) in group.courses
        assert ('PS 242', False) in group.courses
        assert ('PS 243', False) in group.courses
        assert ('PS 270', False) in group.courses
        assert ('PS 272', False) in group.courses
        assert ('PS 273', False) in group.courses
        assert ('PS 280', False) in group.courses
        assert ('PS 281', False) in group.courses
        assert ('PS 282', False) in group.courses
        assert ('PS 283', False) in group.courses
        assert ('PS 291', False) in group.courses
        assert ('PS 292', False) in group.courses
        assert ('PS 299', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'C'
        assert group.goal_num == 3

        assert len(group.courses) == 81
        
        assert ('PS 300', False) in group.courses
        assert ('PS 301', False) in group.courses
        assert ('PS 302', False) in group.courses
        assert ('PS 303', False) in group.courses
        assert ('PS 304', False) in group.courses
        assert ('PS 305', False) in group.courses
        assert ('PS 306', False) in group.courses
        assert ('PS 307', False) in group.courses
        assert ('PS 309', False) in group.courses
        assert ('PS 310', False) in group.courses
        assert ('PS 311', False) in group.courses
        assert ('PS 312', False) in group.courses
        assert ('PS 313', False) in group.courses
        assert ('PS 314', False) in group.courses
        assert ('PS 315', False) in group.courses
        assert ('PS 316', False) in group.courses
        assert ('PS 317', False) in group.courses
        assert ('PS 318', False) in group.courses
        assert ('PS 319', False) in group.courses
        assert ('PS 320', False) in group.courses
        assert ('PS 321', False) in group.courses
        assert ('PS 322', False) in group.courses
        assert ('PS 323', False) in group.courses
        assert ('PS 328', False) in group.courses
        assert ('PS 329', False) in group.courses
        assert ('PS 330', False) in group.courses
        assert ('PS 331', False) in group.courses
        assert ('PS 340', False) in group.courses
        assert ('PS 341', False) in group.courses
        assert ('PS 343', False) in group.courses
        assert ('PS 345', False) in group.courses
        assert ('PS 346', False) in group.courses
        assert ('PS 347', False) in group.courses
        assert ('PS 348', False) in group.courses
        assert ('PS 351', False) in group.courses
        assert ('PS 352', False) in group.courses
        assert ('PS 353', False) in group.courses
        assert ('PS 355', False) in group.courses
        assert ('PS 356', False) in group.courses
        assert ('PS 357', False) in group.courses
        assert ('PS 358', False) in group.courses
        assert ('PS 370', False) in group.courses
        assert ('PS 371', False) in group.courses
        assert ('PS 372', False) in group.courses
        assert ('PS 373', False) in group.courses
        assert ('PS 374', False) in group.courses
        assert ('PS 375', False) in group.courses
        assert ('PS 376', False) in group.courses
        assert ('PS 377', False) in group.courses
        assert ('PS 379', False) in group.courses
        assert ('PS 380', False) in group.courses
        assert ('PS 382', False) in group.courses
        assert ('PS 384', False) in group.courses
        assert ('PS 385', False) in group.courses
        assert ('PS 386', False) in group.courses
        assert ('PS 387', False) in group.courses
        assert ('PS 389', False) in group.courses
        assert ('PS 390', False) in group.courses
        assert ('PS 391', False) in group.courses
        assert ('PS 392', False) in group.courses
        assert ('PS 393', False) in group.courses
        assert ('PS 394', False) in group.courses
        assert ('PS 395', False) in group.courses
        assert ('PS 396', False) in group.courses
        assert ('PS 397', False) in group.courses
        assert ('PS 398', False) in group.courses
        assert ('PS 399', False) in group.courses
        assert ('PS 408', False) in group.courses
        assert ('PS 411', False) in group.courses
        assert ('PS 413', False) in group.courses
        assert ('PS 415', False) in group.courses
        assert ('PS 418', False) in group.courses
        assert ('PS 456', False) in group.courses
        assert ('PS 457', False) in group.courses
        assert ('PS 480', False) in group.courses
        assert ('PS 490', False) in group.courses
        assert ('PS 491', False) in group.courses
        assert ('PS 492', False) in group.courses
        assert ('PS 494', False) in group.courses
        assert ('PS 495', False) in group.courses
        assert ('PS 496', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestPoliticalScience.minor.required_courses

        # test length of the list
        assert len(courses) == 1

        assert [('PS 100', False)] == courses

    def test_repl_courses(self):
        courses = TestPoliticalScience.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestPoliticalScience.minor.name
        credit = TestPoliticalScience.minor.total_credits

        assert name == 'Political Science'.upper()
        assert credit == 18

class TestPolymerScienceAndEngineering:
    minor = minors[60]

    def test_required_groups(self):
        group_list = TestPolymerScienceAndEngineering.minor.required_groups

        assert len(group_list) == 2

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 6

        assert ('CHBE 321', False) in group.courses
        assert ('CHEM 442', False) in group.courses
        assert ('CHEM 444', False) in group.courses
        assert ('ME 200', False) in group.courses
        assert ('MSE 401', False) in group.courses
        assert ('PHYS 427', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'C'
        assert group.goal_num == 2

        assert len(group.courses) == 9
        
        assert ('CHEM 436', False) in group.courses
        assert ('CHEM 437', False) in group.courses
        assert ('ME 450', False) in group.courses
        assert ('MSE 455', False) in group.courses
        assert ('MSE 457', False) in group.courses
        assert ('MSE 458', False) in group.courses
        assert ('MSE 480', False) in group.courses
        assert ('FSHN 469', False) in group.courses
        assert ('TAM 427', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestPolymerScienceAndEngineering.minor.required_courses

        # test length of the list
        assert len(courses) == 5

        assert [('MSE 450', True), ('MSE 452', False), ('MSE 453', False), ('TAM 251', False), ('CHEM 236', False)] == courses

    def test_repl_courses(self):
        courses = TestPolymerScienceAndEngineering.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 1

        assert [('MSE 450', 'CHBE 456')] == courses

    def test_minor(self):
        name = TestPolymerScienceAndEngineering.minor.name
        credit = TestPolymerScienceAndEngineering.minor.total_credits

        assert name == 'Polymer Science & Engineering'.upper()
        assert credit == 25

class TestPortuguese:
    minor = minors[61]

    def test_required_groups(self):
        group_list = TestPortuguese.minor.required_groups

        assert len(group_list) == 1

        # test first group
        group = group_list[0]

        assert group.goal_type == 'H'
        assert group.goal_num == 9

        assert len(group.courses) == 4

        assert ('PORT 403', False) in group.courses
        assert ('PORT 404', False) in group.courses
        assert ('PORT 406', False) in group.courses
        assert ('PORT 410', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestPortuguese.minor.required_courses

        # test length of the list
        assert len(courses) == 2

        assert [('PORT 401', False), ('PORT 402', False)] == courses

    def test_repl_courses(self):
        courses = TestPortuguese.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestPortuguese.minor.name
        credit = TestPortuguese.minor.total_credits

        assert name == 'Portuguese'.upper()
        assert credit == 16

class TestPsychology:
    minor = minors[62]

    def test_required_groups(self):
        group_list = TestPsychology.minor.required_groups

        assert len(group_list) == 3

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 6

        assert ('PSYC 204', False) in group.courses
        assert ('PSYC 210', False) in group.courses
        assert ('PSYC 220', False) in group.courses
        assert ('PSYC 224', False) in group.courses
        assert ('PSYC 230', False) in group.courses
        assert ('PSYC 248', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 7
        
        assert ('PSYC 201', False) in group.courses
        assert ('PSYC 216', False) in group.courses
        assert ('PSYC 238', False) in group.courses
        assert ('PSYC 238', False) in group.courses
        assert ('PSYC 239', False) in group.courses
        assert ('PSYC 245', False) in group.courses
        assert ('PSYC 250', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test third group
        group = group_list[2]

        assert group.goal_type == 'C'
        assert group.goal_num == 2

        assert len(group.courses) == 76
        
        assert ('PSYC 301', False) in group.courses
        assert ('PSYC 302', False) in group.courses
        assert ('PSYC 306', False) in group.courses
        assert ('PSYC 308', False) in group.courses
        assert ('PSYC 311', False) in group.courses
        assert ('PSYC 312', False) in group.courses
        assert ('PSYC 314', False) in group.courses
        assert ('PSYC 318', False) in group.courses
        assert ('PSYC 320', False) in group.courses
        assert ('PSYC 321', False) in group.courses
        assert ('PSYC 322', False) in group.courses
        assert ('PSYC 324', False) in group.courses
        assert ('PSYC 326', False) in group.courses
        assert ('PSYC 327', False) in group.courses
        assert ('PSYC 328', False) in group.courses
        assert ('PSYC 329', False) in group.courses
        assert ('PSYC 331', False) in group.courses
        assert ('PSYC 332', False) in group.courses
        assert ('PSYC 333', False) in group.courses
        assert ('PSYC 334', False) in group.courses
        assert ('PSYC 336', False) in group.courses
        assert ('PSYC 340', False) in group.courses
        assert ('PSYC 341', False) in group.courses
        assert ('PSYC 350', False) in group.courses
        assert ('PSYC 351', False) in group.courses
        assert ('PSYC 352', False) in group.courses
        assert ('PSYC 353', False) in group.courses
        assert ('PSYC 358', False) in group.courses
        assert ('PSYC 361', False) in group.courses
        assert ('PSYC 363', False) in group.courses
        assert ('PSYC 365', False) in group.courses
        assert ('PSYC 373', False) in group.courses
        assert ('PSYC 379', False) in group.courses
        assert ('PSYC 383', False) in group.courses
        assert ('PSYC 385', False) in group.courses
        assert ('PSYC 396', False) in group.courses
        assert ('PSYC 398', False) in group.courses
        assert ('PSYC 402', False) in group.courses
        assert ('PSYC 403', False) in group.courses
        assert ('PSYC 404', False) in group.courses
        assert ('PSYC 408', False) in group.courses
        assert ('PSYC 410', False) in group.courses
        assert ('PSYC 413', False) in group.courses
        assert ('PSYC 414', False) in group.courses
        assert ('PSYC 416', False) in group.courses
        assert ('PSYC 417', False) in group.courses
        assert ('PSYC 420', False) in group.courses
        assert ('PSYC 421', False) in group.courses
        assert ('PSYC 423', False) in group.courses
        assert ('PSYC 425', False) in group.courses
        assert ('PSYC 427', False) in group.courses
        assert ('PSYC 432', False) in group.courses
        assert ('PSYC 433', False) in group.courses
        assert ('PSYC 437', False) in group.courses
        assert ('PSYC 443', False) in group.courses
        assert ('PSYC 445', False) in group.courses
        assert ('PSYC 447', False) in group.courses
        assert ('PSYC 450', False) in group.courses
        assert ('PSYC 451', False) in group.courses
        assert ('PSYC 453', False) in group.courses
        assert ('PSYC 455', False) in group.courses
        assert ('PSYC 456', False) in group.courses
        assert ('PSYC 462', False) in group.courses
        assert ('PSYC 465', False) in group.courses
        assert ('PSYC 468', False) in group.courses
        assert ('PSYC 472', False) in group.courses
        assert ('PSYC 475', False) in group.courses
        assert ('PSYC 477', False) in group.courses
        assert ('PSYC 489', False) in group.courses
        assert ('PSYC 490', False) in group.courses
        assert ('PSYC 492', False) in group.courses
        assert ('PSYC 494', False) in group.courses
        assert ('PSYC 495', False) in group.courses
        assert ('PSYC 496', False) in group.courses
        assert ('PSYC 498', False) in group.courses
        assert ('PSYC 499', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestPsychology.minor.required_courses

        # test length of the list
        assert len(courses) == 2

        assert [('PSYC 100', False), ('PSYC 235', False)] == courses

    def test_repl_courses(self):
        courses = TestPsychology.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestPsychology.minor.name
        credit = TestPsychology.minor.total_credits

        assert name == 'Psychology'.upper()
        assert credit == 18

class TestPublicRelations:
    minor = minors[63]

    def test_required_groups(self):
        group_list = TestPublicRelations.minor.required_groups

        assert len(group_list) == 2

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 3

        assert ('ADV 350', False) in group.courses
        assert ('JOUR 210', False) in group.courses
        assert ('CMN 220', False) in group.courses
                
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'C'
        assert group.goal_num == 2

        assert len(group.courses) == 9
        
        assert ('ADV 393', False) in group.courses
        assert ('ADV 490', False) in group.courses
        assert ('ADV 494', False) in group.courses
        assert ('JOUR 360', False) in group.courses
        assert ('JOUR 453', False) in group.courses
        assert ('JOUR 460', False) in group.courses
        assert ('CMN 321', False) in group.courses
        assert ('CMN 377', False) in group.courses
        assert ('CMN 464', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestPublicRelations.minor.required_courses

        # test length of the list
        assert len(courses) == 3

        assert [('JOUR 200', False), ('ADV 310', False), ('ADV 410', False)] == courses

    def test_repl_courses(self):
        courses = TestPublicRelations.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestPublicRelations.minor.name
        credit = TestPublicRelations.minor.total_credits

        assert name == 'Public Relations'.upper()
        assert credit == 18

class TestScandinavianStudies:
    minor = minors[64]

    def test_required_groups(self):
        group_list = TestScandinavianStudies.minor.required_groups

        assert len(group_list) == 2

        # test first group
        group = group_list[0]

        assert group.goal_type == 'H'
        assert group.goal_num == 6

        assert len(group.courses) == 10

        assert ('SCAN 305', False) in group.courses
        assert ('SCAN 306', False) in group.courses
        assert ('SCAN 376', False) in group.courses
        assert ('SCAN 463', False) in group.courses
        assert ('SCAN 470', False) in group.courses
        assert ('SCAN 472', False) in group.courses
        assert ('SCAN 490', False) in group.courses
        assert ('SCAN 492', False) in group.courses
        assert ('SCAN 494', False) in group.courses
        assert ('SCAN 496', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'H'
        assert group.goal_num == 18

        assert len(group.courses) == 16
        
        assert ('SCAN 103', False) in group.courses
        assert ('SCAN 104', False) in group.courses
        assert ('SCAN 215', False) in group.courses
        assert ('SCAN 225', False) in group.courses
        assert ('SCAN 251', False) in group.courses
        assert ('SCAN 252', False) in group.courses
        assert ('SCAN 305', False) in group.courses
        assert ('SCAN 306', False) in group.courses
        assert ('SCAN 376', False) in group.courses
        assert ('SCAN 463', False) in group.courses
        assert ('SCAN 470', False) in group.courses
        assert ('SCAN 472', False) in group.courses
        assert ('SCAN 490', False) in group.courses
        assert ('SCAN 492', False) in group.courses
        assert ('SCAN 494', False) in group.courses
        assert ('SCAN 496', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestScandinavianStudies.minor.required_courses

        # test length of the list
        assert len(courses) == 1

        assert [('SCAN 102', False)] == courses

    def test_repl_courses(self):
        courses = TestScandinavianStudies.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestScandinavianStudies.minor.name
        credit = TestScandinavianStudies.minor.total_credits

        assert name == 'Scandinavian Studies'.upper()
        assert credit == 18

class TestSocialWork:
    minor = minors[65]

    def test_required_groups(self):
        group_list = TestSocialWork.minor.required_groups

        assert len(group_list) == 1

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 2

        assert len(group.courses) == 17

        assert ('SOCW 240', False) in group.courses
        assert ('SOCW 297', False) in group.courses
        assert ('SOCW 310', False) in group.courses
        assert ('SOCW 315', False) in group.courses
        assert ('SOCW 321', False) in group.courses
        assert ('SOCW 330', False) in group.courses
        assert ('SOCW 360', False) in group.courses
        assert ('SOCW 370', False) in group.courses
        assert ('SOCW 380', False) in group.courses
        assert ('SOCW 412', False) in group.courses
        assert ('SOCW 416', False) in group.courses
        assert ('SOCW 418', False) in group.courses
        assert ('SOCW 420', False) in group.courses
        assert ('SOCW 436', False) in group.courses
        assert ('SOCW 455', False) in group.courses
        assert ('SOCW 475', False) in group.courses
        assert ('SOCW 480', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestSocialWork.minor.required_courses

        # test length of the list
        assert len(courses) == 4

        assert [('SOCW 200', False), ('SOCW 300', False), ('SOCW 410', False), ('SOCW 451', False)] == courses

    def test_repl_courses(self):
        courses = TestSocialWork.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestSocialWork.minor.name
        credit = TestSocialWork.minor.total_credits

        assert name == 'Social Work'.upper()
        assert credit == 18

class TestSpatialAndQuantitativeMethodsInNaturalResourcesAndEnvironmentalSciences:
    minor = minors[66]

    def test_required_groups(self):
        group_list = TestSpatialAndQuantitativeMethodsInNaturalResourcesAndEnvironmentalSciences.minor.required_groups

        assert len(group_list) == 4

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 6

        assert ('NRES 340', False) in group.courses
        assert ('NRES 421', False) in group.courses
        assert ('CPSC 440', False) in group.courses
        assert ('NRES 445', False) in group.courses
        assert ('SOC 485', False) in group.courses
        assert ('STAT 200', False) in group.courses

        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 4
        
        assert ('NRES 422', False) in group.courses
        assert ('NRES 427', False) in group.courses
        assert ('ANSC 448', False) in group.courses
        assert ('GEOG 468', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test third group
        group = group_list[2]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 6
        
        assert ('NRES 454', False) in group.courses
        assert ('NRES 455', False) in group.courses
        assert ('NRES 465', False) in group.courses
        assert ('GEOG 478', False) in group.courses
        assert ('GEOG 479', False) in group.courses
        assert ('GEOG 489', False) in group.courses


        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test fourth group
        group = group_list[3]

        assert group.goal_type == 'H'
        assert group.goal_num == 18

        assert len(group.courses) == 16
        
        assert ('NRES 340', False) in group.courses
        assert ('NRES 421', False) in group.courses
        assert ('CPSC 440', False) in group.courses
        assert ('NRES 445', False) in group.courses
        assert ('SOC 485', False) in group.courses
        assert ('STAT 200', False) in group.courses
        assert ('NRES 422', False) in group.courses
        assert ('NRES 427', False) in group.courses
        assert ('ANSC 448', False) in group.courses
        assert ('GEOG 468', False) in group.courses
        assert ('NRES 454', False) in group.courses
        assert ('NRES 455', False) in group.courses
        assert ('NRES 465', False) in group.courses
        assert ('GEOG 478', False) in group.courses
        assert ('GEOG 479', False) in group.courses
        assert ('GEOG 489', False) in group.courses


        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestSpatialAndQuantitativeMethodsInNaturalResourcesAndEnvironmentalSciences.minor.required_courses

        # test length of the list
        assert len(courses) == 0

    def test_repl_courses(self):
        courses = TestSpatialAndQuantitativeMethodsInNaturalResourcesAndEnvironmentalSciences.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestSpatialAndQuantitativeMethodsInNaturalResourcesAndEnvironmentalSciences.minor.name
        credit = TestSpatialAndQuantitativeMethodsInNaturalResourcesAndEnvironmentalSciences.minor.total_credits

        assert name == 'Spatial & Quantitative Methods in Natural Resources & Environmental Sciences'.upper()
        assert credit == 18

class TestSpeechAndHearingScience:
    minor = minors[67]

    def test_required_groups(self):
        group_list = TestSpeechAndHearingScience.minor.required_groups

        assert len(group_list) == 3

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 2

        assert len(group.courses) == 5

        assert ('SHS 222', False) in group.courses
        assert ('SHS 240', False) in group.courses
        assert ('SHS 300', False) in group.courses
        assert ('SHS 320', False) in group.courses
        assert ('SHS 352', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'H'
        assert group.goal_num == 8

        assert len(group.courses) == 13
        
        assert ('SHS 120', False) in group.courses
        assert ('SHS 200', False) in group.courses
        assert ('SHS 271', False) in group.courses
        assert ('SHS 280', False) in group.courses
        assert ('SHS 301', False) in group.courses
        assert ('SHS 333', False) in group.courses
        assert ('SHS 375', False) in group.courses
        assert ('SHS 380', False) in group.courses
        assert ('SHS 389', False) in group.courses
        assert ('SHS 427', False) in group.courses
        assert ('SHS 450', False) in group.courses
        assert ('SHS 451', False) in group.courses
        assert ('SHS 473', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test third group
        group = group_list[2]

        assert group.goal_type == 'H'
        assert group.goal_num == 6

        assert len(group.courses) == 9
        
        assert ('SHS 301', False) in group.courses
        assert ('SHS 333', False) in group.courses
        assert ('SHS 375', False) in group.courses
        assert ('SHS 380', False) in group.courses
        assert ('SHS 389', False) in group.courses
        assert ('SHS 427', False) in group.courses
        assert ('SHS 450', False) in group.courses
        assert ('SHS 451', False) in group.courses
        assert ('SHS 473', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestSpeechAndHearingScience.minor.required_courses

        # test length of the list
        assert len(courses) == 1

        assert [('SHS 170', False)] == courses

    def test_repl_courses(self):
        courses = TestSpeechAndHearingScience.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestSpeechAndHearingScience.minor.name
        credit = TestSpeechAndHearingScience.minor.total_credits

        assert name == 'Speech & Hearing Science'.upper()
        assert credit == 17

class TestTeacherEducationMinorInEnglishAsASecondLanguage:
    minor = minors[68]

    def test_required_groups(self):
        group_list = TestTeacherEducationMinorInEnglishAsASecondLanguage.minor.required_groups

        assert len(group_list) == 2

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 2

        assert ('EIL 214', False) in group.courses
        assert ('EIL 215', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 2
        
        assert ('EIL 456', False) in group.courses
        assert ('CI 446', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestTeacherEducationMinorInEnglishAsASecondLanguage.minor.required_courses

        # test length of the list
        assert len(courses) == 6

        assert [('EIL 422', False), ('EIL 411', False), ('EIL 460', False), ('EIL 488', False), ('LING 489', False), ('LING 100', False)] == courses

    def test_repl_courses(self):
        courses = TestTeacherEducationMinorInEnglishAsASecondLanguage.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestTeacherEducationMinorInEnglishAsASecondLanguage.minor.name
        credit = TestTeacherEducationMinorInEnglishAsASecondLanguage.minor.total_credits

        assert name == 'Teacher Education Minor in English as a Second Language'.upper()
        assert credit == 23

class TestTeacherEducationMinorInSecondarySchoolTeaching:
    minor = minors[69]

    def test_required_groups(self):
        group_list = TestTeacherEducationMinorInSecondarySchoolTeaching.minor.required_groups

        assert len(group_list) == 0

    def test_required_courses(self):
        courses = TestTeacherEducationMinorInSecondarySchoolTeaching.minor.required_courses

        # test length of the list
        assert len(courses) == 10

        assert [('EDUC 201', False), ('EDUC 202', False), ('CI 401', False), ('CI 403', False), ('CI 404', False), ('CI 473', False), 
        ('EPSY 201', False), ('EPSY 485', False), ('SPED 405', False), ('EDPR 442', False)] == courses

    def test_repl_courses(self):
        courses = TestTeacherEducationMinorInSecondarySchoolTeaching.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestTeacherEducationMinorInSecondarySchoolTeaching.minor.name
        credit = TestTeacherEducationMinorInSecondarySchoolTeaching.minor.total_credits

        assert name == 'Teacher Education Minor in Secondary School Teaching'.upper()
        assert credit == 39

class TestTechnicalSystemsManagement:
    minor = minors[70]

    def test_required_groups(self):
        group_list = TestTechnicalSystemsManagement.minor.required_groups

        assert len(group_list) == 2

        # test first group
        group = group_list[0]

        assert group.goal_type == 'H'
        assert group.goal_num == 6

        assert len(group.courses) == 4

        assert ('TSM 435', False) in group.courses
        assert ('TSM 464', False) in group.courses
        assert ('TSM 465', False) in group.courses
        assert ('TSM 496', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'H'
        assert group.goal_num == 15

        assert len(group.courses) == 13
        
        assert ('TSM 232', False) in group.courses
        assert ('TSM 233', False) in group.courses
        assert ('TSM 234', False) in group.courses
        assert ('TSM 262', False) in group.courses
        assert ('TSM 352', False) in group.courses
        assert ('TSM 363', False) in group.courses
        assert ('TSM 371', False) in group.courses
        assert ('TSM 372', False) in group.courses
        assert ('TSM 381', False) in group.courses
        assert ('TSM 435', False) in group.courses
        assert ('TSM 464', False) in group.courses
        assert ('TSM 465', False) in group.courses
        assert ('TSM 496', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestTechnicalSystemsManagement.minor.required_courses

        # test length of the list
        assert len(courses) == 1

        assert [('TSM 100', False)] == courses

    def test_repl_courses(self):
        courses = TestTechnicalSystemsManagement.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestTechnicalSystemsManagement.minor.name
        credit = TestTechnicalSystemsManagement.minor.total_credits

        assert name == 'Technical Systems Management'.upper()
        assert credit == 18

class TestTheatre:
    minor = minors[71]

    def test_required_groups(self):
        group_list = TestTheatre.minor.required_groups

        assert len(group_list) == 4

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 2

        assert ('THEA 304', False) in group.courses
        assert ('THEA 364', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 18
        
        assert ('THEA 110', False) in group.courses
        assert ('THEA 210', False) in group.courses
        assert ('THEA 211', False) in group.courses
        assert ('THEA 218', False) in group.courses
        assert ('THEA 260', False) in group.courses
        assert ('THEA 263', False) in group.courses
        assert ('THEA 304', False) in group.courses
        assert ('THEA 323', False) in group.courses
        assert ('THEA 362', False) in group.courses
        assert ('THEA 364', False) in group.courses
        assert ('THEA 410', False) in group.courses
        assert ('THEA 411', False) in group.courses
        assert ('THEA 417', False) in group.courses
        assert ('THEA 418', False) in group.courses
        assert ('THEA 463', False) in group.courses
        assert ('THEA 464', False) in group.courses
        assert ('THEA 467', False) in group.courses
        assert ('THEA 483', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test third group
        group = group_list[2]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 14
        
        assert ('THEA 100', False) in group.courses
        assert ('THEA 126', False) in group.courses
        assert ('THEA 153', False) in group.courses
        assert ('THEA 170', False) in group.courses
        assert ('THEA 175', False) in group.courses
        assert ('THEA 220', False) in group.courses
        assert ('THEA 222', False) in group.courses
        assert ('THEA 231', False) in group.courses
        assert ('THEA 270', False) in group.courses
        assert ('THEA 407', False) in group.courses
        assert ('THEA 418', False) in group.courses
        assert ('THEA 433', False) in group.courses
        assert ('THEA 452', False) in group.courses
        assert ('THEA 456', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test fourth group
        group = group_list[3]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 17
        
        assert ('THEA 304', False) in group.courses
        assert ('THEA 323', False) in group.courses
        assert ('THEA 362', False) in group.courses
        assert ('THEA 364', False) in group.courses
        assert ('THEA 410', False) in group.courses
        assert ('THEA 411', False) in group.courses
        assert ('THEA 417', False) in group.courses
        assert ('THEA 418', False) in group.courses
        assert ('THEA 463', False) in group.courses
        assert ('THEA 464', False) in group.courses
        assert ('THEA 467', False) in group.courses
        assert ('THEA 483', False) in group.courses
        assert ('THEA 407', False) in group.courses
        assert ('THEA 418', False) in group.courses
        assert ('THEA 433', False) in group.courses
        assert ('THEA 452', False) in group.courses
        assert ('THEA 456', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestTheatre.minor.required_courses

        # test length of the list
        assert len(courses) == 3

        assert [('THEA 100', False), ('THEA 101', False), ('THEA 208', False)] == courses

    def test_repl_courses(self):
        courses = TestTheatre.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestTheatre.minor.name
        credit = TestTheatre.minor.total_credits

        assert name == 'Theatre'.upper()
        assert credit == 16

class TestTurkishStudies:
    minor = minors[72]

    def test_required_groups(self):
        group_list = TestTurkishStudies.minor.required_groups

        assert len(group_list) == 1

        # test first group
        group = group_list[0]

        assert group.goal_type == 'H'
        assert group.goal_num == 9

        assert len(group.courses) == 23

        assert ('ANTH 402', False) in group.courses
        assert ('ANTH 488', False) in group.courses
        assert ('EURO 415', False) in group.courses
        assert ('HIST 135', False) in group.courses
        assert ('HIST 335', False) in group.courses
        assert ('HIST 337', False) in group.courses
        assert ('HIST 356', False) in group.courses
        assert ('HIST 396', False) in group.courses
        assert ('HIST 439', False) in group.courses
        assert ('HIST 466', False) in group.courses
        assert ('FR 418', False) in group.courses
        assert ('MUS 418', False) in group.courses
        assert ('PS 152', False) in group.courses
        assert ('PS 347', False) in group.courses
        assert ('REL 213', True) in group.courses
        assert ('REL 223', False) in group.courses
        assert ('REL 403', False) in group.courses
        assert ('REL 408', False) in group.courses
        assert ('REL 480', False) in group.courses
        assert ('REL 482', False) in group.courses
        assert ('REES 201', False) in group.courses
        assert ('SOC 483', False) in group.courses
        assert ('TURK 490', False) in group.courses
        
        assert len(group.repl_courses) == 1

        assert [('REL 213', 'REL 214')] == group.repl_courses

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestTurkishStudies.minor.required_courses

        # test length of the list
        assert len(courses) == 3

        assert [('TURK 405', False), ('TURK 406', False), ('TURK 270', False)] == courses

    def test_repl_courses(self):
        courses = TestTurkishStudies.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestTurkishStudies.minor.name
        credit = TestTurkishStudies.minor.total_credits

        assert name == 'Turkish Studies'.upper()
        assert credit == 18

class TestUrbanStudiesAndPlanning:
    minor = minors[73]

    def test_required_groups(self):
        group_list = TestUrbanStudiesAndPlanning.minor.required_groups

        assert len(group_list) == 3

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 1

        assert len(group.courses) == 2

        assert ('UP 203', False) in group.courses
        assert ('UP 204', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test second group
        group = group_list[1]

        assert group.goal_type == 'H'
        assert group.goal_num == 14

        assert len(group.courses) == 88
        
        assert ('UP 101', False) in group.courses
        assert ('UP 116', False) in group.courses
        assert ('UP 136', False) in group.courses
        assert ('UP 160', False) in group.courses
        assert ('UP 185', False) in group.courses
        assert ('UP 199', False) in group.courses
        assert ('UP 201', False) in group.courses
        assert ('UP 203', False) in group.courses
        assert ('UP 204', False) in group.courses
        assert ('UP 205', False) in group.courses
        assert ('UP 210', False) in group.courses
        assert ('UP 211', False) in group.courses
        assert ('UP 260', False) in group.courses
        assert ('UP 301', False) in group.courses
        assert ('UP 312', False) in group.courses
        assert ('UP 316', False) in group.courses
        assert ('UP 330', False) in group.courses
        assert ('UP 335', False) in group.courses
        assert ('UP 340', False) in group.courses
        assert ('UP 345', False) in group.courses
        assert ('UP 347', False) in group.courses
        assert ('UP 357', False) in group.courses
        assert ('UP 390', False) in group.courses
        assert ('UP 397', False) in group.courses
        assert ('UP 401', False) in group.courses
        assert ('UP 405', False) in group.courses
        assert ('UP 406', False) in group.courses
        assert ('UP 407', False) in group.courses
        assert ('UP 418', False) in group.courses
        assert ('UP 420', False) in group.courses
        assert ('UP 423', False) in group.courses
        assert ('UP 426', False) in group.courses
        assert ('UP 428', False) in group.courses
        assert ('UP 430', False) in group.courses
        assert ('UP 436', False) in group.courses
        assert ('UP 438', False) in group.courses
        assert ('UP 441', False) in group.courses
        assert ('UP 443', False) in group.courses
        assert ('UP 446', False) in group.courses
        assert ('UP 447', False) in group.courses
        assert ('UP 455', False) in group.courses
        assert ('UP 456', False) in group.courses
        assert ('UP 457', False) in group.courses
        assert ('UP 460', False) in group.courses
        assert ('UP 466', False) in group.courses
        assert ('UP 470', False) in group.courses
        assert ('UP 473', False) in group.courses
        assert ('UP 474', False) in group.courses
        assert ('UP 475', False) in group.courses
        assert ('UP 478', False) in group.courses
        assert ('UP 479', False) in group.courses
        assert ('UP 480', False) in group.courses
        assert ('UP 481', False) in group.courses
        assert ('UP 494', False) in group.courses
        assert ('UP 501', False) in group.courses
        assert ('UP 503', False) in group.courses
        assert ('UP 504', False) in group.courses
        assert ('UP 505', False) in group.courses
        assert ('UP 508', False) in group.courses
        assert ('UP 509', False) in group.courses
        assert ('UP 510', False) in group.courses
        assert ('UP 511', False) in group.courses
        assert ('UP 512', False) in group.courses
        assert ('UP 513', False) in group.courses
        assert ('UP 519', False) in group.courses
        assert ('UP 521', False) in group.courses
        assert ('UP 533', False) in group.courses
        assert ('UP 535', False) in group.courses
        assert ('UP 543', False) in group.courses
        assert ('UP 545', False) in group.courses
        assert ('UP 546', False) in group.courses
        assert ('UP 547', False) in group.courses
        assert ('UP 552', False) in group.courses
        assert ('UP 555', False) in group.courses
        assert ('UP 576', False) in group.courses
        assert ('UP 578', False) in group.courses
        assert ('UP 580', False) in group.courses
        assert ('UP 585', False) in group.courses
        assert ('UP 587', False) in group.courses
        assert ('UP 589', False) in group.courses
        assert ('UP 590', False) in group.courses
        assert ('UP 591', False) in group.courses
        assert ('UP 592', False) in group.courses
        assert ('UP 594', False) in group.courses
        assert ('UP 596', False) in group.courses
        assert ('UP 597', False) in group.courses
        assert ('UP 598', False) in group.courses
        assert ('UP 599', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

        # test third group
        group = group_list[2]

        assert group.goal_type == 'H'
        assert group.goal_num == 6

        assert len(group.courses) == 41
        
        assert ('UP 301', False) in group.courses
        assert ('UP 312', False) in group.courses
        assert ('UP 316', False) in group.courses
        assert ('UP 330', False) in group.courses
        assert ('UP 335', False) in group.courses
        assert ('UP 340', False) in group.courses
        assert ('UP 345', False) in group.courses
        assert ('UP 347', False) in group.courses
        assert ('UP 357', False) in group.courses
        assert ('UP 390', False) in group.courses
        assert ('UP 397', False) in group.courses
        assert ('UP 401', False) in group.courses
        assert ('UP 405', False) in group.courses
        assert ('UP 406', False) in group.courses
        assert ('UP 407', False) in group.courses
        assert ('UP 418', False) in group.courses
        assert ('UP 420', False) in group.courses
        assert ('UP 423', False) in group.courses
        assert ('UP 426', False) in group.courses
        assert ('UP 428', False) in group.courses
        assert ('UP 430', False) in group.courses
        assert ('UP 436', False) in group.courses
        assert ('UP 438', False) in group.courses
        assert ('UP 441', False) in group.courses
        assert ('UP 443', False) in group.courses
        assert ('UP 446', False) in group.courses
        assert ('UP 447', False) in group.courses
        assert ('UP 455', False) in group.courses
        assert ('UP 456', False) in group.courses
        assert ('UP 457', False) in group.courses
        assert ('UP 460', False) in group.courses
        assert ('UP 466', False) in group.courses
        assert ('UP 470', False) in group.courses
        assert ('UP 473', False) in group.courses
        assert ('UP 474', False) in group.courses
        assert ('UP 475', False) in group.courses
        assert ('UP 478', False) in group.courses
        assert ('UP 479', False) in group.courses
        assert ('UP 480', False) in group.courses
        assert ('UP 481', False) in group.courses
        assert ('UP 494', False) in group.courses

        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestUrbanStudiesAndPlanning.minor.required_courses

        # test length of the list
        assert len(courses) == 1

        assert [('UP 101', False)] == courses

    def test_repl_courses(self):
        courses = TestUrbanStudiesAndPlanning.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestUrbanStudiesAndPlanning.minor.name
        credit = TestUrbanStudiesAndPlanning.minor.total_credits

        assert name == 'Urban Studies & Planning'.upper()
        assert credit == 20

class TestWorldLiteratureEuropeAndAmericasTrack:
    minor = minors[74]

    def test_required_groups(self):
        group_list = TestWorldLiteratureEuropeAndAmericasTrack.minor.required_groups

        assert len(group_list) == 1

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 2

        assert len(group.courses) == 5

        assert ('CWL 395', False) in group.courses
        assert ('CWL 441', False) in group.courses
        assert ('CWL 461', False) in group.courses
        assert ('CWL 471', False) in group.courses
        assert ('CWL 496', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestWorldLiteratureEuropeAndAmericasTrack.minor.required_courses

        # test length of the list
        assert len(courses) == 4

        assert [('CWL 241', False), ('CWL 242', False), ('CWL 201', False), ('CWL 202', False)] == courses

    def test_repl_courses(self):
        courses = TestWorldLiteratureEuropeAndAmericasTrack.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestWorldLiteratureEuropeAndAmericasTrack.minor.name
        credit = TestWorldLiteratureEuropeAndAmericasTrack.minor.total_credits

        assert name == 'World Literature, Europe & Americas Track'.upper()
        assert credit == 18

class TestWorldLiteratureAsiaAndAfricaTrack:
    minor = minors[75]

    def test_required_groups(self):
        group_list = TestWorldLiteratureAsiaAndAfricaTrack.minor.required_groups

        assert len(group_list) == 1

        # test first group
        group = group_list[0]

        assert group.goal_type == 'C'
        assert group.goal_num == 2

        assert len(group.courses) == 5

        assert ('CWL 395', False) in group.courses
        assert ('CWL 441', False) in group.courses
        assert ('CWL 461', False) in group.courses
        assert ('CWL 471', False) in group.courses
        assert ('CWL 496', False) in group.courses
        
        assert len(group.repl_courses) == 0

        assert len(group.unallowed_courses) == 0

    def test_required_courses(self):
        courses = TestWorldLiteratureAsiaAndAfricaTrack.minor.required_courses

        # test length of the list
        assert len(courses) == 4

        assert [('CWL 189', False), ('CWL 190', False), ('CWL 201', False), ('CWL 202', False)] == courses

    def test_repl_courses(self):
        courses = TestWorldLiteratureAsiaAndAfricaTrack.minor.repl_courses

        # no replacement courses for required courses
        assert len(courses) == 0

    def test_minor(self):
        name = TestWorldLiteratureAsiaAndAfricaTrack.minor.name
        credit = TestWorldLiteratureAsiaAndAfricaTrack.minor.total_credits

        assert name == 'World Literature, Asia & Africa Track'.upper()
        assert credit == 18

