# Prog10. title() makes all first letter of each word in the string, 
# capital letter. And all other letter in small case. Create a program 
# that do the same functionality without using title() function.

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program that implement a custom method to convert a string to title case/proper case.
# - Scope: A function that capitalizes first letter of each word.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Capitalize first letter of each word
#     - Convert other letters in the word to lowercase
#     - Handle strings with multiple words
#     - Cannot use built-in title() method

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Input the string with mixed case from the user
#     2. Split the string into words and iterate through each word
#        2.1. Capitalize the first character if it's a letter (A-z or a-z)
#        2.2. Convert the remaining characters to lowercase
#        2.3. Join the words back together with a space
#     3. Display the string in title case/proper case
# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Input the original string
text = input("Enter the string: ")

# Initialize an empty string to store the result
titled_words = []

# Split the text into words
word = ''

for char in text:
    if char == ' ':
        if word:
            # Convert the first letter to uppercase, rest to lowercase
            if 'a' <= word[0] <= 'z':
                first_char = chr(ord(word[0]) - 32)
            else:
                first_char = word[0]
            
            # Process remaining characters to lowercase
            remaining_chars = ''
            
            for i in range(1, len(word)):
                if 'A' <= word[i] <= 'Z':
                    remaining_chars += chr(ord(word[i]) + 32)
                else:
                    remaining_chars += word[i]
            
            titled_words.append(first_char + remaining_chars)
            word = ''
        titled_words.append(' ')
    else:
        word += char

# Handle the last word after the loop
if word:
    if 'a' <= word[0] <= 'z':
        first_char = chr(ord(word[0]) - 32)
    else:
        first_char = word[0]

    remaining_chars = ''

    for i in range(1, len(word)):
        if 'A' <= word[i] <= 'Z':
            remaining_chars += chr(ord(word[i]) + 32)
        else:
            remaining_chars += word[i]

    titled_words.append(first_char + remaining_chars)

# Join words into the final string
result = ''.join(titled_words)

print(f"Output: {result}")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1:
# - Input: "jUAn DEla CrUZ"
# - Expected Output: "Juan Dela Cruz"

# Test Case 2:
# - Input: "MIKE kaizen"
# - Expected Output: "Mike Kaizen"

# Test Case 3:
# - Input: "john mike P. aSUNCION"
# - Expected Output: "John Mike P. Asuncion"

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 6

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike