import random
from stackoverflow.base_problem import BaseProblem

class p8ReverseList(BaseProblem):
    def __init__(self, problem_number, sizes):
        super().__init__(problem_number, sizes)

        #**************************************************************
        # Problem p8: reverse a list
        # Source: Stack Overflow
        # Title: "How do I reverse a list or loop over it backwards?"
        # URL: https://stackoverflow.com/questions/3940128/how-do-i-reverse-a-list-or-loop-over-it-backwards
        # Voted Answer: 1621
        # Date Posted: Oct 15,2010
        #**************************************************************
        self.stack_overflow_code = """
        def funcImp(xs):
            return(list(reversed(xs)))

        print(funcImp([21, 4, 1, 3, 9, 20, 25, 6, 21, 14]))
        """

    def get_function_parameters(self, size):
        lst = [random.randint(0, 1000000) for _ in range(size)]

        arg1 = lst
        arg2 = 'N/A'
        return arg1, arg2

    def get_problem(self):
        return f"p{self.problem_number}_reverse_list"

