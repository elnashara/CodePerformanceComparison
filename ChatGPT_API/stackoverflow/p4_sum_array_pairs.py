import random
from stackoverflow.base_problem import BaseProblem

class p4SumArrayPairs(BaseProblem):
    def __init__(self, problem_number, sizes):
        super().__init__(problem_number, sizes)
        
        #**************************************************************
        # Problem P4: count pairs with given sum
        # Source: Stack Overflow
        # Title: "Count pairs of elements in an array whose sum equals a given sum (but) do it in a single iteration(!)"
        # URL: https://stackoverflow.com/questions/64727140/count-pairs-of-elements-in-an-array-whose-sum-equals-a-given-sum-but-do-it-in
        # Voted Answer: 1
        # Date Posted: Nov 7,2020
        #**************************************************************
        self.stack_overflow_code = """
        def funcImp(array, sum):
            pairs_count = 0

            seen_values = defaultdict(int)
            
            for value in array:
                complement = sum - value
                if seen_values[complement] > 0:
                    pairs_count += 1
                    seen_values[complement] -= 1
                else:
                    seen_values[value] += 1
            
            return pairs_count
        
        # Test the function
        print(funcImp([12, 11, 0, 35, 16, 17, 23, 21, 5], 23))
        """

    def get_function_parameters(self, size):
        lst = [random.randint(0, 1000000) for _ in range(size)]

        # select a random two numbers from the list
        random_item_1 = random.choice(lst)
        random_item_2 = random.choice(lst)
        sum_elements = random_item_1 + random_item_2

        arg1 = lst
        arg2 = sum_elements
        return arg1, arg2

    def get_problem(self):
        return f"p{self.problem_number}_sum_array_pairs"
