 # Problem: Find All Numbers Disappeared in an Array
# Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Difficulty: Easy

# Problem Statement:
# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in nums.

# Testcases:
# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

# Example 2:
# Input: nums = [1,1]
# Output: [2]

# Approach:
 ## my approach was to convert into set to remove the duplicates and the check 
    ## for the numbers from 1 to n and if they are not in the set then add them to the result list
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        set_num = set(nums)
        
        for i in range(1, len(nums)+1):
            if i not in set_num:
                res.append(i)
        return res
