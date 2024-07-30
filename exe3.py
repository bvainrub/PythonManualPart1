'''
Avoid using built-in big integers to solve this challenge. Implement them yourself, since this is what you would be asked to do during a real interview.

Given two binary strings a and b, add them together and return the resulting string.

Example

For a = "1000" and b = "111", the output should be
solution(a, b) = "1111";
For a = "1" and b = "1", the output should be
solution(a, b) = "10".
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string a

A string that can contain only 0 and 1.

Guaranteed constraints:
0 ≤ a.length ≤ 105.

[input] string b

A string that can contain only 0 and 1.

Guaranteed constraints:
0 ≤ b.length ≤ 105.

[output] string

The result of adding strings a and b, without any leading zeros.
'''



'''
To implement a function that adds two binary strings without using Python's built-in integer handling for large numbers, you can manually perform the binary addition. This involves iterating through the strings from the end to the beginning, summing the corresponding bits, and handling the carry.

Here is a step-by-step implementation:

Initialize a result string and a carry variable.
Iterate through the strings from the end to the beginning.
Sum the corresponding bits and the carry.
Append the result bit to the result string and update the carry.
After the loop, if there is a carry left, append it to the result string.
Return the result string reversed (since we appended bits in reverse order).
Here's the implementation:


def solution(a: str, b: str) -> str:
    result = []
    carry = 0
    max_length = max(len(a), len(b))
    
    # Pad the shorter string with leading zeros
    a = a.zfill(max_length)
    b = b.zfill(max_length)
    
    # Iterate over the strings from the end to the beginning
    for i in range(max_length - 1, -1, -1):
        bit_a = int(a[i])
        bit_b = int(b[i])
        
        # Calculate the sum of bits and the carry
        total = bit_a + bit_b + carry
        result_bit = total % 2
        carry = total // 2
        
        # Append the result bit to the result list
        result.append(str(result_bit))
    
    # If there's a carry left, append it
    if carry:
        result.append('1')
    
    # Reverse the result list and join to form the final binary string
    return ''.join(result[::-1])

# Example usage
a = "1000"
b = "111"
print(solution(a, b))  # Output: "1111"

a = "1"
b = "1"
print(solution(a, b))  # Output: "10"




Explanation:
Initialization:

result: An empty list to store the result bits.
carry: A variable to store the carry during addition.
max_length: The maximum length of the two input strings.
Padding:

a.zfill(max_length): Pads the string a with leading zeros to make its length equal to max_length.
b.zfill(max_length): Pads the string b with leading zeros to make its length equal to max_length.
Iteration:

Iterate from the end to the beginning of the strings.
Convert the current characters to integers (bit_a and bit_b).
Calculate the sum of bit_a, bit_b, and carry.
Determine the result bit (result_bit) and the new carry.
Appending:

Append the result bit to the result list.
Handling the final carry:

If there is a carry left after the loop, append it to the result list.
Result formation:

Reverse the result list and join it to form the final binary string.





'''
