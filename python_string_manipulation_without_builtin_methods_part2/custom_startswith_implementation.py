# Prog05. startswith() check if the string beginning part matches the 
# function parameter. Create a program that do the same functionality 
# without using startswith() function.

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program that implement a custom method to check if a string starts with a specific substring.
# - Scope: A function that determines if a string starts with given characters.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Check if the string starts with a specified substring
#     - Work with different substring lengths
#     - Must be case-sensitive
#     - Cannot use built-in startswith() method

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Input the original string and the substring to check from the user
#     2. Compare the start of the string with the given substring
#        2.1. If the length of the substring is greater than the original string, return False
#        2.2. Manually compare each character from the start of the string
#     3. Return True if all characters match, otherwise return False

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Input the original string and substring
text = input("Enter the original string: ")
substring = input("Enter the substring to check: ")

# Check if the substring is longer than the original string
if len(substring) > len(text):
    result = False
else:
    # Compare characters from the start of the string
    result = True

    for i in range(len(substring)):
        if text[i] != substring[i]:
            result = False
            break

print(f"Output: {result}")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1:
# - Input: "Hello World" starting with "Hello"
# - Expected Output: True

# Test Case 2:
# - Input: "Python Programming" starting with "Py"
# - Expected Output: True

# Test Case 3:
# - Input: "Test String" starting with "test"
# - Expected Output: False

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 7

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike