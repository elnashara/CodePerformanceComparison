import random
from stackoverflow.base_problem import BaseProblem

class p2FindDuplicateNumber(BaseProblem):
    def __init__(self, problem_number, sizes):
        super().__init__(problem_number, sizes)
        
        #**************************************************************
        # Problem P2: find duplicate
        # Source: Stack Overflow
        # Title: "Find the Duplicate Number"
        # URL: https://stackoverflow.com/questions/40167364/find-the-duplicate-number
        # Voted Answer: 2
        # Date Posted: Oct 16,2012
        #**************************************************************
        self.stack_overflow_code = """
        def function1(arr):
            n = len(arr) - 1                     # Get n as length of list - 1
            return sum(arr) - (n * (n + 1) / 2)  # n*(n+1)/2 is the sum of integers from 1 to n
        print(function1([1,2,3,4,4,5,6,7,8,9]))
        """

    # Prepare a list for the problem_2 of find duplicate in a list by generating a list based on the size.
    def get_function_parameters(self, size):
        # Generate the complete list of numbers within the range
        lst = list(range(0, size , 1))
        # select a random number from the list
        random_item = random.choice(lst)
        # append the random number to the list
        lst.append(random_item)
        # Randomly reorder the list
        lst = random.sample(lst, len(lst))

        arg1 = lst
        arg2 = 'N/A'
        return arg1, arg2

    def get_problem(self):
        return f"p{self.problem_number}_find_duplicate_number"
