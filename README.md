# Implementation of Linked List Data Structure in Python with Unit Testing Using Pytest Framework

## Repository Overview

This repository contains a Python implementation of a singly linked list, featuring key operations and an efficient merging algorithm:

## Singly Linked List Implementation:

### Node Definition
A `ListNode` class defines the structure of a node, with attributes for its value and a pointer to the next node.
### Merging Two Sorted Linked Lists

The `mergeTwoLists` method merges two sorted linked lists into a single sorted linked list. It uses a dummy node to simplify the merging process:
A pointer, `current`, tracks the end of the merged list as we iterate through `list1` and `list2`.
The algorithm compares the current nodes of both lists, appending the smaller node to the merged list.
Once one of the lists is fully traversed, any remaining nodes from the other list are directly appended, ensuring `O(n)` time complexity, where n is the total number of nodes in both lists.
### Conversion Functions:

`list_to_linked_list` - Converts a Python list into a singly linked list.
`linked_list_to_list` - Converts a singly linked list back into a Python list.
### Unit Tests with Pytest
Comprehensive tests validate

- The merging algorithm across various scenarios, including edge cases with empty lists and lists of different lengths.
- The accuracy of the conversion functions, ensuring proper transformations between linked lists and Python lists.

## Getting Started

### Prerequisites

- Python 3.x
- pytest (for running tests)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/kamil7133/test_two_merged_links_with_pytest
   cd test_two_merged_links_with_pytest
2. Install the required packages (if any).

# Usage

### Example usage
    list1 = list_to_linked_list([1, 2, 4])
    list2 = list_to_linked_list([1, 3, 4])
    merged_list = mergeTwoLists(list1, list2)

### Convert the merged linked list back to a Python list and print
    print(linked_list_to_list(merged_list))  # Output: [1, 1, 2, 3, 4, 4]
# Running Tests
### To run the unit tests, execute the following command:

    pytest test_linked_list.py
### Test Results
All tests are passing! Below are the results from running the tests:

`============================= test session starts ==============================`

`collecting ... collected 8 items`

`test_merge_two_sorted_lists.py::test_merge_two_lists_case_1 PASSED       [ 12%]
test_merge_two_sorted_lists.py::test_merge_two_lists_case_2 PASSED       [ 25%]
test_merge_two_sorted_lists.py::test_merge_two_lists_case_3 PASSED       [ 37%]
test_merge_two_sorted_lists.py::test_merge_two_lists_case_4 PASSED       [ 50%]
test_merge_two_sorted_lists.py::test_merge_two_lists_case_5 PASSED       [ 62%]
test_merge_two_sorted_lists.py::test_merge_two_lists_case_6 PASSED       [ 75%]
test_merge_two_sorted_lists.py::test_merge_two_lists_case_7 PASSED       [ 87%]
test_merge_two_sorted_lists.py::test_merge_two_lists_case_8 PASSED       [100%]`

`============================== 8 passed in 0.01s ===============================`

# Implementation
### Definition of ListNode
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
### Functions for Linked List Operations
Convert a Python list to a linked list

    def list_to_linked_list(lst):
        dummy = ListNode()
        current = dummy
        for val in lst:
            current.next = ListNode(val)
            current = current.next
        return dummy.next
Convert a linked list to a Python list
    
    def linked_list_to_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
    return result
Merge Two Sorted Linked Lists

    def mergeTwoLists(list1, list2):
        dummy = ListNode()
        current = dummy
    
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                current = list1
                list1 = list1.next
            else:
                current.next = list2
                current = list2
                list2 = list2.next
        current.next = list1 if list1 else list2
        return dummy.next
# Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request