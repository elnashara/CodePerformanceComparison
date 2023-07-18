import random
from stackoverflow.base_problem import BaseProblem

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class p13RevereLinkedlist(BaseProblem):
    def __init__(self, problem_number, sizes):
        super().__init__(problem_number, sizes)

        #**************************************************************
        # Problem p13: Reversing a linked list 
        # Source: Stack Overflow
        # Title: "Reversing a linked list in python"
        # URL: https://stackoverflow.com/questions/21529359/reversing-a-linked-list-in-python
        # Voted Answer: 56
        # Date Posted: Feb 3,2014
        #**************************************************************
        self.stack_overflow_code = """
        def funcImp(head):
            new_head = None
            while head:
                head.next, head, new_head = new_head, head.next, head # look Ma, no temp vars!
            return new_head

        # Generate a linked list with 10 random numbers with a range of 1 to 200
        head = Node(random.randint(1, 200))
        current = head
        for i in range(10):
            current.next = Node(random.randint(1, 200))
            current = current.next

        current_node = head
        # print original liked list
        while current_node is not None:
            print(current_node.val, end=" ")
            current_node = current_node.next

        head_fun1_rev = funcImp(head)
        print('')
        # print reversed liked list
        current_node = head_fun1_rev
        while current_node is not None:
            print(current_node.val, end=" ")
            current_node = current_node.next
        """

    def get_function_parameters(self, size):
        # Generate a linked list with 1000000 random numbers with a range of 0 to size
        head = Node(random.randint(0, 1000000))
        current = head
        for i in range(size):
            current.next = Node(random.randint(0, 1000000))
            current = current.next

        arg1 = 'LinkedList'
        arg2 = 'N/A'
        return arg1, arg2

    def get_problem(self):
        return f"p{self.problem_number}_revere_linkedlist"
