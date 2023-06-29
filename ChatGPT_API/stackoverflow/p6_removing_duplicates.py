import random
from stackoverflow.base_problem import BaseProblem

class p6RemovingDuplicates(BaseProblem):
    def __init__(self, problem_number, sizes):
        super().__init__(problem_number, sizes)

        #**************************************************************
        # Problem p6: Removing duplicates
        # Source: Stack Overflow
        # Title: "Removing duplicates in lists"
        # URL: https://stackoverflow.com/questions/7961363/removing-duplicates-in-lists
        # Voted Answer: 2177
        # Date Posted: Nov 1,2011
        #**************************************************************
        self.stack_overflow_code = """
        def function1(t):
            return(list(set(t)))

        print(function1([1, 2, 3, 1, 2, 3, 5, 6, 7, 8]))
        """

    def get_function_parameters(self, size):
        lst = [random.randint(0, 1000000) for _ in range(size)]
        # Choose a random element from the list to be duplicated
        duplicate_element = random.choice(lst)
        # Append the duplicate element to the list
        lst.append(duplicate_element)

        # Choose a random element from the list to be duplicated
        duplicate_element = random.choice(lst)
        # Append the duplicate element to the list
        lst.append(duplicate_element)
        
        # Shuffle the list to mix the order
        random.shuffle(lst)

        arg1 = lst
        arg2 = 'N/A'
        return arg1, arg2

    def get_problem(self):
        return f"p{self.problem_number}_removing_duplicates"
