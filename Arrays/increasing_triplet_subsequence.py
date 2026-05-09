# Problem: Increasing Triplet Subsequence
# Link: https://leetcode.com/problems/increasing-triplet-subsequence/
# Difficulty: Medium

# Problem Statement:
# Given an integer array nums, return true if there exists
# a triplet (i, j, k) such that:
# i < j < k and nums[i] < nums[j] < nums[k].
# Otherwise, return false.

# Testcases:
# Example 1:
# Input: nums = [1,2,3,4,5]
# Output: true

# Example 2:
# Input: nums = [5,4,3,2,1]
# Output: false

# Example 3:
# Input: nums = [2,1,5,0,4,6]
# Output: true


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small = float('inf')
        mid =  float('inf')
        for i in range(len(nums)):
            if nums[i] <= small:
                small = nums[i]
            elif nums[i] <= mid:
                mid = nums[i]
            else:
                return True
        return False 

## Approach:
# We can keep track of the smallest and the middle element of the triplet.
# We can iterate through the array and update the smallest and middle element accordingly.
# If we find an element that is greater than the middle element, then we have found a triplet and we can return true.
# If we reach the end of the array and we haven't found a triplet, then we can return false.
# The time complexity of this approach is O(n) and the space complexity is O(1).