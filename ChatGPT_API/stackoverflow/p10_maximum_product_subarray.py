import random
from stackoverflow.base_problem import BaseProblem

class p10MaximumProductSubarray(BaseProblem):
    def __init__(self, problem_number, sizes):
        super().__init__(problem_number, sizes)
        
        #**************************************************************
        # Problem p10: maximum product subarray
        # Source: Stack Overflow
        # Title: "Maximum Product Subarray"
        # URL: https://stackoverflow.com/questions/25590930/maximum-product-subarray
        # Voted Answer: 0 // because this is the first Python sample.
        # Date Posted: Aug 31,2014
        #**************************************************************
        self.stack_overflow_code = """
        def function1(nums):
            l = len(nums)
            nums_l=nums #product_left_to_right 
            nums_r = nums[::-1] #product_right_to_left
            for i in range(1,l,1):
                nums_l[i] *= (nums_l[i-1] or 1) #if meets 0 then restart in-place by itself.
                nums_r[i] *= (nums_r[i-1] or 1) 
            return max(max(nums_l), max(nums_r))

        print(function1([5, 1, 2, 2, 4, 3, 1, 2, 3, 1, 1, 5, 2]))
        """

    def get_function_parameters(self, size):
        lst = [random.randint(0, 1000000) for _ in range(size)]

        arg1 = lst
        arg2 = 'N/A'
        return arg1, arg2

    def get_problem(self):
        return f"p{self.problem_number}_maximum_product_subarray"
