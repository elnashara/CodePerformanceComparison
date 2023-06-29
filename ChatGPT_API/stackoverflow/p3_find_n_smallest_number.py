import random
from stackoverflow.base_problem import BaseProblem

class p3FindNSmallestNumber(BaseProblem):
    def __init__(self, problem_number, sizes):
        super().__init__(problem_number, sizes)

        #**************************************************************
        # Problem P3: find n smallest indices
        # Source: Stack Overflow
        # Title: "Python algorithm to find the indexes of the k smallest number in an unsorted array?"
        # URL: https://stackoverflow.com/questions/55183783/python-algorithm-to-find-the-indexes-of-the-k-smallest-number-in-an-unsorted-arr
        # Voted Answer: 1
        # Date Posted: Mar 15,2019
        #**************************************************************
        self.stack_overflow_code = """
        from heapq import nsmallest
        from operator import itemgetter
        def function1(seq, n):
            smallest_with_indices = nsmallest(n, enumerate(seq), key=itemgetter(1))
            return [i for i, x in smallest_with_indices]
        print(function1([12, 11, 0, 35, 16, 17, 23, 21, 5], 3))
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
        k = 5
        arg1 = lst
        arg2 = k
        return arg1, arg2

    def get_problem(self):
        return f"p{self.problem_number}_find_n_smallest_number"
