# Problem: Assign Cookies
# Link: https://leetcode.com/problems/assign-cookies/
# Difficulty: Easy
# Problem Statement:
# Assume you are an awesome parent and want to give your children some cookies.
# But, you should give each child at most one cookie.
#
# Each child i has a greed factor g[i], which is the minimum size of a cookie
# that the child will be content with; and each cookie j has a size s[j].
#
# If s[j] >= g[i], we can assign the cookie j to the child i,
# and the child i will be content.
#
# Your goal is to maximize the number of your content children and output
# the maximum number.
#
# Testcases:
# Example 1:
# Input: g = [1,2,3], s = [1,1]
# Output: 1
#
# Example 2:
# Input: g = [1,2], s = [1,2,3]
# Output: 2
#
# Constraints:
# 1 <= g.length <= 3 * 10^4
# 0 <= s.length <= 3 * 10^4
# 1 <= g[i], s[j] <= 2^31 - 1
#
# Note:
# This question is the same as 2410: Maximum Matching of Players With Trainers.

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i,j = 0, 0
        c = 0
        while i <len(g)  and j <len(s):
            if s[j]>= g[i]:
                c +=1
                i +=1
                j +=1
            else:
                j +=1
        return c 
    
## Approach:
# 1. Sort the greed factor array and the cookie size array.
# 2. Use two pointers to iterate through both arrays.
# 3. If the current cookie can satisfy the current child, move both pointers and increment the count of content children.
# 4. If the current cookie cannot satisfy the current child, move the cookie pointer to try the next cookie.
# 5. Continue this process until we have iterated through either array.
# 6. Return the count of content children as the result.
# Time Complexity: O(n log n) due to sorting the arrays.
# Space Complexity: O(1) if we ignore the space used for sorting, otherwise O(n) due to the sorting algorithm.