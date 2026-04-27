# Problem: Single Number
# Link: https://leetcode.com/problems/single-number/
# Difficulty: Easy

# Problem Statement:
# Given a non-empty array of integers nums, every element appears twice except for one.
# Find that single one.
# You must implement a solution with linear runtime complexity and constant extra space.

# Testcases:
# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1

# Approach:
 ## put the count of the numbers in a hashmap
 ## then if the value of the key is 1 then return the key

from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hm = defaultdict(int)
        for n in nums:
            hm[n] += 1
        for key, value in hm.items():
            if value == 1:
                return key