# Prog02. removeprefix() remove the characters at the beginning of the 
# string that matches the function parameter. Create a program that do 
# the same functionality without using removeprefix() function.

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program that implement a custom method to remove a specified prefix from a string.
# - Scope: A function that removes a given prefix manually.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Remove a specified prefix from the beginning of a string
#     - Work with prefixes of different lengths
#     - Return the original string if prefix doesn't match
#     - Cannot use built-in removeprefix() method

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Input the original string and the prefix to be removed
#     2. Compare the prefix with the starting characters of the string
#        2.1. If the characters match, extract the substring after the prefix
#        2.2. If the characters don't match, keep the original string
#     3. Display the string with the prefix removed (if applicable)

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Input the original string and prefix
original = input("Enter the original string: ")
prefix = input("Enter the prefix to remove: ")

# Check if the beginning of the string matches the prefix
match = True

for i in range(len(prefix)):
    if i >= len(original) or original[i] != prefix[i]:
        match = False
        break

# Remove the prefix if it matches
if match:
    result = original[len(prefix):]
else:
    result = original

print(f"Output: {result}")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1:
# - Input: "Juan Dela Cruz" with prefix "J"
# - Expected Output: "uan Dela Cruz"

# Test Case 2:
# - Input: "PascalCase" with prefix "Pascal"
# - Expected Output: "Case"

# Test Case 3:
# - Input: "John Mike P. Asuncion" with prefix "Mike"
# - Expected Output: "John Mike P. Asuncion"

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 6

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike