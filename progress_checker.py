from group import group
from minor import minor
from minor_parser import create_pd, create_minors
from dars_parser import get_courses_only

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

    intersection = get_group_intersection(mnr.get_courses(), get_courses_only(list_of_courses))
    course_goal_num = len (intersection)

    if course_goal_num >= num_required_courses:
        return course_goal_num / num_required_courses, intersection
    elif len(mnr.repl_courses) > 0:
        for repl_tuple in mnr.repl_courses:
            matched_courses = get_group_intersection(list(repl_tuple), list_of_courses)
            possible_double_counts = get_group_intersection(list(repl_tuple), intersection)
            if len (matched_courses) and possible_double_counts == 0:
                course_goal_num += 1
                intersection.append(matched_courses)

    return min(course_goal_num / num_required_courses, 1), intersection


def check_groups(list_of_groups, list_of_courses):
    for grp in list_of_groups:
        print(grp)

def get_group_intersection(grp_courses, list_of_courses):
        # Returns the number of courses that exist in both lists
        return list(set(grp_courses).intersection(list_of_courses))

def check_group(grp, list_of_courses):
    # Deal with a C type group
    if grp.goal_type == 'C':
        return check_C_type_group(grp, list_of_courses)

    # Deal with a H type group
    elif grp.goal_type == 'H':
        return check_H_type_group(grp, list_of_courses)

# list of courses: ('CS 123', 4.0)  grp: a group obj: (C/H, C/H amt., [courses_1,...,courses_n],[!courses],[repl])
# returns tuple: 'C', %completed, list of fulfilled courses
def check_C_type_group(grp : group, list_of_courses : list):
    intersection = get_group_intersection(grp.get_courses(), get_courses_only(list_of_courses))
    course_goal_num = len (intersection)

    if course_goal_num >= grp.goal_num:
        return 'C', min(course_goal_num / grp.goal_num, 1), intersection

    # Verify no weird edge cases with this
    elif len(grp.repl_courses) > 0:
        for repl_tuple in grp.repl_courses:
            matched_courses = get_group_intersection(list(repl_tuple), list_of_courses)
            if len (matched_courses):
                course_goal_num += 1
                intersection.append(matched_courses)
        return 'C', min(course_goal_num / grp.goal_num, 1), intersection

    return 'C', min(course_goal_num / grp.goal_num, 1), intersection


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

def check_total_credits_met(mnr : minor, list_of_courses):
    all_minor_courses = []

    # add all required courses
    for course in mnr.required_courses:
        all_minor_courses.append(course[0])

    # add all courses in each group
    for group in mnr.required_groups:
        for course in group.courses:
            all_minor_courses.append(course[0])

    # remove duplicates
    all_minor_courses = list(dict.fromkeys(all_minor_courses))

    fulfilled_amt = len(get_group_intersection(all_minor_courses, get_courses_only(list_of_courses)))

    return fulfilled_amt, min(fulfilled_amt / mnr.total_credits, 1)


#TODO: This method will take a students list of courses (from parser.py) and the entire list of minors (from minor_parser.py) and return a list of minors that are 'relevant'
# to said student. Need to find set of 1-3 departments that comprise majority of the minor and see if the student has any courses in that department.
def find_relevant_minor(list_of_courses, list_of_all_minors):
    return True

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
('CS 233', 4.0),
('MATH 441', 3.0),
('STAT 200', 3.0),
('MATH 416', 3.0),
('MATH 461', 3.0),
('CS 241', 4.0),
('CS 450', 3.0),
('MATH 413', 3.0),
('MATH 453', 3.0),
('EURO 415', 3.0),
('FR 418', 3.0)
]

df = create_pd('minor_data.csv')
minors = create_minors(df)
print(check_total_credits_met(minors[10], roes_courses))
# for m in minors:
#     print(m.name)

# csminor = minors[10]
# for g in csminor.required_groups:
#     print(g)

# print(check_C_type_group(minors[10].required_groups[0], roes_courses))
# print(check_H_type_group(minors[72].required_groups[0], roes_courses))




# driver class:

# -parse all minors from csv

# -filter out irrelevant minors (dars has no courses in common with these minors)

# -progress_checker:

#     -for each relevant minor

#         -check total credits met  (usually around 18 hrs.)

#         -check required courses  (returns float, list of fulfilled courses)

#         -for each group

#             -check if group fulfilled (returns float, list of fulfilled courses, type of group (c/h))

#     - anything else?


# -> for visualization, need:
#     -total percentage progress for top 5 ish minors completed (general overview)
#     -detailed display: for each group, display all courses and fulfilled courses, and percentages?
