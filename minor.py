from dataclasses import dataclass
from typing import List
import collections

@dataclass
class minor:
    name: str
    required_classes: List[str]
    required_classes_hours: int
    choice_classes: List[str]
    choice_classes_hours: int
    required_classes_subsets: List[List[str]]

    def valid_required_classes_subset(self, courses):
        for possible_courses_subset in self.required_classes_subsets:
            if collections.Counter(possible_courses_subset) == collections.Counter(courses):
                return True
        return False

computer_science_minor = minor('Computer Science', ['CS 125', 'CS 173', 'CS 225'], 11, ['CS 233', 'CS 241', 'CS 357', 'CS 374', 'CS 410'], 9, [['CS 125', 'CS 173', 'CS 225']])
# print(computer_science_minor)
test = ['CS 125', 'CS 225']
print (computer_science_minor.valid_required_classes_subset(test))