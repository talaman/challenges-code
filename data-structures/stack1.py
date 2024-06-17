

def is_valid(s: str) -> bool:
    stack = []  # Initialize an empty stack to store opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}  # Define a mapping of closing brackets to their corresponding opening brackets
    
    for char in s:  # Iterate through each character in the input string
        if char in bracket_map.values():  # If the character is an opening bracket
            stack.append(char)  # Push it onto the stack
        elif char in bracket_map:  # If the character is a closing bracket
            if stack and stack[-1] == bracket_map[char]:  # Check if the stack is not empty and the top of the stack matches the corresponding opening bracket
                stack.pop()  # Pop the opening bracket from the stack
            else:
                return False  # If the stack is empty or the brackets don't match, return False
        else:
            return False  # If the character is neither an opening nor a closing bracket, return False
    
    return not stack  # If the stack is empty after processing all characters, return True; otherwise, return False

# Test cases

def test_is_valid():
    assert is_valid("()") == True  # Test case with balanced brackets
    assert is_valid("()[]{}") == True  # Test case with balanced brackets
    assert is_valid("(]") == False  # Test case with unbalanced brackets
    assert is_valid("([)]") == False  # Test case with unbalanced brackets
    assert is_valid("{[]}") == True  # Test case with balanced brackets

def test_is_valid_empty_string():
    assert is_valid("") == True  # Test case with empty string

def test_is_valid_single_type():
    assert is_valid("(((((())))))") == True  # Test case with balanced brackets of a single type
    assert is_valid("[[[[[[]]]]]]") == True  # Test case with balanced brackets of a single type
    assert is_valid("{{{{{{}}}}}}") == True  # Test case with balanced brackets of a single type

def test_is_valid_unbalanced():
    assert is_valid("(") == False  # Test case with unbalanced brackets
    assert is_valid(")") == False  # Test case with unbalanced brackets
    assert is_valid("(()") == False  # Test case with unbalanced brackets
    assert is_valid("())") == False  # Test case with unbalanced brackets

if __name__ == "__main__":
    test_is_valid()
    test_is_valid_empty_string()
    test_is_valid_single_type()
    test_is_valid_unbalanced()
    print("All tests passed.")