class BaseProblem:
    def __init__(self, problem_number, sizes):
        self.problem_number = problem_number
        self.sizes = sizes
        self.problem_info = []

    def get_function_parameters(self, size):
        # Implement the logic to retrieve function parameters based on the size
        # This method should be overridden in the child classes p1, p2, ....., AND p15
        pass

    def get_problem(self):
        # Implement the logic to retrieve the problem name based on the problem number
        # This method should be overridden in the child classes p1, p2, ....., AND p15
        pass

    def get_info(self):
        params = []
        for size in self.sizes:
            arg1, arg2 = self.get_function_parameters(size)
            set = {
                'size': size,
                'arg1': arg1,
                'arg2': arg2
            }
            params.append(set)

        problem_set = {
            'problem_number': self.problem_number,
            'problem': self.get_problem(),
            'stack_overflow_code': self.stack_overflow_code,
            'function_parameters': params
        }
        self.problem_info.append(problem_set)
        return self.problem_info
