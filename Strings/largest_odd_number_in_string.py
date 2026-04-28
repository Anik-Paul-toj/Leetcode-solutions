# Problem: Largest Odd Number in String
# Link: https://leetcode.com/problems/largest-odd-number-in-string/
# Difficulty: Easy

# Problem Statement:
# You are given a string num representing a large integer.
# Return the largest-valued odd integer (as a string) that is a non-empty substring of num,
# or return an empty string "" if no odd integer exists.

# Testcases:
# Example 1:
# Input: num = "52"
# Output: "5"

# Example 2:
# Input: num = "4206"
# Output: ""

# Example 3:
# Input: num = "35427"
# Output: "35427"


## Approach:
    ## Brute:
        # Loop through the string from the end and check if the current character is odd
        # If it is, return the substring from the beginning to that character
        # Time complexity: O(n)
        # Space complexity: O(1)
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i+1]
        return ""
    