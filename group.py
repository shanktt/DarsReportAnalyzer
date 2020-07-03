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

    # courses is a list of tuples. this method ignores the repl bool, just returns list of course strings
    def get_courses(self):
        course_list = []
        for c in self.courses:
            course_list.append(c[0])
        return course_list
