# Problem: Maximum Subarray
# Link: https://leetcode.com/problems/maximum-subarray/
# Difficulty: Medium

# Problem Statement:
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Testcases:
# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6

# Example 2:
# Input: nums = [1]
# Output: 1

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23

## Approach:
# We can use Kadane's algorithm to solve this problem in O(n) time complexity.
# We will keep track of the current sum and the maximum sum found so far. If the current sum becomes negative, we will reset it to 0.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            # print(summ)
            if summ > maxi:
                maxi = summ
            if summ < 0:
                summ = 0
        return maxi