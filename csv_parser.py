import pandas as pd
from group import group
from minor import minor

def create_pd(path):
    return pd.read_csv(path)

#TODO: Convert course strings into course objects
def create_minors(df):
    minors = []
    for index, row in df.iterrows():
        # Get name of the minor
        name = row['Minor:']

        # Empty list to represent required courses for a minor
        required_courses = []
        # Empty dictionary for repl_courses in a minor
        repl_courses_minor = {}

        # Checks if the row isn't empty so we don't get an error
        if not pd.isna(row['Required Classes:']):
            # Converts a string of classses it into a list, strings are split based on commas
            required_courses_raw = row['Required Classes:'].split(',')
        
            # Iterate through list of courses to see if there are any repl_courses
            for course in required_courses_raw:
                if 'REPL' in course:
                    # Split the string into a list of courses, splitting is based on 'REPL' substring
                    repl_course_list = course.split('REPL')
                    # Removes any extra whitespace from strings in repl_course_list
                    repl_course_list = [s.strip() for s in repl_course_list]
                    # Create an entry in repl_courses_minor where the first entry in repl_course_list is the key and the following entries are the values
                    # For example: 'CS 125 REPL ECE 220 REPL TEST 440' -> 'CS 125' : ['ECE 220', 'TEST 440']
                    repl_courses_minor[repl_course_list[0]] = repl_course_list
                    # Add first entry to list of required courses. Indicate that this course has repl options
                    required_courses.append((repl_course_list[0], True))
                else:
                    # Add course to required_courses while stripping any extra white space. Indicate that this course has not repl options
                    required_courses.append((course.strip(), False))
        
        # Empty list to represent a list of groups for a minor
        grouplist = []
        # Groups 1-6
        for n in range(1,7):
            #Checks if columns of form 'Group(n) Type:' isn't null
            if not pd.isna(row['Group'+str(n)+' Type:']):
                # Dictionary to represent repl courses in a group
                repl_course_group = {}
                # List to represent list of courses in a group
                group_courses = []
                
                # Converts a string of classses it into a list, strings are split based on commas
                group_courses_raw = row['Group'+str(n)+' List:'].split(',')

                for course in group_courses_raw:
                    if 'REPL' in course:
                        repl_course_list = course.split('REPL')
                        repl_course_list = [s.strip() for s in repl_course_list]
                        repl_course_group[repl_course_list[0]] = repl_course_list
                        group_courses.append((repl_course_list[0], True))
                    else:
                        group_courses.append((course.strip(), False))
                
                # List to represent courses that are not allowed for a group
                unallowed_courses_group = []
                if not pd.isna(row['Group'+str(n)+' Courses Not Allowed:']):
                    unallowed_courses_group = row['Group'+str(n)+' Courses Not Allowed:'].replace(' ', '').split(',')

                # Adds a group object to grouplist
                grouplist.append(group(row['Group'+str(n)+' Type:'], row['Group'+str(n)+' Type Amt:'], group_courses, unallowed_courses_group, repl_course_group))

        # Get minimum number of hours to complete a minor
        required_hours = row['Total Credit Hours:']

        # Create minor object and store in minors list
        minors.append(minor(name, required_courses, grouplist, required_hours, repl_courses_minor))
    return minors


df = create_pd('minor_data.csv') 
# create_minors(df)
minors = create_minors(df)
for m in minors:
    print (m)