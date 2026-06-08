# Problem: Maximum 69 Number
# Link: https://leetcode.com/problems/maximum-69-number/
# Difficulty: Easy
# Problem Statement:
# You are given a positive integer num consisting only of digits 6 and 9.
#
# Return the maximum number you can get by changing at most one digit
# (6 becomes 9, and 9 becomes 6).
#
# Testcases:
# Example 1:
# Input: num = 9669
# Output: 9969
# Explanation:
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit results in 9666.
# The maximum number is 9969.
#
# Example 2:
# Input: num = 9996
# Output: 9999
#
# Example 3:
# Input: num = 9999
# Output: 9999
#
# Constraints:
# 1 <= num <= 10^4
# num consists of only 6 and 9 digits.

class Solution:
    def maximum69Number (self, num: int) -> int:
        maxx = num
        for i in range(len(str(num))):
            temp = list(str(num))

            if temp[i] == '6':
                temp[i] = '9'
            elif temp[i] == '9':
                temp[i] = '6'
            cur = int(''.join(temp))
            maxx = max(cur,maxx)
        return maxx
    
## Approach:
# 1. Convert the input number to a string to access each digit.
# 2. Iterate through each digit of the number.
# 3. For each digit, create a temporary list of characters from the string representation of the number.
# 4. If the current digit is '6', change it to '9'. If it's '9', change it to '6'.
# 5. Convert the modified list back to an integer and compare it with the current maximum value.
# 6. Update the maximum value if the modified number is greater.
# 7. After iterating through all digits, return the maximum value found.
# Time Complexity: O(n), where n is the number of digits in the input number.
# Space Complexity: O(n), as we are using a temporary list to store the digits.