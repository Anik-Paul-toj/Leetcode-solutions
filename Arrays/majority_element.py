# Problem: Majority Element
# Link: https://leetcode.com/problems/majority-element/
# Difficulty: Easy

# Problem Statement:
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

# Testcases:
# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# Approach:
    ## we can use a hashmap to count the frequency of each element and return the one with frequency greater than n/2
    ## we can also sort the array and return the middle element as it will be the majority element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import defaultdict
        max_freq = 0
        result = None
        hm = defaultdict(int)
        for n in nums:
            hm[n] += 1
        for key, value in hm.items():
            if value > max_freq:
                max_freq = value
                result = key
        return result