# Problem: Find First and Last Position of Element in Sorted Array
# Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Difficulty: Medium

# Problem Statement:
# Given an array of integers nums sorted in non-decreasing order,
# find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

# Testcases:
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]

# Approach:
 ## 
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = []
        for i in range(len(nums)):
            if nums[i] == target:
                n.append(i)

        if not n:
            return [-1, -1]
        return [n[0], n[-1]]
        