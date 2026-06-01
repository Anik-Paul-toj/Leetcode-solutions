# Problem: Rotate Image
# Link: https://leetcode.com/problems/rotate-image/
# Difficulty: Medium
# Problem Statement:
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.
#
# Testcases:
# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
#
# Example 2:
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
#
# Constraints:
# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r = len(matrix)-1
        while(l<r):
            for i in range(r-l):
                top ,bottom = l, r
                topleft = matrix[top][l + i]
                matrix[top][l + i] = matrix[bottom - i][l]
                matrix[bottom - i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top + i][r]
                matrix[top + i][r] = topleft
            l+=1
            r-=1
        return matrix
# Approach:
# We can rotate the image in place by performing a four-way swap for each element in the matrix. We will iterate through the matrix layer by layer, starting from the outermost layer and moving towards the innermost layer. For each element in the current layer, we will perform a four-way swap to rotate the elements to their correct positions.
# The four-way swap involves the following steps:
# 1. Store the top-left element in a temporary variable.
# 2. Move the bottom-left element to the top-left position.
# 3. Move the bottom-right element to the bottom-left position.
# 4. Move the top-right element to the bottom-right position.
# 5. Move the temporary variable (original top-left element) to the top-right position.
# We will repeat this process for each element in the current layer until we have rotated all layers of the matrix. The time complexity of this approach is O(n^2) since we need to visit each element in the matrix once, and the space complexity is O(1) since we are performing the rotation in place without using any additional data structures.         
# Complexity Analysis:
# Time Complexity: O(n^2) - We need to visit each element in the matrix once to perform the rotation.
# Space Complexity: O(1) - We are performing the rotation in place without using any additional data structures.

# Another Approach:
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Transpose the matrix
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse each row
        for i in range(len(matrix)):
            matrix[i].reverse()     
        return matrix
# Approach:
# We can rotate the image in place by first transposing the matrix and then reversing each row. Transposing the matrix will swap the rows with columns, and reversing each row will give us the desired 90-degree clockwise rotation.
# The steps are as follows:     
# 1. Transpose the matrix by swapping elements at positions (i, j) with (j, i) for all i and j.
# 2. Reverse each row of the transposed matrix to get the final rotated image.
# The time complexity of this approach is O(n^2) since we need to visit each element in the matrix twice (once for transposing and once for reversing), and the space complexity is O(1) since we are performing the rotation in place without using any additional data structures.
# Complexity Analysis:
# Time Complexity: O(n^2) - We need to visit each element in the matrix
# Space Complexity: O(1) - We are performing the rotation in place without using any additional data structures.