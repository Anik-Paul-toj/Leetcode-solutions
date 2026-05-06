# Problem: Spiral Matrix
# Link: https://leetcode.com/problems/spiral-matrix/
# Difficulty: Medium

# Problem Statement:
# Given an m x n matrix, return all elements of the matrix in spiral order.

# Testcases:
# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top,bottom = 0, len(matrix)-1
        left,right = 0, len(matrix[0])-1

        ans = []

        while top<=bottom and left<=right:
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top +=1

            for i in range(top,bottom +1):
                ans.append(matrix[i][right])
            right -=1

            if top <= bottom:
                for i in range(right,left-1,-1):
                    ans.append(matrix[bottom][i])
                bottom -=1

            if left <= right:
                for i in range(bottom,top-1,-1):
                    ans.append(matrix[i][left])
                left +=1
        return ans


## Approach:
# We can solve this problem by maintaining four pointers: top, bottom, left, and right. These pointers will help us keep track of the current boundaries of the matrix that we need to traverse in a spiral order.
# We will use a while loop that continues until the top pointer is less than or equal to the bottom pointer and the left pointer is less than or equal to the right pointer. Inside the loop, we will perform the following steps:
# 1. Traverse from left to right along the top row and append the elements to the result list. Then, we will move the top pointer down by one.
# 2. Traverse from top to bottom along the right column and append the elements to the result list. Then, we will move the right pointer left by one.
# 3. If the top pointer is still less than or equal to the bottom pointer, we will traverse from right to left along the bottom row and append the elements to the result list. Then, we will move the bottom pointer up by one.
# 4. If the left pointer is still less than or equal to the right pointer, we will traverse from bottom to top along the left column and append the elements to the result list. Then, we will move the left pointer right by one.
# We will repeat these steps until we have traversed all the elements in the matrix in spiral order. Finally, we will return the result list containing the elements in spiral order.
# Time Complexity: O(m*n) where m is the number of rows and n is the number of columns in the matrix, as we need to visit each element once.
# Space Complexity: O(m*n) in the worst case, if we store all the elements in the result list. However, if we consider the output list as not part of the space complexity, then the space complexity is O(1) as we are using only a constant amount of extra space for the pointers and temporary variables.
    