'''You are given an array of integers digits representing the digits of a positive integer. For example, digits = [1, 2, 3] represents the integer 123.

It is guaranteed that digits does not have any leading zeros.

Assuming that digits represents the integer n, your task is to return an array that represents the integer n + 1.

Example

For digits = [1, 2, 3], the output should be solution(digits) = [1, 2, 4];
For digits = [1, 2, 9], the output should be solution(digits) = [1, 3, 0];
For digits = [9, 9, 9], the output should be solution(digits) = [1, 0, 0, 0].
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer digits

An array with integer digits from 0 to 9.

Guaranteed constraints:
1 ≤ digits.length ≤ 104,
0 ≤ digits[i] ≤ 9.

[output] array.integer

Return an array that represents the digits of n + 1.
'''

def solution(digits):
    
    for i in range(len(digits)-1):
        if digits[i] == 9:
            for j in range(i, len(digits)):
                digits[j] = 0
            digits[i-1] += 1

    if digits[len(digits)-1] != 9:
        digits[len(digits)-1] += 1
    else:
        digits[len(digits)-1] = 0
        digits[0] += 1
        for i in range(1, len(digits)):
            digits[i] = 0

    return digits

print(solution([1,2,3,4,5,6]))
print(solution([1,2,3,4,5,9]))
print(solution([1,2,3,9,5,0]))
print(solution([1, 2, 9]))
print(solution([9,9,9]))



'''
To solve this problem, you need to simulate the addition of 1 to the number represented by the array digits. You can achieve this by iterating over the digits from the end to the beginning, handling the carry as needed.

Here’s a step-by-step approach:

Start from the last digit and add 1 to it.
If the result is less than 10, update the digit and return the result.
If the result is 10, set the current digit to 0 and carry over 1 to the next more significant digit.
Continue this process until you either run out of digits or there’s no carry left.
If you finish the loop with a carry, it means you need an additional digit at the beginning (e.g., incrementing 999 results in 1000).

def solution(digits):
    n = len(digits)
    
    # Start from the last digit and add 1
    for i in range(n-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    
    # If we exited the loop, it means we had a carry over the most significant digit
    return [1] + digits

# Example usage
print(solution([1, 2, 3]))  # Output: [1, 2, 4]
print(solution([1, 2, 9]))  # Output: [1, 3, 0]
print(solution([9, 9, 9]))  # Output: [1, 0, 0, 0]



Explanation:
Initialization: Determine the length of the digits array.
Iterate from the end: Start from the last digit and iterate backwards.
Addition and Carry Handling:
If the current digit is less than 9, increment it by 1 and return the digits array as the result.
If the current digit is 9, set it to 0 and continue to the next iteration to handle the carry.
Final Carry Check: If you finish the loop and all digits were 9 (causing a carry beyond the most significant digit), prepend 1 to the digits array.
This approach handles the problem efficiently and correctly, even for the largest possible inputs.




'''
