# Prog08/Prog09. swapcase() reverse the casing of each of the character 
# of the string. Create a program that do the same functionality 
# without using swapcase() function.

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program that implement a custom method to reverse character casing.
# - Scope: A function that swaps uppercase to lowercase and lowercase to uppercase.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Swap case of each alphabetic character
#     - Uppercase becomes lowercase and vice versa
#     - Non-alphabetic characters remain unchanged
#     - Cannot use built-in swapcase() method

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Input the string with mixed case from the user
#     2. Iterate through each character
#        2.1. If the character is an uppercase letter (A-Z), convert it to lowercase.
#        2.2. If the character is a lowercase letter (a-z), convert it to uppercase.
#        2.3. Leave non-alphabetic characters unchanged
#     3. Display the string with swapped character cases
# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Input the original string
text = input("Enter the string with mixed case: ")

# Initialize an empty string for swapped case
swapped = ''

# Iterate through each character in the string
for char in text:
    # Check if character is uppercase (A-Z)
    if 'A' <= char <= 'Z':
        # Convert to lowercase by adding 32 to ASCII value
        swapped += chr(ord(char) + 32)
    # Check if character is lowercase (a-z)
    elif 'a' <= char <= 'z':
        # Convert to uppercase by subtracting 32 from ASCII value
        swapped += chr(ord(char) - 32)
    else:
        # Leave non-alphabetic characters unchanged
        swapped += char

print(f"Output: {swapped}")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1:
# - Input: "jUAn DEla CrUZ"
# - Expected Output: "JuaN deLA cRuz"

# Test Case 2:
# - Input: "MIKE kaizen"
# - Expected Output: "mike KAIZEN"

# Test Case 3:
# - Input: "John Mike P. Asuncion"
# - Expected Output: "john mike P. aSUNCION"

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 6

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike