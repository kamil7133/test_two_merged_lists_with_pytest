import pytest
from MergeTwoSortedList import *

def test_merge_two_lists_case_1():
    solution = Solution()
    list1 = list_to_linked_list([1, 2, 4])
    list2 = list_to_linked_list([1, 3, 4])
    merged = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(merged) == [1, 1, 2, 3, 4, 4], "Failed on test case 1"

def test_merge_two_lists_case_2():
    solution = Solution()
    list1 = list_to_linked_list([1, 2, 3])
    list2 = list_to_linked_list([])
    merged = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(merged) == [1, 2, 3], "Failed on test case 2"

def test_merge_two_lists_case_3():
    solution = Solution()
    list1 = list_to_linked_list([])
    list2 = list_to_linked_list([])
    merged = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(merged) == [], "Failed on test case 3"

def test_merge_two_lists_case_4():
    solution = Solution()
    list1 = list_to_linked_list([5])
    list2 = list_to_linked_list([1])
    merged = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(merged) == [1, 5], "Failed on test case 4"

def test_merge_two_lists_case_5():
    solution = Solution()
    list1 = list_to_linked_list([1, 2])
    list2 = list_to_linked_list([3, 4, 5])
    merged = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(merged) == [1, 2, 3, 4, 5], "Failed on test case 5"

def test_merge_two_lists_case_6():
    solution = Solution()
    list1 = list_to_linked_list([1, 2])
    list2 = list_to_linked_list([3, 4, 5])
    merged = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(merged) == [1, 2, 3, 4, 5], "Failed on test case 6"

def test_merge_two_lists_case_7():
    solution = Solution()
    list1 = list_to_linked_list([3, 4, 5])
    list2 = list_to_linked_list([1, 2])
    merged = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(merged) == [1, 2, 3, 4, 5], "Failed on test case 7"

def test_merge_two_lists_case_8():
    solution = Solution()
    list1 = list_to_linked_list([1, 2, 4, 4])
    list2 = list_to_linked_list([1, 3, 4])
    merged = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(merged) == [1, 1, 2, 3, 4, 4, 4], "Failed on test case 8"
