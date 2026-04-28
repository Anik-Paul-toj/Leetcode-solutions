# Problem: Plus One
# Link: https://leetcode.com/problems/plus-one/
# Difficulty: Easy

# Problem Statement:
# You are given a large integer represented as an integer array digits,
# where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant.
# Increment the integer by one and return the resulting array of digits.

# Testcases:
# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]

# Example 2:
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]

# Example 3:
# Input: digits = [9]
# Output: [1,0]

## Approach:
 ## Prothome digits list ke string e convert kori using join
    ##Tarpor oi string ke int e convert kori → full number pai
    ##Tarpor number ta ke +1 kori
    ##Ebar abar number ta ke string e convert kori
    ##Finally, prottekta digit ke abar int kore list e store kori
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(map(str,digits)))
        num += 1
        l = []
        for n in str(num):
            l.append(int(n))
        return l
