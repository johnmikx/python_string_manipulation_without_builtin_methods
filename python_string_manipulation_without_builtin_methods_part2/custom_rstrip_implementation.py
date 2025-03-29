# Prog01. rstrip() remove the space characters at the end of the string.
# Create a program that do the same functionality without using 
# rstrip() function.

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program that implement a custom method to remove trailing spaces from a string.
# - Scope: A function that removes spaces at the ending of a string manually.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Remove all consecutive space characters from the ending of a string
#     - Work with strings containing multiple trailing spaces
#     - Preserve the original text content includng the internal spaces
#     - Cannot use built-in rstrip() method

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Input a string with potential trailing spaces
#     2. Iterate from the end of the string to find the last non-space character
#        2.1. Extract the substring from the beginning to the last non-space character
#     3. Display the string without trailing spaces

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Ask the user for input
text = input("Enter a string with trailing spaces: ")

# Initialize index to the last character
i = len(text) - 1

# Find the last non-space character
while i >= 0 and text[i] == ' ':
    i -= 1

# Extract substring without trailing spaces
result = text[:i + 1]
print(f"Output: {result}")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1:
# - Input: "Juan Dela Cruz      "
# - Expected Output: "Juan Dela Cruz"

# Test Case 2:
# - Input: "Hello World!    "
# - Expected Output: "Hello World!"

# Test Case 3:
# - Input: "No Trailing Spaces"
# - Expected Output: "No Trailing Spaces"

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 7

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike