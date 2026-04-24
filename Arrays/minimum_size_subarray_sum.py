# Problem: Minimum Size Subarray Sum
# Link: https://leetcode.com/problems/minimum-size-subarray-sum/
# Difficulty: Medium

# Problem Statement:
# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a subarray whose sum is greater than or equal to target.
# If there is no such subarray, return 0 instead.

# Testcases:
# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2

# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1

# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0


# Approch:
 ## sliding window approach:
   ## so we can assign a result to inf as amadr minmum resuly lagbe
    ## then we can assign a variable to 0 as amadr sum lagbe
    ## then ekta pointer nebo index zero te  and the loop ghorabo puro len(nums)-1 obdi jeta r diye 
    ## then amra sum er sathe nums[r] add korbo total += nums[r]
    ## the while total >= target
    ## untill amra result er modhe minimum  ta store korbbo result = min(result, r-l+1)
    ## then amra total theke nums[l] minus korbo total -= nums[l] as ager ta minus korte thakbo
    ## and l +=1 korte thakbo as amra left pointer ke right e move korte thakbo
    ## finally amra check korbo jodi result inf hoy tahole return 0 otherwise return result
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = float('inf')
        total = 0
        l = 0
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                result = min(result, r-l+1)
                total -= nums[l]
                l += 1
        return 0 if result == float('inf') else result