
def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the target element.
    
    :param arr: List[int] - A sorted list of integers
    :param target: int - The target integer to search for
    :return: int - The index of the target in the array if found, otherwise -1
    """
    left, right = 0, len(arr) - 1  # Initialize the left and right pointers
    
    while left <= right:  # Continue the loop until the left pointer is greater than the right pointer
        mid = left + (right - left) // 2  # Calculate the middle index
        
        if arr[mid] == target:  # If the middle element is equal to the target, return the index
            return mid
        elif arr[mid] < target:  # If the middle element is less than the target, update the left pointer
            left = mid + 1
        else:  # If the middle element is greater than the target, update the right pointer
            right = mid - 1
            
    return -1  # Return -1 if the target is not found

# Test cases

def test_binary_search():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2  # Test case: target is in the middle
    assert binary_search([1, 2, 3, 4, 5], 1) == 0  # Test case: target is at the beginning
    assert binary_search([1, 2, 3, 4, 5], 5) == 4  # Test case: target is at the end
    assert binary_search([1, 2, 3, 4, 5], 6) == -1  # Test case: target is not in the array
    assert binary_search([], 3) == -1  # Test case: empty array
    assert binary_search([1], 1) == 0  # Test case: single element array

def test_binary_search_edge_cases():
    assert binary_search([1, 2, 3, 4, 5], 2) == 1  # Test case: target is in the middle
    assert binary_search([1, 2, 3, 4, 5], 4) == 3  # Test case: target is in the middle
    assert binary_search([1, 2, 3, 4, 5], 0) == -1  # Test case: target is smaller than the smallest element
    assert binary_search([1, 2, 3, 4, 5], -1) == -1  # Test case: target is smaller than the smallest element
    assert binary_search([1, 3, 5, 7, 9], 9) == 4  # Test case: target is at the end
    assert binary_search([1, 3, 5, 7, 9], 1) == 0  # Test case: target is at the beginning

if __name__ == "__main__":
    test_binary_search()
    test_binary_search_edge_cases()
    print("All tests passed!")
