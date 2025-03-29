# Prog07. zfill() add zero characters at the beginning of the string to 
# complete the number of characters specifies in function parameter. 
# Create a program that do the same functionality without using 
# zfill() function.

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program that implement a custom method to add zeros at the beginning of a string.
# - Scope: A function that adds zeros to the left of a string.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Add zeros to the left of a string to reach specified length
#     - If the string starts with a sign (+ or -), place zeros after the sign
#     - If the string is already longer or equal to the width, return the original string
#     - Cannot use built-in zfill() method

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Input the original string and the desired width
#     2. Check if the string starts with a sign (+ or -)
#        2.1. If True, add zeros after the sign until the length matches the width
#        2.2. If False, return the original string
#     3. Display the n-digit string representation of the number

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Input the original string and desired width
text = input("Enter the original string: ")
width = int(input("Enter the desired width: "))

# Check if padding is needed
if len(text) >= width:
    result = text
else:
    # Check if the string starts with a sign
    if text and (text[0] == '+' or text[0] == '-'):
        # Place zeros after the sign
        result = text[0] + '0' * (width - len(text)) + text[1:]
    else:
        # Add zeros to the beginning
        result = '0' * (width - len(text)) + text

print(f"Output: {result}")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1:
# - Input: "143" with width 6
# - Expected Output: "000143"

# Test Case 2:
# - Input: "-42" with width 8
# - Expected Output: "-0000042"

# Test Case 3:
# - Input: "12345" with width 5
# - Expected Output: "12345"

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 7

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike