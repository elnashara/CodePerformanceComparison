import random
from stackoverflow.base_problem import BaseProblem

class p7Quicksort(BaseProblem):
    def __init__(self, problem_number, sizes):
        super().__init__(problem_number, sizes)

        #**************************************************************
        # Problem p7: Quicksort
        # Source: Stack Overflow
        # Title: "Quicksort with Python"
        # URL: https://stackoverflow.com/questions/18262306/quicksort-with-python
        # Voted Answer: 316
        # Date Posted: Aug 15,2013
        #**************************************************************
        self.stack_overflow_code = """
        def function1(array):
            # Sort the array by using quicksort.

            less = []
            equal = []
            greater = []

            if len(array) > 1:
                pivot = array[0]
                for x in array:
                    if x < pivot:
                        less.append(x)
                    elif x == pivot:
                        equal.append(x)
                    elif x > pivot:
                        greater.append(x)
                # Don't forget to return something!
                return function1(less)+equal+function1(greater)  # Just use the + operator to join lists
            # Note that you want equal ^^^^^ not pivot
            else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
                return array

        print(function1([21, 4, 1, 3, 9, 20, 25, 6, 21, 14]))
        """

    def get_function_parameters(self, size):
        lst = [random.randint(0, 1000000) for _ in range(size)]

        arg1 = lst
        arg2 = 'N/A'
        return arg1, arg2

    def get_problem(self):
        return f"p{self.problem_number}_quicksort"
