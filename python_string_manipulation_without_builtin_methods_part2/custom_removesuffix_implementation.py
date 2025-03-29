# Prog02. removesuffix() remove the characters at the end of the string 
# that matches the function parameter. Create a program that do the 
# same functionality without using removesuffix() function.

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program that implement a custom method to remove a specified suffix from a string.
# - Scope: A function that removes a given suffix manually.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Remove a specified suffix from the ending of a string
#     - Work with suffixes of different lengths
#     - Return the original string if suffix doesn't match
#     - Cannot use built-in removesuffix() method

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Input the original string and the suffix to be removed
#     2. Check if the string ends with the given suffix
#        2.1. If the characters match, return the string with suffix removed
#        2.2. If the characters don't match, keep the original string
#     3. Display the string with the suffix removed (if applicable)

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Input the original string and suffix
original = input("Enter the original string: ")
suffix = input("Enter the suffix to remove: ")

# Check if the string ends with the suffix
if len(suffix) <= len(original):
    match = True
    for i in range(len(suffix)):
        if original[len(original) - len(suffix) + i] != suffix[i]:
            match = False
            break

    # Remove suffix if it matches
    if match:
        result = original[:len(original) - len(suffix)]
    else:
        result = original

print(f"Output: {result}")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1:
# - Input: "Juan Dela Cruz" with suffix "z"
# - Expected Output: "Juan Dela Cru"

# Test Case 2:
# - Input: "PascalCase" with suffix "Case"
# - Expected Output: "Pascal"

# Test Case 3:
# - Input: "John Mike P. Asuncion" with suffix "Asuncion"
# - Expected Output: "John Mike P. "

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 7

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike