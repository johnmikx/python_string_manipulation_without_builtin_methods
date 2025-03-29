# Prog03. upper() converts all characters of the string into upper case.
# Create a program that do the same functionality without using 
# upper() function.

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program that implement a custom method to convert a string to uppercase.
# - Scope: A function that converts all characters to uppercase manually.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Convert all lowercase characters to uppercase
#     - Preserve non-alphabetic characters
#     - Work with mixed-case strings
#     - Cannot use built-in upper() method

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Input a string in mixed case from the user
#     2. Iterate through each character of the string
#        2.1. If the character is a lowercase letter, convert it to uppercase by subtracting 32 to its ASCII value
#        2.2. If the character is not lowercase, keep it unchanged
#     3. Display the uppercase version of the string

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Input the string from the user
text = input("Enter a string with mixed case: ")

# Empty string to store the uppercase result
uppercase = ''

# Iterate through each character
for char in text:
    # Check if the character is a lowercase letter
    if 'a' <= char <= 'z':
        # Convert to uppercase by subtracting 32 to ASCII value
        uppercase += chr(ord(char) - 32)
    else:
        # Keep non-uppercase characters unchanged
        uppercase += char

print(f"Output: {uppercase}")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1:
# - Input: "Juan Dela Cruz"
# - Expected Output: "JUAN DELA CRUZ"

# Test Case 2:
# - Input: "mike kaizen"
# - Expected Output: "MIKE KAIZEN"

# Test Case 3:
# - Input: "John Mike P. Asuncion"
# - Expected Output: "JOHN MIKE P. ASUNCION"

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 7

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike