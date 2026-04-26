# Problem: Check if Array Is Sorted and Rotated
# Link: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
# Difficulty: Easy

# Problem Statement:
# Given an array nums, return true if the array was originally sorted in non-decreasing order,
# then rotated some number of positions (including zero). Otherwise, return false.
# There may be duplicates in the original array.

# Testcases:
# Example 1:
# Input: nums = [3,4,5,1,2]
# Output: true

# Example 2:
# Input: nums = [2,1,3,4]
# Output: false

# Example 3:
# Input: nums = [1,2,3]
# Output: true

# approach:
 ## suppose we have an array [3,4,5,1,2]
 ## so we will keep track on count of how many times the current element is greater than the next element
 ## so if the nums[prev] > nums[curr] then we will increase the count by 1
 ## the if the count is <= 1 then we will return True
 ## otherwise we will return False
 
class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        for i in range(n):
            prev = (i-1) % n
            curr = i
            if nums[prev] > nums[curr]:
                count += 1
        return count <= 1
