from test_two_merged_links_with_pytest.MergeTwoSortedList import *

def test():
    solution = Solution()

    #case 1
    list1 = list_to_linked_list([1,2,4])
    list2 = list_to_linked_list([1,3,4])
    merged = solution.mergeTwoLists(list1,list2)
    assert linked_list_to_list(merged) == [1, 1, 2, 3, 4, 4]

    #case 2
    list1 = list_to_linked_list([1, 2, 3])
    list2 = list_to_linked_list([])
    merged = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(merged) == [1, 2, 3]

    #case 3
    list1 = list_to_linked_list([])
    list2 = list_to_linked_list([])
    merged = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(merged) == []


    #case 4
    list1 = list_to_linked_list([5])
    list2 = list_to_linked_list([1, 3, 7])
    merged = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(merged) == [1, 3, 5, 7]