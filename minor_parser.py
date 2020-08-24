import pandas as pd
from group import group
from minor import minor

def create_pd(path):
    return pd.read_csv(path)

def create_minors(df):
    minors = []
    for index, row in df.iterrows():
        # Get name of the minor
        name = row['Minor:']

        # Empty list to represent required courses for a minor
        required_courses = []
        # Empty list for repl_courses in a minor
        repl_courses_minor = []
        # Set to represent set of all course departments in minor
        depts = set()

        # Checks if the row isn't empty so we don't get an error
        if not pd.isna(row['Required Classes:']):
            # Converts a string of classses it into a list, strings are split based on commas
            required_courses_raw = row['Required Classes:'].split(',')
        
            # Iterate through list of courses to see if there are any repl_courses
            for course in required_courses_raw:
                if 'REPL' in course:
                    # Calls parse_repl_courses method to add to parse repl course string and append to repl_courses_minor dict 
                    required_courses.append((parse_repl_courses(course, repl_courses_minor, depts), True))
                else:
                    # Add course to required_courses while stripping any extra white space. Indicate that this course has not repl options
                    required_courses.append((course.strip(), False))
                    depts.add(course.strip().split(' ')[0])
        
        # Empty list to represent a list of groups for a minor
        grouplist = []
        
        # Groups 1-6
        for n in range(1,7):
            #Checks if columns of form 'Group(n) Type:' isn't null
            if not pd.isna(row['Group'+str(n)+' Type:']):
                # List to represent repl courses in a group
                repl_course_group = []
                # List to represent list of courses in a group
                group_courses = []
                
                # Converts a string of classses it into a list, strings are split based on commas
                group_courses_raw = row['Group'+str(n)+' List:'].split(',')

                for course in group_courses_raw:
                    if 'REPL' in course:
                        # Calls parse_repl_courses method to add to parse repl course string and append to repl_course_group list 
                        group_courses.append((parse_repl_courses(course, repl_course_group, depts), True))
                    else:
                        group_courses.append((course.strip(), False))
                        # get the course dept/add it to the set of course depts
                        depts.add(course.strip().split(' ')[0])

                # Adds a group object to grouplist
                grouplist.append(group(row['Group'+str(n)+' Type:'], row['Group'+str(n)+' Type Amt:'], group_courses, repl_course_group))

        # Get minimum number of hours to complete a minor
        required_hours = row['Total Credit Hours:']
        # Create minor object and store in minors list
        minors.append(minor(name.upper(), required_courses, grouplist, required_hours, repl_courses_minor, depts))
    return minors

def parse_repl_courses(course_str, repl_list, dept_set):
    # Split the string into a list of courses, splitting is based on 'REPL' substring
    repl_course_list = course_str.split('REPL')
    # Removes any extra whitespace from strings in repl_course_list
    repl_course_list = [s.strip() for s in repl_course_list]
    # for course in replacement list add the deptartment to the set of departments
    [dept_set.add(s.split(' ')[0]) for s in repl_course_list]
    # Append a tuple in repl_list of the REPL courses from repl_course_list
    # For example: 'CS 125 REPL ECE 220 REPL TEST 440' -> ('CS 125', 'ECE 220', 'TEST 440)
    repl_list.append(tuple(repl_course_list))

    # Return first entry in repl_course_list
    return repl_course_list[0]