def two_sum(nums, target):
    num_to_index = {}  # Create an empty dictionary to store the numbers and their corresponding indices
    
    for i, num in enumerate(nums):  # Iterate through the list of numbers along with their indices
        difference = target - num  # Calculate the difference between the target and the current number
        if difference in num_to_index:  # Check if the difference exists in the dictionary
            return [num_to_index[difference], i]  # If the difference exists, return the indices of the two numbers
        num_to_index[num] = i  # Add the current number and its index to the dictionary
    
    return []  # If no solution is found, return an empty list


def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]  # Test case where the target is 9, expected output is [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]  # Test case where the target is 6, expected output is [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]  # Test case where the target is 6, expected output is [0, 1]
    assert two_sum([2, 5, 5, 11], 10) == [1, 2]  # Test case where the target is 10, expected output is [1, 2]

def test_two_sum_with_negatives():
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]  # Test case with negative numbers, target is -8, expected output is [2, 4]
    assert two_sum([-3, 4, 3, 90], 0) == [0, 2]  # Test case with negative and positive numbers, target is 0, expected output is [0, 2]

def test_two_sum_no_solution():
    assert two_sum([1, 2, 3, 4], 8) == []  # Test case where no solution is possible, target is 8, expected output is []

if __name__ == "__main__":
    test_two_sum()  # Run the test cases for the two_sum function
    test_two_sum_with_negatives()  # Run the test cases for the two_sum_with_negatives function
    test_two_sum_no_solution()  # Run the test cases for the two_sum_no_solution function
    print("All tests passed")  # Print a message indicating that all tests passed
