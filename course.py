class course:
    def __init__(self, dept_ : str, course_num_ : int, credit_hours_=None, repl_list_=None, course_pair_=None, counts_=True):
        self.dept = dept_
        self.course_num = course_num_
        self.credit_hours = credit_hours_
        self.repl_list = repl_list_
        self.course_pair = course_pair_
        self.counts = counts_
    
    def __str__(self):
        if self.repl_list is None and self.course_pair is None:
            return (f'{self.dept} {self.course_num}, {self.credit_hours} credit hours')
        return (f'{self.dept} {self.course_num}, {self.credit_hours} credit hours. A list of replacement courses are {self.repl_list}. Pair Class: {self.course_pair}. Counts for credit: {self.counts}')
    
    def __repr__(self):
        if self.repl_list is None and self.course_pair is None:
            return (f'{self.__class__.__name__}({self.dept}, {self.course_num}, {self.credit_hours}, {self.counts})')
        return (f'{self.__class__.__name__}({self.dept}, {self.course_num}, {self.credit_hours}, {self.repl_list}, {self.course_pair}, {self.counts})')
    
    def __eq__(self, other):
        return (self.dept == other.dept
        and self.course_num == other.course_num 
        and self.credit_hours == other.credit_hours
        and self.counts == other.counts)

    def dump(self):
        return {'course': {'dept': self.dept,
                            'course_num' : self.course_num,
                            'credit_hours' : self.credit_hours,
                            'repl_list' : self.repl_list,
                            'course_pair' : self.course_pair,
                            'counts' : self.counts}}
    
