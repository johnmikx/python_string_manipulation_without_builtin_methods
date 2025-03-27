# Prog06. ljust() add space characters at the end of the string to 
# complete the number of characters specifies in function parameter. 
# Create a program that do the same functionality without using 
# ljust() function.

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program that implement a custom method to left-justify a string with padding.
# - Scope: A function that adds spaces to the right of a string.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Add spaces to the right of a string to reach specified length
#     - Work with strings shorter and longer than specified length
#     - Use space as default padding character
#     - Cannot use built-in ljust() method

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Input the original string and the desired width
#     2. Check if the string length is less than the specified with
#        2.1. If True, add spaces to the right until the length matches the width
#        2.2. If False, return the original string
#     3. Display the left-justified string with padding if necessary

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Input the original string and desired width
text = input("Enter the original string: ")
width = int(input("Enter the desired width: "))

# Check if the string length is less than the specified width
if len(text) >= width:
    result = text
else:
    # Add spaces to reach the specified width
    result = text + ' ' * (width - len(text))

print(f"Output: {result}")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1:
# - Input: "Hello" with width 10
# - Expected Output: "Hello     " (5 spaces added)

# Test Case 2:
# - Input: "Python" with width 8
# - Expected Output: "Python  " (2 spaces added)

# Test Case 3:
# - Input: "Programming" with width 5
# - Expected Output: "Programming" (no spaces added since it reached its desired width)

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 6

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike