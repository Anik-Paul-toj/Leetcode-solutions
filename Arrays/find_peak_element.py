# Problem: Find Peak Element
# Link: https://leetcode.com/problems/find-peak-element/
# Difficulty: Medium

# Problem Statement:
# A peak element is an element that is strictly greater than its neighbors.
# Given an array nums, return the index of any peak element.
# You may assume nums[-1] = nums[n] = -∞.
# You must write an algorithm with O(log n) time complexity.

# Testcases:
# Example 1:
# Input: nums = [1,2,3,1]
# Output: 2

# Example 2:
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5

## Approach:
    ## Brute:
        # Loop through the array and check if the current element is greater than its neighbors
        # If it is, return the index of that element
        # Time complexity: O(n)
        # Space complexity: O(1)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if (i==0 or nums[i -1]<nums[i]) and (i==len(nums)-1 or nums[i]>nums[i+1]):  ## considering that nums[-1] and nums[n] are -∞
                return i                                                                ## thats why we are checking for i==0 and i==len(nums)-1 to avoid index out of range error
            
    ## Optimal:
    