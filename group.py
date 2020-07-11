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

    # Converts the list of tuples into a flat list: [('CS 125', 'ECE 220'), ('CS 173', 'MATH 213')] -> ['CS 125', 'ECE 220', 'CS 173', 'MATH 213']
    def get_repl_courses_as_flat_list(self):
        return [course for courses_tuple in self.repl_courses for course in courses_tuple]

    # Converts the list of tuples into a dictionary where the first element in the tuple is the key the and rest of the elements in the tuple are the value (in the form of a list of strings)
    def convert_repl_courses_into_dict(self):
        return dict([(repl_tuple[0], list(repl_tuple[1:])) for repl_tuple in self.repl_courses])