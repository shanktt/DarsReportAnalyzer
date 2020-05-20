class course:
    def __init__(self, dept_, course_num_, credit_hours_):
        self.dept = dept_
        self.course_num = course_num_
        self.credit_hours = credit_hours_
    
    def __str__(self):
        return (f'{self.dept} {self.course_num}, {self.credit_hours} credit hours')
    
    def __repr__(self):
        return (f'{self.__class__.__name__}({self.dept}, {self.course_num}, {self.credit_hours})')