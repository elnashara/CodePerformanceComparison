import timeit
import traceback
import textwrap
import random

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def create_linked_list(size):
    head = Node(random.randint(0, 1000000))
    current = head
    for i in range(size):
        current.next = Node(random.randint(0, 1000000))
        current = current.next

    return head

def create_linked_list_loop(size):
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

    return head

class RuntimeExecution:
    def __init__(self, func_code, versions):
        self.func_code = func_code
        self.versions = versions
        self._timeout_counter = 1

    def get_timeout_counter(self):
        return self._timeout_counter
    
    def execute(self, size, *args):
        try:
            for arg in args[0]:
                if size == arg['size']:
                    arg1 = arg['arg1']
                    arg2 = arg['arg2']
                    break
            
            if arg1 == 'LinkedList':
                arg1 = create_linked_list(size)
            elif arg1 == 'LinkedListwithLoop':
                arg1 = create_linked_list_loop(size)
            
            dedented_code = textwrap.dedent(self.func_code)
            compiled_code = compile(dedented_code, "<string>", "exec")
            # Execute the code string to define the function
            exec(compiled_code, globals())

            # Get the dynamically defined function by its name
            funcImp = globals().get("funcImp")
            if funcImp is None or not callable(funcImp):
                raise RuntimeError("funcImp function not found or not callable")

            time_list = []
            self._timeout_counter = 0
            for i in range(self.versions):
                # timeit.timeit() function returns the time in seconds.
                time_res = timeit.timeit(lambda: funcImp(i) if arg1 == 'N/A' and arg2 == 'N/A' else funcImp(arg1) if arg2 == 'N/A' else funcImp(arg1, arg2), number=100)
                time_list.append(time_res)
                del time_res
                self._timeout_counter += 1

            return (time_list, "N/A")
        except Exception as e:
            traceback.print_exc()
            raise
