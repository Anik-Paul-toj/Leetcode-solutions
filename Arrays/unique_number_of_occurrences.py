# Problem: Unique Number of Occurrences
# Link: https://leetcode.com/problems/unique-number-of-occurrences/
# Difficulty: Easy
# Problem Statement:
# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
#
# Testcases:
# Example 1:
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
#
# Example 2:
# Input: arr = [1,2]
# Output: false
#
# Example 3:
# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true
#
# Constraints:
# 1 <= arr.length <= 1000
# -1000 <= arr[i] <= 1000

from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hm = defaultdict(int)
        for n in arr:
            hm[n] +=1
        print(hm)
        return len(hm.values()) == len(set(hm.values()))
    
## Approach:
# 1. Create a hashmap to store the frequency of each element in the array.
# 2. Iterate through the hashmap values and check if the length of the values is equal to the length of the set of values. If they are equal, it means that all occurrences are unique, so return true. Otherwise, return false.
# 3. The time complexity of this approach is O(n) where n is the length of the input array, and the space complexity is O(n) due to the hashmap storing the frequency of each element.

