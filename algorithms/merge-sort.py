
def merge_sort(arr):
    """
    Perform Merge Sort on the array.
    
    :param arr: List[int] - A list of integers to be sorted
    :return: List[int] - The sorted list of integers
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])  # Recursively sort the left half of the array
    right_half = merge_sort(arr[mid:])  # Recursively sort the right half of the array

    return merge(left_half, right_half)  # Merge the sorted left and right halves

def merge(left, right):
    """
    Merge two sorted lists into one sorted list.
    
    :param left: List[int] - The first sorted list
    :param right: List[int] - The second sorted list
    :return: List[int] - The merged and sorted list
    """
    sorted_list = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:  # Compare the elements from the left and right lists
            sorted_list.append(left[left_index])  # Append the smaller element to the sorted list
            left_index += 1
        else:
            sorted_list.append(right[right_index])  # Append the smaller element to the sorted list
            right_index += 1

    sorted_list.extend(left[left_index:])  # Append the remaining elements from the left list
    sorted_list.extend(right[right_index:])  # Append the remaining elements from the right list
    
    return sorted_list

# Test cases

def test_merge_sort():
    assert merge_sort([3, 6, 8, 10, 1, 2, 1]) == [1, 1, 2, 3, 6, 8, 10]
    assert merge_sort([3, -1, 0, 10, -2, 8, 4]) == [-2, -1, 0, 3, 4, 8, 10]
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert merge_sort([3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3]
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]

def test_merge_sort_edge_cases():
    assert merge_sort([1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1]
    assert merge_sort([5, 5, 5, 2, 2, 2, 8, 8, 8]) == [2, 2, 2, 5, 5, 5, 8, 8, 8]
    assert merge_sort([-1, -5, 0, 3, 9, 2, -2, 6]) == [-5, -2, -1, 0, 2, 3, 6, 9]
    assert merge_sort([2, 1, 1, 3, 3, 0, 4]) == [0, 1, 1, 2, 3, 3, 4]

if __name__ == "__main__":
    test_merge_sort()
    test_merge_sort_edge_cases()
    print("All tests passed!")
