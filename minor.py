from typing import List
import collections
from group import group
from abc import ABC, abstractmethod

class minor(ABC):
    def __init__(self, name_ : str, required_courses_ : list, required_groups_ : list, total_credits_ : int, repl_courses_ : dict):
        self.name = name_
        self.required_courses = required_courses_
        self.required_groups = required_groups_
        self.total_credits = total_credits_
        self.repl_courses = repl_courses_

    def __str__(self):
        return (f'{self.name}, {self.total_credits} hrs total. Required classes: {self.required_courses}. REPL Courses: {self.repl_courses}. Required Groups: {self.required_groups}')