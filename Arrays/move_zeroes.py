# Problem: Move Zeroes
# Link: https://leetcode.com/problems/move-zeroes/
# Difficulty: Easy

# Problem Statement:
# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.
# You must do this in-place without making a copy of the array.

# Testcases:
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

# approach:
 ## ekta j = 0 pointer nebp
 ## eibar check korbo nums[i] == 0 kina
   ## jodi nums[i] != 0 hoy tahole nums[j] = nums[i] korbo
    ## eibar j ke increase korbo
 ## sese jei jayga gulo faka thakbe as uporer jonno skip korte korte last e faka space thakbe sekhane 0 bosiye debo

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0  # position for next non-zero
        
        # move non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        
        # fill remaining with zeros
        for i in range(j, len(nums)):
            nums[i] = 0