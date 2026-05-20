# Problem: Find Pivot Index
# Link: https://leetcode.com/problems/find-pivot-index/
# Difficulty: Easy
# Problem Statement:
# Given an array of integers nums, calculate the pivot index of this array.
#
# The pivot index is the index where the sum of all the numbers strictly to the left
# of the index is equal to the sum of all the numbers strictly to the index's right.
#
# If the index is on the left edge of the array, then the left sum is 0 because there
# are no elements to the left. This also applies to the right edge of the array.
#
# Return the leftmost pivot index. If no such index exists, return -1.
#
# Testcases:
# Example 1:
# Input: nums = [1,7,3,6,5,6]
# Output: 3
#
# Example 2:
# Input: nums = [1,2,3]
# Output: -1
#
# Example 3:
# Input: nums = [2,1,-1]
# Output: 0
#
# Constraints:
# 1 <= nums.length <= 10^4
# -1000 <= nums[i] <= 1000

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        j = len(nums) - 1
        preSum = [0] * len(nums)
        sufSum = [0] * len(nums)
        for n in range(1, len(nums)):
            preSum[n] = preSum[n - 1] + nums[n - 1]
        print(preSum)
        sufSum[j] = 0  # base case
        for n in range(j - 1, -1, -1):
            sufSum[n] = sufSum[n + 1] + nums[n + 1]
        print(sufSum)
        for i in range(len(preSum)):
            if preSum[i] == sufSum[i]:
                return i
        return -1
    
## Approach:
# 1. We can use two arrays to store the prefix sum and suffix sum of the input array.
# 2. We can then iterate through the prefix sum and suffix sum arrays and check if they are equal at any index.
# 3. If we find such an index, we can return it as the pivot index.
# 4. If we do not find any such index, we can return -1.
# Time Complexity: O(n) where n is the length of the input array.
# Space Complexity: O(n) where n is the length of the input array.

# Note: We can also solve this problem using a single pass approach by keeping track of the total sum of the array and the left sum while iterating through the array. However, the above approach is more intuitive and easier to understand.
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            if left_sum == total_sum - left_sum - nums[i]:
                return i
            left_sum += nums[i]
        return -1
## Approach:
# 1. We can keep track of the total sum of the array and the left sum while iterating through the array.
# 2. At each index, we can check if the left sum is equal to the  total sum minus the left sum minus the current element.
# 3. If we find such an index, we can return it as the pivot index.
# 4. If we do not find any such index, we can return -1.
# Time Complexity: O(n) where n is the length of the input array.
# Space Complexity: O(1) as we are using only a constant amount of extra space