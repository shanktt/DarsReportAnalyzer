from dataclasses import dataclass
from typing import List
import collections
from group import group

@dataclass
class minor:
    def __init__(self, name_ : str, required_courses_ : list, required_groups_ : list, total_credits_ : int):
        self.name = name_
        self.required_courses = required_courses_
        self.required_groups = required_groups_
        self.total_credits = total_credits_

    def __str__(self):
        return (f'{self.name}, {self.total_credits} hrs total. Required classes: {self.required_courses}')

    def __repr__(self):
        return (f'{self.name}, {self.total_credits}, {self.required_courses}, {self.required_groups}')

# cs_group = group(2, 3, ['CS 233', 'CS 241', 'CS 357', 'CS 374'])
# comp_sci_minor = minor('Computer Science', ['CS 125', 'CS 173', 'CS 225'], [cs_group], 20)
# print(comp_sci_minor)

# computer_science_minor = minor('Computer Science', ['CS 125', 'CS 173', 'CS 225'], 11, ['CS 233', 'CS 241', 'CS 357', 'CS 374', 'CS 410'], 9, [['CS 125', 'CS 173', 'CS 225']])
# # print(computer_science_minor)
# test = ['CS 125', 'CS 225']
# print (computer_science_minor.valid_required_classes_subset(test))