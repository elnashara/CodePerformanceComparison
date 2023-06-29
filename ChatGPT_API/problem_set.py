from stackoverflow.p1_find_missing_number import P1FindMissingNumber
from stackoverflow.p2_find_duplicate_number import p2FindDuplicateNumber
from stackoverflow.p3_find_n_smallest_number  import p3FindNSmallestNumber
from stackoverflow.p4_sum_array_pairs import p4SumArrayPairs
from stackoverflow.p5_find_duplicates_list import p5FindDuplicatesList
from stackoverflow.p6_removing_duplicates import p6RemovingDuplicates
from stackoverflow.p7_quicksort import p7Quicksort
from stackoverflow.p8_reverse_list import p8ReverseList
from stackoverflow.p9_count_frequency import p9CountFrequency
from stackoverflow.p10_maximum_product_subarray import p10MaximumProductSubarray
from stackoverflow.p11_find_middle_element_linkedlist import p11FindMiddleElementLinkedlist
from stackoverflow.p12_detect_loop_in_linkedlist import p12DetectLoopInLinkedlist
from stackoverflow.p13_revere_linkedlist import p13RevereLinkedlist
from stackoverflow.p14_find_length_linkedList import p14FindLengthLinkedList
from stackoverflow.p15_pascal_triangle import p15PascalTriangle

class ProblemSet:
    def __init__(self, problem_number, sizes):
        self.problem_number = problem_number
        self.sizes = sizes
        self.problem_instance = self.create_problem_instance()

    def create_problem_instance(self):
        problem_classes = {
            1: P1FindMissingNumber,
            2: p2FindDuplicateNumber,
            3: p3FindNSmallestNumber,
            4: p4SumArrayPairs,
            5: p5FindDuplicatesList,
            6: p6RemovingDuplicates,
            7: p7Quicksort,
            8: p8ReverseList,
            9: p9CountFrequency,
            10: p10MaximumProductSubarray,
            11: p11FindMiddleElementLinkedlist,
            12: p12DetectLoopInLinkedlist,
            13: p13RevereLinkedlist,
            14: p14FindLengthLinkedList,
            15: p15PascalTriangle
            }

        problem_class = problem_classes.get(self.problem_number)
        if problem_class:
            return problem_class(self.problem_number, self.sizes)
        else:
            raise ValueError("Invalid problem number")
        
    def handle_problem_number(self):
        return self.problem_instance.get_info()
