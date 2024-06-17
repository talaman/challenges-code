# Define a class for the queue
class MyQueue:
    # Initialize the queue with two stacks
    def __init__(self):
        self.stack_in = []  # Stack for incoming items
        self.stack_out = []  # Stack for outgoing items

    # Method to add an item to the queue
    def push(self, x: int) -> None:
        self.stack_in.append(x)  # Add the item to the incoming stack

    # Method to remove an item from the queue
    def pop(self) -> int:
        self._transfer_if_needed()  # Ensure all items are in the outgoing stack
        return self.stack_out.pop()  # Remove the last item from the outgoing stack

    # Method to get the item at the front of the queue without removing it
    def peek(self) -> int:
        self._transfer_if_needed()  # Ensure all items are in the outgoing stack
        return self.stack_out[-1]  # Return the last item from the outgoing stack

    # Method to check if the queue is empty
    def empty(self) -> bool:
        # Return True if both stacks are empty, False otherwise
        return not self.stack_in and not self.stack_out

    # Private method to transfer items from the incoming stack to the outgoing stack
    def _transfer_if_needed(self):
        # If the outgoing stack is empty
        if not self.stack_out:
            # While there are items in the incoming stack
            while self.stack_in:
                # Move the items from the incoming stack to the outgoing stack
                self.stack_out.append(self.stack_in.pop())

# Test the queue operations
def test_queue_operations():
    queue = MyQueue()  # Create a new queue
    queue.push(1)  # Add 1 to the queue
    queue.push(2)  # Add 2 to the queue
    assert queue.peek() == 1  # Check that the front of the queue is 1
    assert queue.pop() == 1   # Check that removing an item from the queue returns 1
    assert not queue.empty()  # Check that the queue is not empty

# Test the empty queue
def test_queue_empty():
    queue = MyQueue()  # Create a new queue
    assert queue.empty() == True  # Check that the queue is empty

# Test the queue with multiple elements
def test_queue_with_multiple_elements():
    queue = MyQueue()  # Create a new queue
    queue.push(1)  # Add 1 to the queue
    queue.push(2)  # Add 2 to the queue
    queue.push(3)  # Add 3 to the queue
    assert queue.pop() == 1   # Check that removing an item from the queue returns 1
    assert queue.pop() == 2   # Check that removing an item from the queue returns 2
    assert queue.peek() == 3  # Check that the front of the queue is 3
    assert queue.pop() == 3   # Check that removing an item from the queue returns 3
    assert queue.empty() == True  # Check that the queue is empty

# Main function
# if __name__ == "__main__":
test_queue_operations()  # Run the queue operations test
test_queue_empty()  # Run the empty queue test
test_queue_with_multiple_elements()  # Run the multiple elements test
print("All tests passed.")  # Print a success message if all tests pass