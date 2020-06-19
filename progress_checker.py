from group import group
from minor import minor
from minor_parser import create_pd, create_minors

def check_groups(list_of_groups, list_of_courses):
    for grp in list_of_groups:
        print(grp)
    
def get_group_intersection(grp_courses, list_of_courses):
        return list(set(grp_courses).intersection(list_of_courses))

def check_group(grp, list_of_courses):
    if grp.goal_type == 'C':   
        check_C_type_group(grp, list_of_courses)

    elif grp.goal_type == 'H':
        print('test')

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


df = create_pd('minor_data.csv') 
minors = create_minors(df)
check_minors(minors, 'test')