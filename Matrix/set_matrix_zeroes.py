# Problem: Set Matrix Zeroes
# Link: https://leetcode.com/problems/set-matrix-zeroes/
# Difficulty: Medium
# Problem Statement:
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
#
# You must do it in place.
#
# Testcases:
# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
#
# Example 2:
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
#
# Constraints:
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -2^31 <= matrix[i][j] <= 2^31 - 1
#
# Follow up:
# A straightforward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?

# Brute Force Solution:
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col = [0] * len(matrix[0])
        row = [0] * len(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] =1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row[i]==1 or col[j]==1:
                    matrix[i][j] =0
        return matrix
# Approach:
# 1. We can use two arrays to keep track of the rows and columns that need to be set to zero.
# 2. We iterate through the matrix and whenever we find a zero, we mark the corresponding row and column in the arrays.
# 3. After the first pass, we iterate through the matrix again and set the elements to zero if their corresponding row or column is marked in the arrays.
# Time Complexity: O(m*n) where m is the number of rows and n is the number of columns in the matrix.
# Space Complexity: O(m+n) for the two arrays used to keep track of the rows and columns that need to be set to zero.

# 2nd:
class solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col0 = 1
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                col0 = 0
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(len(matrix)-1, -1, -1):
            for j in range(len(matrix[0])-1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0 == 0:
                matrix[i][0] = 0
        return matrix
# Approach:
# 1. We can use the first row and first column of the matrix to keep track of the rows and columns that need to be set to zero.
# 2. We iterate through the matrix and whenever we find a zero, we mark the corresponding row and column in the first row and first column.
# 3. After the first pass, we iterate through the matrix again in reverse order and set the elements to zero if their corresponding row or column is marked in the first row or first column.
# 4. We also need to keep track of whether the first column needs to be set to zero separately, since we are using it to keep track of the rows.
# Time Complexity: O(m*n) where m is the number of rows and n is the number of columns in the matrix.
# Space Complexity: O(1) since we are using the first row and first column of the matrix to keep track of the rows and columns that need to be set to zero, and a variable to keep track of whether the first column needs to be set to zero.       
