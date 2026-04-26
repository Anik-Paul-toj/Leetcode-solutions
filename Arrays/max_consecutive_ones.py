# Problem: Max Consecutive Ones
# Link: https://leetcode.com/problems/max-consecutive-ones/
# Difficulty: Easy

# Problem Statement:
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Testcases:
# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 3

# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 2

# approach:
    ## we will keep track of the count of consecutive 1's and the maximum count
    ## if we encounter a 1 then we will increase the count by 1
    ## if we encounter a 0 then we will update the maximum count and reset the count to 0
    ## at the end we will return the maximum count
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        c = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                c += 1
                ans = max(ans, c)
            else:
                c = 0
        return ans

