# Problem: Split a String in Balanced Strings
# Link: https://leetcode.com/problems/split-a-string-in-balanced-strings/
# Difficulty: Easy
# Problem Statement:
# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
#
# Given a balanced string s, split it into some number of substrings such that:
#
# Each substring is balanced.
#
# Return the maximum number of balanced strings you can obtain.
#
# Testcases:
# Example 1:
# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation:
# s can be split into "RL", "RRLL", "RL", "RL",
# each substring contains same number of 'L' and 'R'.
#
# Example 2:
# Input: s = "RLRRRLLRLL"
# Output: 2
# Explanation:
# s can be split into "RL", "RRRLLRLL",
# each substring contains same number of 'L' and 'R'.
#
# Example 3:
# Input: s = "LLLLRRRR"
# Output: 1
# Explanation:
# s can be split into "LLLLRRRR".
#
# Constraints:
# 2 <= s.length <= 1000
# s[i] is either 'L' or 'R'.
# s is a balanced string.

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        count = 0
        for ch in s:
            if ch == 'R':
                balance +=1
            else:
                balance -=1
            if balance == 0:
                count +=1
        return count

## Approach:
# 1. Initialize a variable `balance` to keep track of the difference between the count of 'R' and 'L' characters, and a variable `count` to count the number of balanced substrings.
# 2. Iterate through each character in the input string `s`.
# 3. For each character, update the `balance` variable: increment it for 'R' and decrement it for 'L'.
# 4. Whenever `balance` becomes zero, it means we have found a balanced substring, so we increment the `count` variable.
# 5. After iterating through the entire string, return the `count` variable as the result.
# Time Complexity: O(n), where n is the length of the input string `s`.
# Space Complexity: O(1), as we are using only a constant amount of extra space for the counters.
