# Problem: Merge Strings Alternately
# Link: https://leetcode.com/problems/merge-strings-alternately/
# Difficulty: Easy

# Problem Statement:
# You are given two strings word1 and word2.
# Merge the strings by adding letters in alternating order, starting with word1.
# If one string is longer, append the remaining letters at the end.

# Testcases:
# Example 1:
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"

# Example 2:
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"

# Example 3:
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        for i in range(min(len(word1), len(word2))):
            ans += word1[i]
            ans+= word2[i]
        ans += word1[len(word2):]
        ans += word2[len(word1):]
        return ans
    
## Approach:
# We can solve this problem by iterating through both strings simultaneously and appending characters from each
# string to the result string in an alternating manner. We can use a loop that runs for the length of the shorter string, and in each iteration, we append one character from word1 and one character from word2 to the result string. After the loop, we can append any remaining characters from the longer string to the result string. Finally, we return the merged string.
# Time Complexity: O(n) where n is the length of the longer string, as we need to iterate through both strings once.
# Space Complexity: O(n) where n is the length of the merged string, as we      need to store the result string.