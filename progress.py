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

    intersection = get_intersection(mnr.get_courses(), get_courses_only(list_of_courses))
    course_goal_num = len (intersection)

    #TODO: Check for weird edge cases
    if len(mnr.repl_courses) > 0:
        for repl_tuple in mnr.repl_courses:
            matched_courses = get_intersection(list(repl_tuple), get_courses_only(list_of_courses))
            intersection.extend(matched_courses)
            intersection = list(set(intersection))
            course_goal_num = len (intersection)

    return 'R', round(course_goal_num / num_required_courses * 100, 2), intersection

def get_hours_for_courses(list_of_courses, list_of_student_courses):
    dict_of_student_courses = dict (list_of_student_courses)
    hours = 0

    for course in list_of_courses:
        # num = dict_of_student_courses[course]
        num = dict_of_student_courses.get(course, 0)
        hours += num
    
    return hours

# This method should only be called when we have overcounted in get_H_group_intersection_manual
def get_combo_of_courses_for_hours_requirement(list_of_courses : list, list_of_student_courses : list, required_hours : int):
    dict_of_student_courses = dict (list_of_student_courses)
    courses_with_hours = []

    for course in list_of_courses:
        courses_with_hours.append((course, dict_of_student_courses.get(course, 0)))

    courses, hours = zip(*courses_with_hours)

    possible_hours_combos = list(subset_sum(hours, required_hours))

    min_list_size = 0 if len(possible_hours_combos) == 0 else len(min(possible_hours_combos, key=len))

    lists_of_min_size = [l for l in possible_hours_combos if len(l) == min_list_size]

    hours_with_min_sum = [] if len(lists_of_min_size) == 0 else min(lists_of_min_size, key=sum)

    # iterate through this list of hours and find courses with coressponding hour
    # test this
    final_course_list = []
    for hour in hours_with_min_sum:
        # ReWrite
        for course_hours_tuple in courses_with_hours:
            if (course_hours_tuple[1] == hour):
                final_course_list.append(course_hours_tuple[0])
                courses_with_hours.remove(course_hours_tuple)
                break
    
    return final_course_list


def subset_sum(numbers : list, target : int, partial=[], partial_sum=0):
    if partial_sum == target or (partial_sum <= (target/3)*4 and partial_sum > target):
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        yield from subset_sum(remaining, target, partial + [n], partial_sum + n)

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
def get_C_group_intersection_manual(grp : group, unique_grp_courses : list, list_of_student_courses : list, num_required_courses : int):
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
    

    # Need to check if the any of the courses in unique_grp_courses is a repl course before checking against the entirety of courses in the group
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

def get_H_group_intersection_manual(grp : group, unique_grp_courses : list, list_of_student_courses : list, required_hours : int):
    intersection = []

    # If there are course unique to this group (ie these courses are not contained in any other groups)
    if (len(unique_grp_courses)):
        # Get the intersection between the student's courses and this list of unique courses
        intersection = get_intersection(unique_grp_courses, get_courses_only(list_of_student_courses))
        # If the total hours for the courses in this intersection is larger than the required hours for this H type group we need to remove extra courses
        hours = get_hours_for_courses(intersection, list_of_student_courses)
        if (hours > required_hours):
            intersection = get_combo_of_courses_for_hours_requirement(intersection, list_of_student_courses, required_hours)
            # Test this (Ideally this should change the list_of_student_courses variable passed into this method)
            hours = get_hours_for_courses(intersection, list_of_student_courses)
            list_of_student_courses[:] = [course_gpa_tuple for course_gpa_tuple in list_of_student_courses if course_gpa_tuple[0] not in intersection]
            return intersection, hours
        elif (len(intersection) == required_hours):
            # Test this (Ideally this should change the list_of_student_courses variable passed into this method)
            hours = get_hours_for_courses(intersection, list_of_student_courses)
            list_of_student_courses[:] = [course_gpa_tuple for course_gpa_tuple in list_of_student_courses if course_gpa_tuple[0] not in intersection]
            return intersection, hours
    

    # Need to check if the any of the courses in unique_grp_courses is a repl course before checking against the entirety of courses in the group
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
        # Easy way to fix bug of duplicates appearing at this stage
        intersection = list(dict.fromkeys(intersection))
    else:
        intersection = get_intersection(grp.get_courses(), get_courses_only(list_of_student_courses))

    hours = get_hours_for_courses(intersection, list_of_student_courses)
    if (len(intersection) > required_hours):
        intersection = get_combo_of_courses_for_hours_requirement(intersection, list_of_student_courses, required_hours)
        hours = get_hours_for_courses(intersection, list_of_student_courses)
        list_of_student_courses[:] = [course_gpa_tuple for course_gpa_tuple in list_of_student_courses if course_gpa_tuple[0] not in intersection]
        return intersection, hours
    elif (len(intersection) == required_hours):
        hours = get_hours_for_courses(intersection, list_of_student_courses)
        list_of_student_courses[:] = [course_gpa_tuple for course_gpa_tuple in list_of_student_courses if course_gpa_tuple[0] not in intersection]
        return intersection, hours

    # Check repl courses
    overcount_flag = False
    if (len(grp.repl_courses)):
        for repl_tuple in grp.repl_courses:
            hours = get_hours_for_courses(intersection, list_of_student_courses)
            if (hours >= required_hours):
                overcount_flag = True
                break
            
            matched_course = get_intersection(list(repl_tuple), get_courses_only(list_of_student_courses))
            if (len(get_intersection(matched_course, intersection))):
                continue
            else:
                intersection.extend(matched_course)


    if (overcount_flag):
        intersection = get_combo_of_courses_for_hours_requirement(intersection, list_of_student_courses, required_hours)

    hours = get_hours_for_courses(intersection, list_of_student_courses)
    list_of_student_courses[:] = [course_gpa_tuple for course_gpa_tuple in list_of_student_courses if course_gpa_tuple[0] not in intersection]

    return intersection, hours

# list of courses: ('CS 123', 4.0)  grp: a group obj: (C/H, C/H amt., [courses_1,...,courses_n],[!courses],[repl])
# returns tuple: 'C', %completed, list of fulfilled courses
def check_C_type_group(grp : group, unique_grp_courses: list, student_courses_tuples : list):
    intersection = get_C_group_intersection_manual(grp, unique_grp_courses, student_courses_tuples, grp.goal_num)
    achieved_goal_num = len (intersection)

    return ['C', round(achieved_goal_num / grp.goal_num * 100, 2), intersection]


# returns tuple: 'H', %completed, list of fulfilled courses
def check_H_type_group(grp : group, unique_grp_courses: list, student_courses_tuples : list):
    intersection, achieved_hours = get_H_group_intersection_manual(grp, unique_grp_courses, student_courses_tuples, grp.goal_num)

    return ['H', round(achieved_hours / grp.goal_num * 100, 2), intersection]

def check_minors(list_of_minors, list_of_courses):
    for mnr in list_of_minors:
        check_groups(mnr.required_groups, list_of_courses)

#TODO: This method will take a students list of courses (from parser.py) and the entire list of minors (from minor_parser.py) and return a list of minors that are 'relevant' 
# to said student. Need to find set of 1-3 departments that comprise majority of the minor and see if the student has any courses in that department. 
def find_relevant_minor(list_of_courses, list_of_all_minors):
    return True

if __name__ == "__main__":
    df = create_pd('minor_data/minor_data.csv') 
    minors = create_minors(df)

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

    # print (check_C_type_group(minors[10].required_groups[0], get_unique_courses_in_group(minors[10], minors[10].required_groups[0]), roes_courses))
    # print (check_C_type_group(minors[10].required_groups[1], get_unique_courses_in_group(minors[10], minors[10].required_groups[1]), roes_courses))

    # print (check_H_type_group(minors[72].required_groups[0], roes_courses))

    # print (get_unique_courses_in_group(minors[0], minors[0].required_groups[1]))

    # unique = get_unique_courses_in_group(minors[0], minors[0].required_groups[0])

    # print (get_C_group_intersection_manual(minors[0].required_groups[0], unique, roes_courses, ))

    # print (tuple(filter(lambda x: 'MATH 453' in x, roes_courses)))

    # test = list(filter(lambda x: 'MATH 453' in x, roes_courses))
    # print (test[0][1])

    # print (dict(roes_courses))

    # print (get_hours_for_courses(['TEST 453'], roes_courses))

    print (check_H_type_group(minors[72].required_groups[0], get_unique_courses_in_group(minors[72], minors[72].required_groups[0]), roes_courses))