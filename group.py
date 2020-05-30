from enum import Enum, auto
from course import course


class goal(Enum):
    credit_hours = auto()
    num_courses = auto()

class group:
    def __init__(self, goal_type_ : goal, num_credits_or_num_courses : int, courses_ : list):
        self.goal_type = goal_type_
        self.goal_num = num_credits_or_num_courses
        self.courses = courses_
    
    def __str__(self):
        return (f'{self.__class__.__name__}({self.goal_type}, {self.goal_num}, {self.courses})') #self.goal_type.name


# a = course("ECE", 125, 4)
# b = course("CS", 125, 4)
# print(a == b)
# var = group(goal.credit_hours, 4, [course("CS", 125, 4), course("CS", 173, 4), course("CS", 225, 4)])
# print(var)
