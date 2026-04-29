# Problem: Word Pattern
# Link: https://leetcode.com/problems/word-pattern/
# Difficulty: Easy

# Problem Statement:
# Given a pattern and a string s, check if s follows the same pattern.
# There must be a bijection between pattern characters and words in s.
# Each character maps to exactly one unique word and vice versa.

# Testcases:
# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true

# Example 2:
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false

# Example 3:
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false

## Approach:
# 1. Create two hash maps (dictionaries) to store the mapping of characters in the pattern to words in the string and vice versa.
# 2. Split the string into words and compare the lengths of the pattern and the words. If they don't match, return False.
# 3. Iterate through the words and the pattern simultaneously, updating the hash maps with the current word and character's index.
# 4. After processing all characters, compare the values of the two hash maps. If they are the same, return True; otherwise, return False.

from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hms = defaultdict(list)
        hmp = defaultdict(list)
        arrs = s.split()
        arrp = list(pattern)
        if len(arrs) != len(arrp):
            return False
        for i,ch in enumerate(arrs):
            hms[ch].append(i)
        for i,ch in enumerate(arrp):
            hmp[ch].append(i)
        return sorted(hmp.values())==sorted(hms.values())