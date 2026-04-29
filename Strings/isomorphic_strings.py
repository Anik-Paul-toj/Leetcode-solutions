# Problem: Isomorphic Strings
# Link: https://leetcode.com/problems/isomorphic-strings/
# Difficulty: Easy

# Problem Statement:
# Given two strings s and t, determine if they are isomorphic.
# Characters in s can be replaced to get t while preserving order.
# No two characters may map to the same character.

# Testcases:
# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# Example 2:
# Input: s = "f11", t = "b23"
# Output: false

# Example 3:
# Input: s = "paper", t = "title"
# Output: true

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st ={}
        ts ={}

        for c1,c2 in zip(s,t):
            if c1 in st and st[c1] != c2:
                return False
            if c2 in ts and ts[c2] != c1:
                return False
            st[c1] = c2
            ts[c2] = c1
            # print(st)
            # print(ts)
        return True

## Approach:
 ## Bijection Mapping:
# 1. Create two hash maps (dictionaries) to store the mapping of characters in string s to characters in string t and vice versa.
# 2. Iterate through both strings simultaneously, checking the mapping for each character.
# 3. If a character in s has already been mapped to a different character in t, or if a character in t has already been mapped to a different character in s, return False.
# 4. If the mapping is consistent throughout the strings, return True at the end.