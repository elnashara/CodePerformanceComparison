import random
from stackoverflow.base_problem import BaseProblem

class p9CountFrequency(BaseProblem):
    def __init__(self, problem_number, sizes):
        super().__init__(problem_number, sizes)

        #**************************************************************
        # Problem p9: Count frequency
        # Source: Stack Overflow
        # Title: "How to count the frequency of the elements in an unordered list?"
        # URL: https://stackoverflow.com/questions/2161752/how-to-count-the-frequency-of-the-elements-in-an-unordered-list
        # Voted Answer: 634
        # Date Posted: Jan 29,2010
        #**************************************************************
        self.stack_overflow_code = """
        import collections
        def funcImp(a):
            return(collections.Counter(a))

        print(funcImp([5, 1, 2, 2, 4, 3, 1, 2, 3, 1, 1, 5, 2]))
        """

    def get_function_parameters(self, size):
        lst = [random.randint(0, 1000000) for _ in range(size)]

        arg1 = lst
        arg2 = 'N/A'
        return arg1, arg2

    def get_problem(self):
        return f"p{self.problem_number}_count_frequency"
