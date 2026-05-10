# Problem: Find the Difference of Two Arrays
# Link: https://leetcode.com/problems/find-the-difference-of-two-arrays/
# Difficulty: Easy
# Problem Statement:
# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
#
# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
#
# Note that the integers in the lists may be returned in any order.
#
# Testcases:
# Example 1:
# Input: nums1 = [1,2,3], nums2 = [2,4,6]
# Output: [[1,3],[4,6]]
#
# Example 2:
# Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
# Output: [[3],[]]
#
# Constraints:
# 1 <= nums1.length, nums2.length <= 1000
# -1000 <= nums1[i], nums2[i] <= 1000

from collections import defaultdict
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hm = defaultdict(int)
        hm2 = defaultdict(int)
        for n in nums1:
            hm[n] += 1
        for n in nums2:
            hm2[n] +=1
        l1 =[]
        l2 = []
        for i in range(len(nums2)):
            if nums2[i] not in hm and nums2[i] not in l1:
                l1.append(nums2[i])
        for i in range(len(nums1)):
            if nums1[i] not in hm2 and nums1[i] not in l2:
                l2.append(nums1[i])
        return ([l2,l1])
        # print(hm,hm2)
        
## Approach:
# 1. Create two hashmaps to store the frequency of each element in nums1 and nums2.
# 2. Iterate through nums2 and check if each element is not present in the hashmap of nums1 and also not already added to the result list for nums2. If so, add it to the result list for nums2.
# 3. Iterate through nums1 and check if each element is not present in the hashmap of nums2 and also not already added to the result list for nums1. If so, add it to the result list for nums1.
# 4. Return the result list containing both lists of distinct integers.
# 5. The time complexity of this approach is O(n + m) where n and m are the lengths of nums1 and nums2 respectively, and the space complexity is O(n + m) due to the hashmaps and result lists.

