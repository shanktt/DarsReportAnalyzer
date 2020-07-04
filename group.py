class group:
    def __init__(self, goal_type_ : str, num_credits_or_num_courses : int, courses_ : list, unallowed_courses_ : list, repl_courses_ : list):
        self.goal_type = goal_type_
        self.goal_num = num_credits_or_num_courses
        self.courses = courses_
        self.unallowed_courses = unallowed_courses_
        self.repl_courses = repl_courses_
    
    def __str__(self):
        return (f'{self.__class__.__name__}({self.goal_type}, {self.goal_num}, {self.courses}, {self.unallowed_courses}, {self.repl_courses})') 
    
    def __repr__(self):
        return (f'{self.__class__.__name__}({self.goal_type}, {self.goal_num}, {self.courses}, {self.unallowed_courses}, {self.repl_courses})') 

    def get_courses(self):
        return [c[0] for c in self.courses]