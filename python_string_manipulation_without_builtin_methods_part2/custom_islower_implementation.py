# Prog04. islower() check if all characters of the string is on lower 
# case. Create a program that do the same functionality without using 
# islower() function.

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program that implement a custom method to check if a string is entirely lowercase.
# - Scope: A function that determines if all alphabetic characters are lowercase.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Check if all alphabetic characters are lowercase
#     - Ignore non-alphabetic characters
#     - Return False if any alphabetic characters is not lowercase
#     - Cannot use built-in islower() method

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Input a string to check from the user
#     2. Iterate through each character of the string
#        2.1. Skip non-alphabetic characters
#        2.2. If any alphabetic character is not lowercase, return False
#     3. Return True if all alphabetic characters are lowercase or if no alphabetic characters are found

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Input the string from the user
text = input("Enter a string to check: ")

# Flag to track if any alphabetic character is found
has_alphabetic = False

# Iterate through each character
for char in text:
    # Check if the character is a lowercase letter
    if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
        has_alphabetic = True
        # Check if the character is not lowercase
        if 'A' <= char <= 'Z':
            result = False
            break
else:
    # If no uppercase alphabetic characters are found, set result to True
    result = has_alphabetic

print(f"Output: {result}")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1:
# - Input: "mike kaizen"
# - Expected Output: True

# Test Case 2:
# - Input: "hello world!"
# - Expected Output: True

# Test Case 3:
# - Input: "Hello World"
# - Expected Output: False

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 7

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike