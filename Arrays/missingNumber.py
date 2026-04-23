# Problem: Missing Number
# Link: https://leetcode.com/problems/missing-number/
# Difficulty: Easy


# Problem Statement:
# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.

# Testcases:
# Example 1:
# Input: nums = [3,0,1]
# Output: 2

# Example 2:
# Input: nums = [0,1]
# Output: 2

# Example 3:
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8

# approach:
# so like we can add the total from the given array and then we can add the total from the range of 0 to n and then we can subtract the total of the given array from the total of the range and we will get the missing number.

## If nums = [3,0,1], then:
    # so the numbers should be 0, 1, 2, 3   (n = 3)
## sum(range(len(nums)+1))
    # sum(range(4)) → 0 + 1 + 2 + 3 = 6
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums)+1)) -sum(nums)