# Prog07. center() add space characters at the beginning and at the end 
# of the string to print the string at the center. Create a program 
# that do the same functionality without using center() function.

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program that implement a custom method to center a string with padding.
# - Scope: A function that adds spaces to both sides of a string.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Add spaces to both left and right sides of a string
#     - Center the original string within specified width
#     - Handle odd and even width scenarios
#     - Cannot use built-in center() method

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Input the original string and total width from the user
#     2. Check if the length of the string is greater than or equal to the width
#        2.1. If True, return the original string
#        2.2. Otherwise:
#           2.2.1. Calculate the total padding required
#           2.2.2. Split the padding into left and right
#           2.2.3. If the padding is odd, add one extra space to the left
#     3. Display the manually padded centered string

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Input the original string and width
text = input("Enter the original string: ")
width = int(input("Enter the total width: "))

# Check if the string is already longer or equal to the width
if len(text) >= width:
    result = text
else:
    # Calculate total padding needed
    total_padding = width - len(text)
    
    # Calculate left and right padding
    left_padding = total_padding // 2
    right_padding = total_padding - left_padding

    # Create manually centered string with spaces
    result = ' ' * left_padding + text + ' ' * right_padding

print(f"Output: {result}")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1:
# - Input: "Hello" with width 11
# - Expected Output: "   Hello   " (3 spaces left, 3 spaces right)

# Test Case 2:
# - Input: "Python" with width 10
# - Expected Output: "  Python  " (2 spaces left, 2 spaces right)

# Test Case 3:
# - Input: "Programming" with width 8
# - Expected Output: "Programming" (no spaces added since it reached its desired width)

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 6

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike