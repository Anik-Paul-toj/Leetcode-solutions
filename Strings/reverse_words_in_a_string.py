# Problem: Reverse Words in a String
# Link: https://leetcode.com/problems/reverse-words-in-a-string/
# Difficulty: Medium

# Problem Statement:
# Given a string s, reverse the order of words.
# Words are separated by spaces.
# Remove extra spaces and return words separated by a single space.

# Testcases:
# Example 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"

# Example 2:
# Input: s = "  hello world  "
# Output: "world hello"

# Example 3:
# Input: s = "a good   example"
# Output: "example good a"

class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        return (' '.join(l[::-1]))

## Approach:
    # 1. Split the input string s into a list of words using the split() method, which automatically handles multiple spaces and removes leading/trailing spaces.
    
    