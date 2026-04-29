# Problem: Rotate String
# Link: https://leetcode.com/problems/rotate-string/
# Difficulty: Easy

# Problem Statement:
# Given two strings s and goal, return true if s can become goal
# after some number of shifts.
# A shift means moving the first character of s to the end.

# Testcases:
# Example 1:
# Input: s = "abcde", goal = "cdeab"
# Output: true

# Example 2:
# Input: s = "abcde", goal = "abced"
# Output: false

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # k = len(goal)
        s = list(s)
        goal = list(goal)
        for i in range(len(s)):
            s = s[-1:] + s[:-1]   # rotate by 1
            if s == goal:
                return True
        return False

## Approach:
# 1. Convert both strings to lists for easier manipulation.
# 2. Iterate through the string s, performing a rotation by moving the last character to the front.
# 3. After each rotation, check if the rotated string matches the goal string.
# 4. If a match is found, return True. If the loop completes without finding a match, return False.