import random
from stackoverflow.base_problem import BaseProblem

class p5FindDuplicatesList(BaseProblem):
    def __init__(self, problem_number, sizes):
        super().__init__(problem_number, sizes)

        #**************************************************************
        # Problem p5: Find the duplicates in a list
        # Source: Stack Overflow
        # Title: "How do I find the duplicates in a list and create another list with them?"
        # URL: https://stackoverflow.com/questions/9835762/how-do-i-find-the-duplicates-in-a-list-and-create-another-list-with-them
        # Voted Answer: 890
        # Date Posted: Mar 23,2012
        #**************************************************************
        self.stack_overflow_code = """
        import collections
        def function1(array):
            return([item for item, count in collections.Counter(array).items() if count > 1])

        print(function1([1,2,3,2,1,5,6,5,5,5]))
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
        return f"p{self.problem_number}_find_duplicates_list"
