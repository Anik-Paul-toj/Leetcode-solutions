# Problem: Sort Characters By Frequency
# Link: https://leetcode.com/problems/sort-characters-by-frequency/
# Difficulty: Medium

# Problem Statement:
# Given a string s, sort it in decreasing order based on the frequency of characters.
# Characters with higher frequency should come first.
# Same characters must be grouped together.

# Testcases:
# Example 1:
# Input: s = "tree"
# Output: "eert"

# Example 2:
# Input: s = "cccaaa"
# Output: "aaaccc"

# Example 3:
# Input: s = "Aabb"
# Output: "bbAa"

class Solution:
    def frequencySort(self, s: str) -> str:      
        freq = Counter(s)
        res = ""
        print(freq.most_common())
        for ch, count in freq.most_common():
            res += ch * count
        return res
## Approach:
# 1. Use a hash map (dictionary) to count the frequency of each character in the input string s.
# 2. Sort the characters based on their frequency in decreasing order using the most_common() method of the Counter class.
# 3. Build the resulting string by repeating each character according to its frequency and concatenating them together.