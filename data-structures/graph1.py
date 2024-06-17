from typing import List

def can_finish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    # Build graph using adjacency list
    graph = [[] for _ in range(numCourses)]  # Create an empty adjacency list for each course
    for course, pre_req in prerequisites:  # Iterate through the prerequisites
        graph[course].append(pre_req)  # Add the prerequisite to the adjacency list of the course
    
    # Track visited nodes and recursion stack
    visited = [0] * numCourses  # Create a visited array to keep track of visited nodes
    # 0: not visited, 1: visiting, 2: visited
    
    def dfs(course):
        if visited[course] == 1:  # If the course is currently being visited, it means there is a cycle
            return False
        if visited[course] == 2:  # If the course has already been visited, no need to visit again
            return True
        
        visited[course] = 1  # Mark the course as visiting
        for neighbor in graph[course]:  # Visit all the neighbors of the course
            if not dfs(neighbor):  # Recursively visit the neighbors
                return False
        
        visited[course] = 2  # Mark the course as visited after all neighbors are visited
        return True
    
    # Check for cycles in each course
    for course in range(numCourses):  # Iterate through each course
        if not dfs(course):  # Perform depth-first search on each course
            return False
    
    return True


def test_can_finish():
    assert can_finish(2, [[1,0]]) == True  # Test case: Course 1 depends on Course 0, so it can be finished
    assert can_finish(2, [[1,0], [0,1]]) == False  # Test case: Course 1 depends on Course 0 and Course 0 depends on Course 1, so it cannot be finished
    assert can_finish(4, [[1,0], [2,0], [3,1], [3,2]]) == True  # Test case: Course 1 depends on Course 0, Course 2 depends on Course 0, and Course 3 depends on both Course 1 and Course 2, so it can be finished
    assert can_finish(3, [[1,0], [2,1], [0,2]]) == False  # Test case: Course 1 depends on Course 0, Course 2 depends on Course 1, and Course 0 depends on Course 2, so it cannot be finished

def test_can_finish_with_empty_input():
    assert can_finish(0, []) == True  # Test case: No courses and no prerequisites, so it can be finished

if __name__ == "__main__":
    test_can_finish()  # Run the tests
    test_can_finish_with_empty_input()
    print("All tests passed.")
