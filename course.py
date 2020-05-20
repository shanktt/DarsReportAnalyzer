class course:
    def __init__(self, dept_ : str, course_num_ : int, credit_hours_ : int, repl_dept_=None, repl_course_num_=None, repl_credit_hours_=None):
        self.dept = dept_
        self.course_num = course_num_
        self.credit_hours = credit_hours_
        self.repl_dept = repl_dept_
        self.repl_course_num = repl_course_num_
        self.repl_credit_hours = repl_credit_hours_
    
    def __str__(self):
        if self.repl_dept is None:
            return (f'{self.dept} {self.course_num}, {self.credit_hours} credit hours')
        return (f'{self.dept} {self.course_num}, {self.credit_hours} credit hours. A replacement course is {self.repl_dept} {self.repl_course_num}, {self.repl_credit_hours} credit hours.')
    
    def __repr__(self):
        if self.repl_dept is None:
            return (f'{self.__class__.__name__}({self.dept}, {self.course_num}, {self.credit_hours})')
        return (f'{self.__class__.__name__}({self.dept}, {self.course_num}, {self.credit_hours}, {self.repl_dept}, {self.repl_course_num}, {self.repl_credit_hours})')
    
    def __eq__(self, other):
        if self.dept == other.dept and self.course_num == other.course_num and self.credit_hours == other.credit_hours:
            return True
        return False