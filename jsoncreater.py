import json
from course import course
import os

# TODO: in the creater give an argument that tells the thing to use the 
# creater for the dars report/one that creates one for the minor

# TODO: Make this file that does every from the other files
def convert_list_to_json(courses : list, minors=None, minor=False):
    for i in range(0, len(courses)):
        json_string = json.dumps([o.dump() for o in courses], indent=4, sort_keys=True)
    return json_string

def create_json(courses_json):
    if os.path.exists('sample.json'):
        os.remove('sample.json')
        f = open('sample.json', 'x')
    with open('sample.json', 'w') as outfile:
        json.dump(courses_json, outfile)

# List = []
# List.append(course('CS', 125, 4))
# List.append(course('CS', 225, 4))

# string = convert_list_to_json(List)
# print(string)
# create_json(string)