import random
from stackoverflow.base_problem import BaseProblem

class P1FindMissingNumber(BaseProblem):
    def __init__(self, problem_number, sizes):
        super().__init__(problem_number, sizes)
        
        #**************************************************************
        # Problem P1: find missing number 
        # Source: Stack Overflow
        # Title: "Quickest way to find missing number in an array of numbers"
        # URL: https://stackoverflow.com/questions/2113795/quickest-way-to-find-missing-number-in-an-array-of-numbers
        # Voted Answer: 152
        # Date Posted: Oct 16,2012
        #**************************************************************
        self.stack_overflow_code = """
        def funcImp(arr):
            sum = 0
            idx = -1
            for i in range(len(arr)):
                if arr[i] == 1:
                    idx = i
                else:
                    sum += arr[i]

            total = (len(arr) + 1) * len(arr) / 2
            # print("missing number is: " + str(sum - total) + " at index " + str(idx))
            return (total - sum - 1)
        print(funcImp([0, 1, 2, 3, 4, 5, 7, 8, 9, 10]))
        """
    # Prepare a list for the problem_1 of finding a missing number by generating a list based on the size.
    def get_function_parameters(self, size):
        # Implement the logic specific to Class P1FindMissingNumber for getting function parameters
        # based on the size

        # Generate the complete list of numbers within the range
        lst = list(range(0, size , 1))
        # Select a random index to remove one number from the list
        missing_index = random.randint(0, len(lst)-1)
        # Remove the number at the selected index
        lst.pop(missing_index)
        # Randomly reorder the list
        lst = random.sample(lst, len(lst))

        arg1 = lst
        arg2 = 'N/A'
        return arg1, arg2

    def get_problem(self):
        return f"p{self.problem_number}_find_missing_number"
