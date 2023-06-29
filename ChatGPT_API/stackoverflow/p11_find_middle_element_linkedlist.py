import random
from stackoverflow.base_problem import BaseProblem

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class p11FindMiddleElementLinkedlist(BaseProblem):
    def __init__(self, problem_number, sizes):
        super().__init__(problem_number, sizes)

        #**************************************************************
        # Problem p11: Find middle element linkedlist
        # Source: Stack Overflow
        # Title: "How to find middle element in a python linked list in a single traversal?"
        # URL: https://stackoverflow.com/questions/50656320/how-to-find-middle-element-in-a-python-linked-list-in-a-single-traversal
        # Voted Answer: 2
        # Date Posted: Jun 2,2018
        #**************************************************************
        self.stack_overflow_code = """
        def funcImp(head, count=0):
            yield head
            if not head.next:
            yield [count]
            else: 
            yield from funcImp(head.next, count+1)

        # Create a linked list with 100 random unsorted numbers with range 1 to 200
        list=[]
        head = Node(random.randint(1, 200))
        current = head
        for i in range(10):
            current.next = Node(random.randint(1, 200))
            list.append(current.val)
            current = current.next

        *l, [count] = funcImp(head)
        print(f'full list: {list}')
        print('middle value:', list[count//2])
        """

    def get_function_parameters(self, size):
        head = Node(random.randint(0, 1000000))
        current = head
        for i in range(size):
            current.next = Node(random.randint(0, 1000000))
            current = current.next

        arg1 = head
        arg2 = 'N/A'
        return arg1, arg2

    def get_problem(self):
        return f"p{self.problem_number}_find_middle_element_linkedlist"
