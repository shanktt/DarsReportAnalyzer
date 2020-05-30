import json
from course import course
import os
import minor
import minor_parser

# serializes the DARS report and the minor data into json files
def create_json(courses : list, minors=None, minor=False):

    # can use same function for creating JSON files for minors/DARS reports
    if not minor and minors is None:
        with open('sample.json', 'w') as outfile:
            json.dump([o.dump() for o in courses], outfile, indent=4)
    else:
        minor_to_json(minors)

# serialize a list of minors into a json file
def minor_to_json(minors : list):
    with open('minor_data.json', 'w') as outfile:
        json.dump([m.dump() for m in minors], outfile, indent=4)
        


# minors = minor_parser.create_minor_list('minor_data/minor_data.csv')
# minor_to_json(minors)
# print(minors[len(minors) - 1])
