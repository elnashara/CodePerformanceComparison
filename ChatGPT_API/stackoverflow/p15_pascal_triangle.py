from stackoverflow.base_problem import BaseProblem

class p15PascalTriangle(BaseProblem):
    def __init__(self, problem_number, sizes):
        super().__init__(problem_number, sizes)

        #**************************************************************
        # Problem p15: pascal triangle
        # Source: Stack Overflow
        # Title: "Pascal's Triangle for Python"
        # URL: https://stackoverflow.com/questions/24093387/pascals-triangle-for-python
        # Voted Answer: 28
        # Date Posted: Jul 10,2015
        #**************************************************************
        self.stack_overflow_code = """
        import math
        # pascals_tri_formula = [] # don't collect in a global variable.
        def combination(n, r): # correct calculation of combinations, n choose k
            return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))
        def for_test(x, y): # don't see where this is being used...
            for y in range(x):
                return combination(x, y)
        def funcImp(rows):
            result = [] # need something to collect our results in
            # count = 0 # avoidable! better to use a for loop, 
            # while count <= rows: # can avoid initializing and incrementing 
            for count in range(rows): # start at 0, up to but not including rows number.
                # this is really where you went wrong:
                row = [] # need a row element to collect the row in
                for element in range(count + 1): 
                    # putting this in a list doesn't do anything.
                    # [pascals_tri_formula.append(combination(count, element))]
                    row.append(combination(count, element))
                result.append(row)
                # count += 1 # avoidable
            return result
        # now we can print a result:
        for row in funcImp(5):
            print(row)
        """

    def get_function_parameters(self, size):
        arg1 = 'N/A'
        arg2 = 'N/A'
        return arg1, arg2

    def get_problem(self):
        return f"p{self.problem_number}_pascal_triangle"
