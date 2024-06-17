
def quick_sort(arr):
    """
    Perform Quick Sort on the array.
    
    :param arr: List[int] - A list of integers to be sorted
    :return: List[int] - The sorted list of integers
    """
    if len(arr) <= 1:
        return arr
    
    # Selecting the pivot element as the middle element of the array
    pivot = arr[len(arr) // 2]
    
    # Partitioning the array into three sub-arrays: left, middle, and right
    left = [x for x in arr if x < pivot]       # Elements smaller than the pivot
    middle = [x for x in arr if x == pivot]    # Elements equal to the pivot
    right = [x for x in arr if x > pivot]      # Elements greater than the pivot
    
    # Recursively sorting the left and right sub-arrays
    return quick_sort(left) + middle + quick_sort(right)

# Test cases

def test_quick_sort():
    assert quick_sort([3, 6, 8, 10, 1, 2, 1]) == [1, 1, 2, 3, 6, 8, 10]
    assert quick_sort([3, -1, 0, 10, -2, 8, 4]) == [-2, -1, 0, 3, 4, 8, 10]
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert quick_sort([3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3]
    assert quick_sort([]) == []
    assert quick_sort([1]) == [1]

def test_quick_sort_edge_cases():
    assert quick_sort([1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1]
    assert quick_sort([5, 5, 5, 2, 2, 2, 8, 8, 8]) == [2, 2, 2, 5, 5, 5, 8, 8, 8]
    assert quick_sort([-1, -5, 0, 3, 9, 2, -2, 6]) == [-5, -2, -1, 0, 2, 3, 6, 9]
    assert quick_sort([2, 1, 1, 3, 3, 0, 4]) == [0, 1, 1, 2, 3, 3, 4]

if __name__ == "__main__":
    test_quick_sort()
    test_quick_sort_edge_cases()
    print("All tests passed!")
