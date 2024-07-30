'''
You are developing a new programming language and currently working on variable names. You have a list of words that you consider to be good and could be used for variable names. All the strings in words consist of lowercase English letters.

A complex variable name is a combination (possibly with repetitions) of some strings from words, written in CamelCase. In other words, all the strings are written without spaces and each string (with the possible exception of the first one) starts with a capital letter.

Your programming language should accept complex variable names only.

You need to check if the variableName is accepted by your programming language.

Example

For words = ["is", "valid", "right"] and variableName = "isValid", the output should be solution(words, variableName) = true.

As variableName consists of words "is" and "valid", and both of them are in words.

For words = ["is", "valid", "right"] and variableName = "IsValid", the output should be solution(words, variableName) = true.

Note that both variants: "IsValid" and "isValid" are valid in CamelCase.

For words = ["is", "valid", "right"] and variableName = "isValId", the output should be solution(words, variableName) = false.

variableName is separated to words "is", "val", "id", and not all words are in words.
'''




'''
To check if a variable name is accepted according to the rules of your programming language, we need to verify that the variable name can be decomposed into a sequence of words from the provided list, following CamelCase conventions. Here’s a step-by-step approach to implement this:

Initialize: Start with an empty word and iterate through each character in the variableName.
Construct Words: Accumulate characters to form words. When you encounter an uppercase letter (indicating the start of a new word in CamelCase), check if the accumulated word is in the list of allowed words. If it is, reset the accumulator for the next word.
Final Check: After the loop, check the last accumulated word.
Here’s the implementation in Python:


def solution(words, variableName):
    current_word = ""
    word_list = set(words)  # Convert the list to a set for O(1) lookups
    
    for char in variableName:
        if char.isupper():
            # If we hit an uppercase, we finish the current word
            if current_word and current_word not in word_list:
                return False
            current_word = char.lower()  # Start a new word
        else:
            current_word += char
    
    # Check the last accumulated word
    if current_word not in word_list:
        return False
    
    return True

# Example usage
words = ["is", "valid", "right"]
variableName1 = "isValid"
variableName2 = "IsValid"
variableName3 = "isValId"

print(solution(words, variableName1))  # Output: True
print(solution(words, variableName2))  # Output: True
print(solution(words, variableName3))  # Output: False







Explanation:
Set Conversion: Convert the list of words to a set for faster lookup.
Character Iteration: Loop through each character in variableName.
If the character is uppercase, it marks the beginning of a new word:
Check if the current_word (accumulated so far) is in word_list.
If it’s not, return False since it’s not a valid word.
Reset current_word to the lowercase version of the current character (starting a new word).
If the character is lowercase, add it to current_word.
Final Word Check: After the loop, ensure the last accumulated word is in the word_list.
This approach ensures that we correctly parse and validate CamelCase variable names against the provided list of words.


'''


