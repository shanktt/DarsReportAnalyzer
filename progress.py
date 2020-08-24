from group import group
from minor import minor
from minor_parser import create_pd, create_minors
from dars_parser import get_courses_only

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