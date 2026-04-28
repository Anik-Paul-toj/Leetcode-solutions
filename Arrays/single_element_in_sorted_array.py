# Problem: Single Element in a Sorted Array
# Link: https://leetcode.com/problems/single-element-in-a-sorted-array/
# Difficulty: Medium

# Problem Statement:
# You are given a sorted array where every element appears exactly twice,
# except for one element which appears only once.
# Return that single element.
# Your solution must run in O(log n) time and O(1) space.

# Testcases:
# Example 1:
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2

# Example 2:
# Input: nums = [3,3,7,7,10,11,11]
# Output: 10

## Approach:
 ## Prothome ekta hashmap (dictionary) nei using defaultdict(int)
    # Tarpor array ta loop kore prottek number er count store kori
    # Mane:
    # jeta 2 bar ase → count = 2
    # jeta 1 bar ase → count = 1
    # Tarpor abar hashmap ta loop kori
    # Jekhane value (count) = 1 → oi key tai answer
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(map(str,digits)))
        num += 1
        l = []
        for n in str(num):
            l.append(int(n))
        return l
