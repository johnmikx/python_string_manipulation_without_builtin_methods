# Prog05. endswith() check if the string end part matches the function 
# parameter. Create a program that do the same functionality without 
# using endswith() function.

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program that implement a custom method to check if a string ends with a specific substring.
# - Scope: A function that determines if a string ends with given characters.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Check if the string ends with a specified substring
#     - Work with different substring lengths
#     - Must be case-sensitive
#     - Cannot use built-in endswith() method

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Input the original string and the substring to check from the user
#     2. Compare the end of the string with the given substring
#        2.1. If the length of the substring is greater than the original string, return False
#        2.2. Manually compare each character from the end of the string
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
    # Compare characters from the end of the string
    result = True
    text_index = len(text) - len(substring)

    for i in range(len(substring)):
        if text[text_index + i] != substring[i]:
            result = False
            break

print(f"Output: {result}")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1:
# - Input: "Hello World" ending with "World"
# - Expected Output: True

# Test Case 2:
# - Input: "Python Programming" ending with "ming"
# - Expected Output: True

# Test Case 3:
# - Input: "Test String" ending with "string"
# - Expected Output: False

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 6

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike