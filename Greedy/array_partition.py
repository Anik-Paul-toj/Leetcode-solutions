# Problem: Array Partition
# Link: https://leetcode.com/problems/array-partition/
# Difficulty: Easy
# Problem Statement:
# Given an integer array nums of 2n integers, group these integers into
# n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of
# min(ai, bi) for all i is maximized.
#
# Return the maximized sum.
#
# Testcases:
# Example 1:
# Input: nums = [1,4,3,2]
# Output: 4
# Explanation:
# The optimal pairing is (1,2), (3,4).
# min(1,2) + min(3,4) = 1 + 3 = 4.
#
# Example 2:
# Input: nums = [6,2,6,5,1,2]
# Output: 9
# Explanation:
# The optimal pairing is (1,2), (2,5), (6,6).
# min(1,2) + min(2,5) + min(6,6) = 1 + 2 + 6 = 9.
#
# Constraints:
# 1 <= n <= 10^4
# nums.length == 2 * n
# -10^4 <= nums[i] <= 10^4

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        s = 0
        for i in range(0,len(nums),2):
            s += nums[i]
        return s
# approach:
# 1. Sort the input array.
# 2. Iterate through the sorted array with a step of 2, summing up the elements at even indices.
# 3. Return the computed sum as the result.
# Time Complexity: O(n log n) due to sorting the array.
# Space Complexity: O(1) if we ignore the space used for sorting, otherwise O(n) due to the sorting algorithm.