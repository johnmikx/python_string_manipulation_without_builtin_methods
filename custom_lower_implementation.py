# Prog03. lower() converts all characters of the string into lower case.
# Create a program that do the same functionality without using 
# lower() function.

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program that implement a custom method to convert a string to lowercase.
# - Scope: A function that converts all characters to lowercase manually.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Convert all uppercase characters to lowercase
#     - Preserve non-alphabetic characters
#     - Work with mixed-case strings
#     - Cannot use built-in lower() method

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Input a string in mixed case from the user
#     2. Iterate through each character of the string
#        2.1. If the character is an uppercase letter, convert it to lowercase by adding 32 to its ASCII value
#        2.2. If the character is not uppercase, keep it unchanged
#     3. Display the lowercase version of the string

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Input the string from the user
text = input("Enter a string with mixed case: ")

# Empty string to store the lowercase result
lowercase = ''

# Iterate through each character
for char in text:
    # Check if the character is an uppercase letter
    if 'A' <= char <= 'Z':
        # Convert to lowercase by adding 32 to ASCII value
        lowercase += chr(ord(char) + 32)
    else:
        # Keep non-uppercase characters unchanged
        lowercase += char

print(f"Output: {lowercase}")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1:
# - Input: "Juan Dela Cruz"
# - Expected Output: "juan dela cruz"

# Test Case 2:
# - Input: "MIKE KAIZEN"
# - Expected Output: "mike kaizen"

# Test Case 3:
# - Input: "John Mike P. Asuncion"
# - Expected Output: "john mike p. asuncion"

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 6

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike