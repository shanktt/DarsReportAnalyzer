import json
from course import course
import os
import minor
import minor_parser

# TODO: in the creater give an argument that tells the thing to use the 
# creater for the dars report/one that creates one for the minor

# TODO: Make this file that does every from the other files
# for DARS report -> json file
def create_json(courses : list, minors=None, minor=False):

    # can use same function for creating JSON files for minors/DARS reports
    if not minor and minors is None:
        with open('sample.json', 'w') as outfile:
            json.dump([o.dump() for o in courses], outfile, indent=4)


# list of minors -> json file
def minor_to_json(minors : list):
    with open('minor_data.json', 'w') as outfile:
        json.dump([m.dump() for m in minors], outfile, indent=4)
        


minors = minor_parser.create_minor_list('minor_data.csv')
minor_to_json(minors)
print(minors[len(minors) - 1])




# List = []
# List.append(course('CS', 125, 4))
# List.append(course('CS', 225, 4))
# List2 = []
# List2.append(course('CS', 357, 3))
# List2.append(course('CS', 361, 3))
# List3 = []
# List3.append(course('CS', 421, 4))
# List3.append(course('CS', 233, 4))

# create_json(List + List2 + List3)