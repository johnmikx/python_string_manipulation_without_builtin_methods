# Prog01. lstrip() remove the space characters at the beginning of the 
# string. Create a program that do the same functionality without 
# using lstrip() function.

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program that implement a custom method to remove leading spaces from a string.
# - Scope: A function that removes spaces at the beginning of a string manually.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Remove all consecutive space characters from the beginning of a string
#     - Work with strings containing multipe leading spaces
#     - Preserve the original text content includng the internal spaces
#     - Cannot use built-in lstrip() method

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Input a string with potential leading spaces
#     2. Iterate through the string to find the first non-space character
#        2.1. Extract the substring starting from the first non-space character
#     3. Display the string without leading spaces

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Ask the user for input
text = input("Enter a string with leading spaces: ")

# Initialize
i = 0

# Remove leading spaces manually
while i < len(text) and text [i] == ' ':
    i += 1

# Get the result without leading spaces
result = text[i:]
print(f"Output: {result}")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1:
# - Input: "    Juan Dela Cruz"
# - Expected Output: "Juan Dela Cruz"

# Test Case 2:
# - Input: "Hello World!"
# - Expected Output: "Hello World!"

# Test Case 3:
# - Input: "        John Mike P. Asuncion"
# - Expected Output: "John Mike P. Asuncion"

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 6

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike