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

    intersection = get_group_intersection(mnr.get_courses(), get_courses_only(list_of_courses))
    course_goal_num = len (intersection)

    #TODO: Check for weird edge cases
    if len(mnr.repl_courses) > 0:
        for repl_tuple in mnr.repl_courses:
            matched_courses = get_group_intersection(list(repl_tuple), get_courses_only(list_of_courses))
            intersection.extend(matched_courses)
            intersection = list(set(intersection))
            course_goal_num = len (intersection)

    return course_goal_num / num_required_courses, intersection


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

def check_C_type_group(grp, list_of_courses):
    #TODO: Add a utility method to group class that gets all courses from the tuples since grp.courses is a list of tuples 
    course_goal_num = len (get_group_intersection(grp.courses, list_of_courses))

    if course_goal_num >= grp.goal_num:
        return True
    # Verify no weird edge cases with this
    elif len(grp.repl_courses) > 0:
        for repl_tuple in grp.repl_courses:
            if len (get_group_intersection(list(repl_tuple), list_of_courses)):
                course_goal_num+=1
    
def check_H_type_group(grp, list_of_courses):
    return True

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

test_courses = [
    ('CS 225', 4.0),
    ('MATH 213', 4.0),
    ('ECE 220', 4.0),
    ('KIN 249', 4.0)
]

print (check_required_courses(minors[10], test_courses))
print (minors[10].required_courses)
# check_required_courses(minors[10], test_courses)