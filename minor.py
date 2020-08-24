from group import group
import itertools

class minor:
    def __init__(self, name_ : str, required_courses_ : list, required_groups_ : list, total_credits_ : int, repl_courses_ : list, dept_set_ : set):
        self.name = name_
        self.required_courses = required_courses_
        self.required_groups = required_groups_
        self.total_credits = total_credits_
        self.repl_courses = repl_courses_
        self.dept_set = dept_set_

    def __str__(self):
        return (f'{self.name}, {self.total_credits} hrs total. Required classes: {self.required_courses}. Required groups: {self.required_groups}. Replacement Courses: {self.repl_courses}. Department Set: {self.dept_set}')

    def __repr__(self):
        return (f'{self.name}, {self.total_credits}, {self.required_courses}, {self.required_groups}, {self.repl_courses}, {self.dept_set}')
    
    def __eq__(self, other):
        if (self.name == other.name and self.required_courses == other.required_courses 
        and self.required_groups == other.required_groups and self.total_credits == other.total_credits):
            return True
        return False
    
    def get_courses(self):
        return [c[0] for c in self.required_courses]

    def get_repl_courses_flattened(self):
        repl_courses = []
        for i in self.repl_courses:
            repl_courses.append(list(i)[1:])

        # flatten the list
        repl_courses = list(itertools.chain(*repl_courses))
        return repl_courses
