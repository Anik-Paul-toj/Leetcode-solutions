# Problem: Determine if Two Strings Are Close
# Link: https://leetcode.com/problems/determine-if-two-strings-are-close/
# Difficulty: Medium
# Problem Statement:
# Two strings are considered close if you can attain one from the other using the following operations:
#
# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
#
# Operation 2: Transform every occurrence of one existing character into another existing character,
# and do the same with the other character.
# For example, aacabb -> bbcbaa
#
# You can use the operations on either string as many times as necessary.
#
# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
#
# Testcases:
# Example 1:
# Input: word1 = "abc", word2 = "bca"
# Output: true
#
# Example 2:
# Input: word1 = "a", word2 = "aa"
# Output: false
#
# Example 3:
# Input: word1 = "cabbba", word2 = "abbccc"
# Output: true
#
# Constraints:
# 1 <= word1.length, word2.length <= 10^5
# word1 and word2 contain only lowercase English letters.

from collections import defaultdict
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        hm1 = defaultdict(int)
        hm2 = defaultdict(int)
        for ch in word1:
            hm1[ch] += 1
        for ch in word2:
            hm2[ch] += 1
        return sorted(hm2.values()) == sorted(hm1.values()) and set(hm1.keys()) == set(hm2.keys())
        # print(hm1)
        
## Approach:
# 1. Create two hashmaps to store the frequency of each character in word1 and word2.
# 2. Check if the sorted list of values (frequencies) in both hash  maps are the same and if the set of keys (characters) in both hashmaps are the same. If both conditions are true, return true. Otherwise, return false.
# 3. The time complexity of this approach is O(n log n) due to the sorting of the frequency values, where n is the number of unique characters in the strings. The space complexity is O(n) due to the hashmaps storing the frequency of each character.
    