# Problem: Valid Anagram
# Link: https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy

# Problem Statement:
# Given two strings s and t, return true if t is an anagram of s,
# and false otherwise.

# Testcases:
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hs = defaultdict(int)
        s = list(s)
        for ch in s:
            hs[ch] +=1
        # print(ht)

        ht = defaultdict(int)
        t = list(t)
        for ch in t:
            ht[ch] +=1
        return ht==hs
    
## Approach:
# 1. Create two hash maps (dictionaries) to count the frequency of each character
#    in both strings s and t.
# 2. Iterate through each character in string s and update the count in the first hash map.
# 3. Iterate through each character in string t and update the count in the second hash map.
# 4. Finally, compare the two hash maps. If they are equal, return True; otherwise, return False.