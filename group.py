from enum import Enum, auto
from course import course


class grouptype(Enum):
    COURSES = auto()
    CREDIT_HOURS = auto()

class group:
    def __init__(self, goal_type_ : grouptype, num_credits_or_num_courses : int, courses_ : list):
        self.goal_type = goal_type_
        self.goal_num = num_credits_or_num_courses
        self.courses = courses_
    
    def __str__(self):
        return (f'{self.__class__.__name__}({self.goal_type.name}, {self.goal_num}, {self.courses})')
    
    def __repr__(self):
        return (f'{self.__class__.__name__}({self.goal_type.name}, {self.goal_num}, {self.courses})')


# a = course("ECE", 125, 4)
# b = course("CS", 125, 4)
# print(a == b)
# var = group(goal.credit_hours, 4, [course("CS", 125, 4), course("CS", 173, 4), course("CS", 225, 4)])
# print(var)
