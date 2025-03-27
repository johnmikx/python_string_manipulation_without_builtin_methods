# Prog04. isupper() check if all characters of the string is on upper 
# case. Create a program that do the same functionality without using 
# isupper() function.

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program that implement a custom method to check if a string is entirely uppercase.
# - Scope: A function that determines if all alphabetic characters are uppercase.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Check if all alphabetic characters are uppercase
#     - Ignore non-alphabetic characters
#     - Return False if any alphabetic characters is not uppercase
#     - Cannot use built-in isupper() method

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Input a string to check from the user
#     2. Iterate through each character of the string
#        2.1. Skip non-alphabetic characters
#        2.2. If any alphabetic character is not uppercase, return False
#     3. Return True if all alphabetic characters are uppercase or if no alphabetic characters are found

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Input the string from the user
text = input("Enter a string to check: ")

# Flag to track if any alphabetic character is found
has_alphabetic = False

# Iterate through each character
for char in text:
    # Check if the character is an uppercase letter
    if ('A' <= char <= 'Z') or ('a' <= char <= 'z'):
        has_alphabetic = True
        # Check if the character is not uppercase
        if 'a' <= char <= 'z':
            result = False
            break
else:
    # If no lowercase alphabetic characters are found, set result to True
    result = has_alphabetic

print(f"Output: {result}")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1:
# - Input: "MIKE KAIZEN"
# - Expected Output: True

# Test Case 2:
# - Input: "HELLO WORLD!"
# - Expected Output: True

# Test Case 3:
# - Input: "Hello World"
# - Expected Output: False

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 6

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike