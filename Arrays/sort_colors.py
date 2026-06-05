# Problem: Sort Colors
# Link: https://leetcode.com/problems/sort-colors/
# Difficulty: Medium
# Problem Statement:
# Given an array nums with n objects colored red, white, or blue, sort them in-place
# so that objects of the same color are adjacent, with the colors in the order
# red, white, and blue.
#
# We will use the integers 0, 1, and 2 to represent the color red, white,
# and blue, respectively.
#
# You must solve this problem without using the library's sort function.
#
# Testcases:
# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
#
# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]
#
# Constraints:
# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
#
# Follow up:
# Could you come up with a one-pass algorithm using only constant extra space?


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0,c1,c2 = 0,0,0
        for i in range(len(nums)):
            if nums[i] == 0:
                c0+=1
            elif nums[i] ==1:
                c1+=1
            else:
                c2 +=1
        idx = 0
        for i in range(c0):
            nums[idx] = 0
            idx +=1
        for i in range(c1):
            nums[idx] = 1
            idx +=1
        for i in range(c2):
            nums[idx] = 2
            idx +=1
        return nums
# Approach:
# We can count the number of 0s, 1s and 2s in the input array and then overwrite the input array with the counted values.
# Time Complexity: O(n) where n is the length of the input array.
# Space Complexity: O(1) as we are using only a constant amount of extra space

## or
class Solution:
    def sortColors(self, nums):
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
# Approach:
# We can use the Dutch National Flag algorithm to solve this problem in O(n) time complexity and O(1) space complexity.
# We will maintain three pointers: low, mid and high. The low pointer will point to the next position of 0, the mid pointer will point to the current element and the high pointer will point to the next position of 2. We will iterate through the array and swap the elements accordingly.
# Time Complexity: O(n) where n is the length of the input array.
# Space Complexity: O(1) as we are using only a constant amount of extra space.
