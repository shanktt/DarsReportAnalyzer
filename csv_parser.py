import pandas as pd
from group import group
from minor import minor

def create_pd(path):
    return pd.read_csv(path)

def create_minors(df):
    minors = []
    for index, row in df.iterrows():
        name = row['Minor:']
        required_courses = []
        #Checks if the row isn't empty so we don't get an error
        if not pd.isna(row['Required Classes:']):
            #removes all spaces from the string of classes and converts it into a list separated by commas
            required_courses = row['Required Classes:'].replace(' ', '').split(',')

        grouplist = []
        #Groups 1-6
        for n in range(1,7):
            #Checks if columns 'Group(n) Type:' isn't null
            if not pd.isna(row['Group'+str(n)+' Type:']):
                #Adds a group object to grouplist 
                grouplist.append(group(row['Group'+str(n)+' Type:'], row['Group'+str(n)+' Type Amt:'], row['Group'+str(n)+' List:'].replace(' ', '').split(',')))
        
        required_hours = row['Total Credit Hours:']

        minors.append(minor(name, required_courses, grouplist, required_hours))
    return minors



df = create_pd('dars_data.csv')
minors = create_minors(df)
for m in minors:
    print (m)