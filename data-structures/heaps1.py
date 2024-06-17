import heapq

def find_kth_largest(nums, k):
    # Create a max-heap with the first k elements
    heap = nums[:k]  # Extract the first k elements from the list
    heapq.heapify(heap)  # Convert the list into a heap data structure
    
    # Iterate through the remaining elements
    for num in nums[k:]:
        # Push current element onto the heap
        heapq.heappush(heap, num)  # Add the current element to the heap
        # Pop the smallest element (maintains heap of size k)
        heapq.heappop(heap)  # Remove the smallest element from the heap
    
    # Return the kth largest element
    return heapq.heappop(heap)  # Return the smallest element in the heap, which is the kth largest element


def test_find_kth_largest():
    assert find_kth_largest([3,2,1,5,6,4], 2) == 5
    assert find_kth_largest([3,2,3,1,2,4,5,5,6], 4) == 4

def test_find_kth_largest_with_duplicates():
    assert find_kth_largest([3,2,3,1,2,4,5,5,6], 1) == 6
    assert find_kth_largest([3,2,3,1,2,4,5,5,6], 3) == 5

def test_find_kth_largest_edge_cases():
    assert find_kth_largest([1], 1) == 1
    assert find_kth_largest([-1, 2, 0], 1) == 2

if __name__ == "__main__":
    test_find_kth_largest()
    test_find_kth_largest_with_duplicates()
    test_find_kth_largest_edge_cases()
    print("All tests passed.")
