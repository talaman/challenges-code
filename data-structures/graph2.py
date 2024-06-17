from typing import List, Tuple
from collections import deque

def shortest_path_binary_maze(maze: List[List[int]]) -> int:
    if not maze or maze[0][0] == 0 or maze[-1][-1] == 0:
        return -1
    
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    
    queue = deque([(0, 0, 1)])  # (row, col, distance)
    visited = set()
    visited.add((0, 0))
    
    while queue:
        row, col, dist = queue.popleft()
        
        # Check if we've reached the bottom-right corner
        if row == rows - 1 and col == cols - 1:
            return dist
        
        # Explore neighbors
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < rows and 0 <= c < cols and maze[r][c] == 1 and (r, c) not in visited:
                queue.append((r, c, dist + 1))
                visited.add((r, c))
    
    return -1

# Test cases

def test_shortest_path_binary_maze():
    maze1 = [
        [1, 1, 0, 1],
        [1, 1, 0, 1],
        [0, 1, 1, 1],
        [1, 0, 1, 1]
    ]
    assert shortest_path_binary_maze(maze1) == 6
    
    maze2 = [
        [1, 1, 0],
        [0, 1, 1],
        [1, 0, 1]
    ]
    assert shortest_path_binary_maze(maze2) == -1
    
    maze3 = [
        [1, 1],
        [1, 1]
    ]
    assert shortest_path_binary_maze(maze3) == 2

def test_shortest_path_binary_maze_edge_cases():
    assert shortest_path_binary_maze([]) == -1
    assert shortest_path_binary_maze([[0]]) == -1
    assert shortest_path_binary_maze([[1]]) == 1

if __name__ == "__main__":
    test_shortest_path_binary_maze()
    test_shortest_path_binary_maze_edge_cases()
    print("All tests passed!")
