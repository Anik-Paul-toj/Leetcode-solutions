# Problem: Largest Number
# Link: https://leetcode.com/problems/largest-number/
# Difficulty: Medium

# Problem Statement:
# Given a list of non-negative integers nums, arrange them such that they form the largest number.
# Since the result may be very large, return it as a string.

# Testcases:
# Example 1:
# Input: nums = [10,2]
# Output: "210"

# Example 2:
# Input: nums = [3,30,34,5,9]
# Output: "9534330"

## Approach 
# 1. Convert all integers to strings for easy comparison.
# 2. Sort the list of strings based on a custom comparison function that compares the 
#       concatenation of two strings in both possible orders (e.g., "30" + "3" vs "3" + "30").
# 3. Join the sorted list of strings to form the largest number.
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i,n in enumerate(nums):
            nums[i] = str(n)
        print(nums)

        def com(n1,n2):
            return n1+n2 > n2+n1

        n = len(nums)
        for i in range(n):
            for j in range(n - 1):
                if not com(nums[j], nums[j + 1]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        result = ''.join(nums)
        if result[0] == '0':
            return '0'
        else:
            return result
