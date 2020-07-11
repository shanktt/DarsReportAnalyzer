from group import group
from minor import minor
from minor_parser import create_pd, create_minors
from parser import get_courses_only

# This should be the process in which a students progress for minors are handled
# 1. Take the student's list of courses from that is obtained from parser.py 
# 2. For each minor created from minor_parser.py identify 1-3 departments that comprise the majority of the minors required courses and group.
#    This might belong within minor_parser.py and as a parameter within a minor object in minor.py. Another alternative is to have a method within
#    minor.py that is called in the objects constructor and completes this functionality
# 3. Take this reduced list of minors and begin comparing them against the student's list of classes
#   3.1. First check the required courses against the student's courses
#   3.2. Then begin to check each group (Seperate functions for C type group and H type group)
#   Note:   When checking the list of required courses and the groups return two things from these functions.
#           First return value should be a float which represents the amount of courses a student has fulfilled for the minor's required courses or group.
#           For example if a minor's required courses is comprised of 'CS 125, CS 173, CS 225' and a student has completed classes 'CS 125, CS 173' then the function 
#           Should return 0.66666666666. The second return value should be a list of the courses that the student has completed. In this case that would be 'CS 125, CS 173'.
#           Returning a float will allow us to display to a student the percentage of a group/required courses they have completed. The list of classes that they have completed
#           will help in the visualization portion of the website
#   Note about repl courses:    One way in which repl courses can be checked is first find the size of the intersection between a list of courses from a group and a student's
#                               list of completed courses. The size of this intersection can be stored as a student's 'total completed amount' for a group. 
#                               If the size of this 'total completed amount' is less than the amount required to complete the group, then check to see if the
#                               courses within the group contains any repl courses. This can be determined by seeing if any of the tuples in the group's list of courses have
#                               there second parameter as true. If this is the case than the program should check the intersection of the student's completed courses against
#                               the list of repl courses (need to guard against edge cases that can easily arise in this). Add this intersection amount to the student's previous
#                               'total completed amount' and now proceed with returning the required values from the function. 
#                               The edge case that can arise from this is that say a group of type C with 3 required courses has the following courses within it:
#                               [('CS 125', True), ('CS 173', True), ('CS 225', False)] and 
#                               the student's list of courses contains ['CS 125']. The intersection of the two lists will be of size 1, while the required amount is 3 for
#                               this group. Once we proceed to


def check_required_courses(mnr : minor, list_of_courses):
    num_required_courses = len (mnr.required_courses)

    intersection = get_intersection(mnr.get_courses(), get_courses_only(list_of_courses))
    course_goal_num = len (intersection)

    #TODO: Check for weird edge cases
    if len(mnr.repl_courses) > 0:
        for repl_tuple in mnr.repl_courses:
            matched_courses = get_intersection(list(repl_tuple), get_courses_only(list_of_courses))
            intersection.extend(matched_courses)
            intersection = list(set(intersection))
            course_goal_num = len (intersection)

    return course_goal_num / num_required_courses, intersection


def check_groups(list_of_groups, list_of_courses):
    for grp in list_of_groups:
        print(grp)
    
def get_intersection(grp_courses, list_of_courses):
        # Returns the number of courses that exist in both lists 
        return list(set(grp_courses).intersection(list_of_courses))

def get_unique_courses_in_group(mnr : minor, grp : group):
    unique_group_courses = grp.get_courses()
    
    for i in range(len(mnr.required_groups)):
        if (grp == mnr.required_groups[i]):
            continue
        unique_group_courses = list(set(unique_group_courses) - set(mnr.required_groups[i].get_courses()))
    
    return unique_group_courses

# list_of_courses should be the original list of the student
# this is the list of tuples that has course strings and gpa floats in a tuples together
# we will be modifying said list in this method so the original must be passed
#TODO: Optimize this
def get_group_intersection_manual(grp : group, unique_grp_courses : list, list_of_student_courses : list, num_required_courses : int):
    intersection = []

    # If there are course unique to this group (ie these courses are not contained in any other groups)
    if (len(unique_grp_courses)):
        # Get the intersection between the student's courses and this list of unique courses
        intersection = get_intersection(unique_grp_courses, get_courses_only(list_of_student_courses))
        # If this intersection is larger than the number of courses actually required for this C type group we need to remove the extra courses
        if (len(intersection) > num_required_courses):
            intersection = intersection[:int(num_required_courses)]
            # Test this (Ideally this should change the list_of_student_courses variable passed into this method)
            list_of_student_courses[:] = [course_gpa_tuple for course_gpa_tuple in list_of_student_courses if course_gpa_tuple[0] not in intersection]
            return intersection
        elif (len(intersection) == num_required_courses):
            # Test this (Ideally this should change the list_of_student_courses variable passed into this method)
            list_of_student_courses[:] = [course_gpa_tuple for course_gpa_tuple in list_of_student_courses if course_gpa_tuple[0] not in intersection]
            return intersection
    

    #TODO: Need to check if the any of the courses in unique_grp_courses is a repl course before checking against the entirety of courses in the group
    unique_grp_courses_with_repls = get_intersection(unique_grp_courses, grp.get_repl_courses_as_flat_list())
    if (len(unique_grp_courses_with_repls)):
        repl_courses_as_dict = grp.convert_repl_courses_into_dict()
        for course_with_repl in unique_grp_courses_with_repls:
            possible_repls = repl_courses_as_dict[course_with_repl]
            intersection_with_repls = get_intersection(possible_repls, get_courses_only(list_of_student_courses))
            if (len(intersection_with_repls)):
                intersection.extend(intersection_with_repls)

    # Check entirety of courses within the group for any matches
    # If we reach this point and the size of the intersection is larger than 0, then we have repl courses within this intersection that need to be preserved, which is
    # what is happening below in the if statement
    if (len(intersection)):
        intersection.extend(get_intersection(grp.get_courses(), get_courses_only(list_of_student_courses)))
    else:
        intersection = get_intersection(grp.get_courses(), get_courses_only(list_of_student_courses))

    if (len(intersection) > num_required_courses):
        intersection = intersection[:int(num_required_courses)]
        list_of_student_courses[:] = [course_gpa_tuple for course_gpa_tuple in list_of_student_courses if course_gpa_tuple[0] not in intersection]
        return intersection
    elif (len(intersection) == num_required_courses):
        list_of_student_courses[:] = [course_gpa_tuple for course_gpa_tuple in list_of_student_courses if course_gpa_tuple[0] not in intersection]
        return intersection

    # Check repl courses
    if (len(grp.repl_courses)):
        for repl_tuple in grp.repl_courses:
            if (len(intersection) == num_required_courses):
                break
            # Test against case of student having CS 241 and ECE 391 credit
            matched_course = get_intersection(list(repl_tuple), get_courses_only(list_of_student_courses))

            if (len(get_intersection(matched_course, intersection))):
                continue
            else:
                intersection.extend(matched_course)

    list_of_student_courses[:] = [course_gpa_tuple for course_gpa_tuple in list_of_student_courses if course_gpa_tuple[0] not in intersection]

    return intersection

# list of courses: ('CS 123', 4.0)  grp: a group obj: (C/H, C/H amt., [courses_1,...,courses_n],[!courses],[repl])
# returns tuple: 'C', %completed, list of fulfilled courses
def check_C_type_group(grp : group, unique_grp_courses: list, student_courses_tuples : list):
    intersection = get_group_intersection_manual(grp, unique_grp_courses, student_courses_tuples, grp.goal_num)
    achieved_goal_num = len (intersection)

    return ['C', achieved_goal_num / grp.goal_num, intersection]


# returns tuple: 'H', %completed, list of fulfilled courses
def check_H_type_group(grp : group, list_of_courses : list):
    grp_courses = grp.get_courses()
    total_hrs = 0
    fulfilled_courses = []
    for course in list_of_courses:
        if str(course[0]) in grp_courses:
            total_hrs += course[1]
            fulfilled_courses.append(course[0])

    print(total_hrs)
    return 'H', min(total_hrs / grp.goal_num, 1), fulfilled_courses

def check_minors(list_of_minors, list_of_courses):
    for mnr in list_of_minors:
        check_groups(mnr.required_groups, list_of_courses)

#TODO: This method will take a students list of courses (from parser.py) and the entire list of minors (from minor_parser.py) and return a list of minors that are 'relevant' 
# to said student. Need to find set of 1-3 departments that comprise majority of the minor and see if the student has any courses in that department. 
def find_relevant_minor(list_of_courses, list_of_all_minors):
    return True


df = create_pd('minor_data.csv') 
minors = create_minors(df)
# check_minors(minors, 'test')
# print (minors[10])

# test_courses = [
#     ('CS 225', 4.0),
#     ('MATH 213', 4.0),
#     ('ECE 220', 4.0),
#     ('KIN 249', 4.0)
# ]

# print (check_required_courses(minors[10], test_courses))
# print (minors[10].required_courses)
# check_required_courses(minors[10], test_courses)
# Test this (Ideally this should change the list_of_student_courses variable passed into this method)
roes_courses = [
('MATH 241', 4.0),
('CS 100', 1.0),
('CS 101', 3.0),
('CS 125', 4.0),
('CS 126', 3.0),
('CS 173', 3.0),
('HIST 142', 3.0),
('JAPN 203', 5.0),
('JAPN 204', 5.0),
('JAPN 305', 5.0),
('JAPN 306', 5.0),
('LAS 101', 1.0),
('LING 111', 3.0),
('MATH 220', 5.0),
('MATH 231', 3.0),
('MATH 347', 3.0),
('PHYS 211', 4.0),
('PHYS 212', 4.0),
('PSYC 100', 4.0),
('RHET 105', 4.0),
('CS 225', 4.0),
# ('CS 233', 4.0),
('MATH 441', 3.0),
('STAT 200', 3.0),
('MATH 416', 3.0),
('MATH 461', 3.0),
# ('CS 241', 4.0),
('CS 450', 3.0),
('MATH 413', 3.0),
('MATH 453', 3.0),
('EURO 415', 3.0),
('FR 418', 3.0),
('CS 433', 3.0),
# Added for testing:
# ('CS 374', 4.0),
('ECE 391', 4.0)
]

# Make this a method
unique_group_courses_list = []
for i in range(len(minors[10].required_groups)):
    unique_group_courses = minors[10].required_groups[i].get_courses()
    for j in range(len(minors[10].required_groups)):
        if (minors[10].required_groups[i] == minors[10].required_groups[j]):
            continue
        unique_group_courses = list(set(unique_group_courses) - set(minors[10].required_groups[j].get_courses()))
    unique_group_courses_list.append(unique_group_courses)

# for l in unique_group_courses_list:
    # print (l)

# print (unique_group_courses_list[0])
# print()
# print ('intersection:')
# print (get_group_intersection_manual(unique_group_courses_list[0], minors[10].required_groups[0], roes_courses, minors[10].required_groups[0].goal_num))
# print()
# print (roes_courses)


print (check_C_type_group(minors[10].required_groups[0], unique_group_courses_list[0], roes_courses))
print (check_C_type_group(minors[10].required_groups[1], unique_group_courses_list[1], roes_courses))

# print (get_unique_courses_in_group(minors[10], minors[10].required_groups[0]))
# print (minors[10].required_groups[0].get_repl_courses_as_flat_list())

# test = minors[10].required_groups[0].convert_repl_courses_into_dict()
# print (test)

# print (test['CS 241'])