import random
from stackoverflow.base_problem import BaseProblem

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class p12DetectLoopInLinkedlist(BaseProblem):
    def __init__(self, problem_number, sizes):
        super().__init__(problem_number, sizes)

        #**************************************************************
        # Problem p12: Detect loop in a Linked List
        # Source: Stack Overflow
        # Title: "How to detect a loop in a linked list?"
        # URL: https://stackoverflow.com/questions/2663115/how-to-detect-a-loop-in-a-linked-list
        # Voted Answer: 595
        # Date Posted: Apr 18,2010
        # The code on the StackOverflow website was originally written in Java, but I converted it to Python.
        #**************************************************************
        self.stack_overflow_code = """
        def funcImp(first):
            if first is None:
                return False
            slow = first
            fast = first
            while True:
                slow = slow.next
                if fast.next is not None:
                    fast = fast.next.next
                else:
                    return False
                if slow is None or fast is None:
                    return False
                if slow == fast:
                    return True

        # Generate a linked list with 100 random numbers with a range of 1 to 200
        head = Node(random.randint(1, 200))
        current = head
        for i in range(100):
            current.next = Node(random.randint(1, 200))
            current = current.next

        # Create a loop in the linked list (connect the last node to a random node)
        last_node = current
        random_node = head
        for i in range(random.randint(1, 100)):
            random_node = random_node.next
        last_node.next = random_node

        print(funcImp(head))
        """

    def get_function_parameters(self, size):
        # Generate a linked list with 1000000 random numbers with a range of 0 to size
        head = Node(random.randint(0, 1000000))
        current = head
        for i in range(size):
            current.next = Node(random.randint(0, 1000000))
            current = current.next

        # Create a loop in the linked list (connect the last node to a random node)
        last_node = current
        random_node = head
        for i in range(random.randint(1, 100)):
            random_node = random_node.next
        last_node.next = random_node            

        arg1 = head
        arg2 = 'N/A'
        return arg1, arg2

    def get_problem(self):
        return f"p{self.problem_number}_detect_loop_in_linkedlist"
