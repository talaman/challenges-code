class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode()  # Create a dummy node to serve as the head of the merged list
    tail = dummy  # Initialize the tail pointer to the dummy node
    
    while list1 and list2:  # Iterate until either list1 or list2 becomes empty
        if list1.val < list2.val:  # If the value in list1 is smaller
            tail.next = list1  # Append list1 node to the merged list
            list1 = list1.next  # Move to the next node in list1
        else:  # If the value in list2 is smaller or equal
            tail.next = list2  # Append list2 node to the merged list
            list2 = list2.next  # Move to the next node in list2
        tail = tail.next  # Move the tail pointer to the newly added node
    
    if list1:  # If there are remaining nodes in list1
        tail.next = list1  # Append the remaining nodes to the merged list
    elif list2:  # If there are remaining nodes in list2
        tail.next = list2  # Append the remaining nodes to the merged list
    
    return dummy.next  # Return the merged list (excluding the dummy node)

# Helper function to create a linked list from a list
def create_linked_list(lst):
    dummy = ListNode()  # Create a dummy node to serve as the head of the linked list
    tail = dummy  # Initialize the tail pointer to the dummy node
    for value in lst:
        tail.next = ListNode(value)  # Create a new node with the given value
        tail = tail.next  # Move the tail pointer to the newly added node
    return dummy.next  # Return the linked list (excluding the dummy node)

# Helper function to convert linked list to a list
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)  # Append the value of the current node to the result list
        node = node.next  # Move to the next node
    return result  # Return the resulting list

# Test cases
# import pytest

def test_merge_two_lists():
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged_list = merge_two_lists(list1, list2)
    assert linked_list_to_list(merged_list) == [1, 1, 2, 3, 4, 4]

def test_merge_two_empty_lists():
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    merged_list = merge_two_lists(list1, list2)
    assert linked_list_to_list(merged_list) == []

def test_merge_one_empty_list():
    list1 = create_linked_list([1])
    list2 = create_linked_list([])
    merged_list = merge_two_lists(list1, list2)
    assert linked_list_to_list(merged_list) == [1]

def test_merge_lists_with_one_element_each():
    list1 = create_linked_list([2])
    list2 = create_linked_list([1])
    merged_list = merge_two_lists(list1, list2)
    assert linked_list_to_list(merged_list) == [1, 2]

if __name__ == "__main__":
    # pytest.main()
    test_merge_two_lists()
    test_merge_two_empty_lists()
    test_merge_one_empty_list()
    test_merge_lists_with_one_element_each()
    print("All tests passed")
