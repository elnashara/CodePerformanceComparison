import random
from stackoverflow.base_problem import BaseProblem

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class p14FindLengthLinkedList(BaseProblem):
    def __init__(self, problem_number, sizes):
        super().__init__(problem_number, sizes)

        #**************************************************************
        # Problem p14: Find the length of linked list
        # Source: Stack Overflow
        # Title: "Finding the length of a linked list in python"
        # URL: https://stackoverflow.com/questions/21529359/reversing-a-linked-list-in-python
        # Voted Answer: 5
        # Date Posted: Jul 10,2015
        #**************************************************************
        self.stack_overflow_code = """
        def funcImp(head):
            temp=head
            count=0
            while(temp):
                count+=1
                temp=temp.next
            return count

        # Generate a linked list with 10 random numbers with a range of 1 to 200
        head = Node(random.randint(1, 200))
        current = head
        for i in range(10):
            current.next = Node(random.randint(1, 200))
            current = current.next

        print(funcImp(head))    
        """

    def get_function_parameters(self, size):
        # Generate a linked list with 1000000 random numbers with a range of 0 to size
        head = Node(random.randint(0, 1000000))
        current = head
        for i in range(size):
            current.next = Node(random.randint(0, 1000000))
            current = current.next

        arg1 = head
        arg2 = 'N/A'
        return arg1, arg2

    def get_problem(self):
        return f"p{self.problem_number}_find_length_linkedList"

