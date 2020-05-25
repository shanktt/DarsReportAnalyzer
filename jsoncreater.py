import json
from course import course
import os

# TODO: in the creater give an argument that tells the thing to use the 
# creater for the dars report/one that creates one for the minor

# TODO: Make this file that does every from the other files
def create_json(courses : list, minors=None, minor=False):

    # can use same function for creating JSON files for minors/DARS reports
    if not minor and minors is None:
        with open('sample.json', 'w') as outfile:
            json.dump([o.dump() for o in courses], outfile, indent=4)

List = []
List.append(course('CS', 125, 4))
List.append(course('CS', 225, 4))
List2 = []
List2.append(course('CS', 357, 3))
List2.append(course('CS', 361, 3))
List3 = []
List3.append(course('CS', 421, 4))
List3.append(course('CS', 233, 4))

create_json(List + List2 + List3)