def length_of_longest_substring(s: str) -> int:
    char_set = set()  # Create an empty set to store unique characters
    left = 0  # Initialize the left pointer
    max_length = 0  # Initialize the maximum length of the substring
    
    for right in range(len(s)):  # Iterate through the string using the right pointer
        while s[right] in char_set:  # Check if the current character is already in the set
            char_set.remove(s[left])  # If it is, remove the character at the left pointer from the set
            left += 1  # Move the left pointer to the right
        char_set.add(s[right])  # Add the current character to the set
        max_length = max(max_length, right - left + 1)  # Update the maximum length of the substring
    
    return max_length  # Return the maximum length of the longest substring

# Test cases
print(length_of_longest_substring("abcabcbb"))  # Expected output: 3
print(length_of_longest_substring("bbbbb"))     # Expected output: 1
print(length_of_longest_substring("pwwkew"))    # Expected output: 3
print(length_of_longest_substring(""))          # Expected output: 0
print(length_of_longest_substring("au"))        # Expected output: 2
print(length_of_longest_substring("dvdf"))      # Expected output: 3