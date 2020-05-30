from typing import List
import collections
from group import group
from abc import ABC, abstractmethod

class minor(ABC):
    def __init__(self, name_ : str, required_courses_ : list, required_groups_ : list, total_credits_ : int):
        self.name = name_
        self.required_courses = required_courses_
        self.required_groups = required_groups_
        self.total_credits = total_credits_

    def __str__(self):
        return (f'{self.name}, {self.total_credits} hrs total. Required classes: {self.required_courses}. Required groups: {self.required_groups}')

    def __repr__(self):
        return (f'{self.name}, {self.total_credits}, {self.required_courses}, {self.required_groups}')
    
    def __eq__(self, other):
        if (self.name == other.name and self.required_courses == other.required_courses 
        and self.required_groups == other.required_groups and self.total_credits == other.total_credits):
            return True
        return False

    # TODO: for dumps use .__str__ or repr to represent one of the courses/just repr the group as its own object figure it out