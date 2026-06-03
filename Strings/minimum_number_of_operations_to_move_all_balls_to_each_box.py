# Problem: Minimum Number of Operations to Move All Balls to Each Box
# Link: https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
# Difficulty: Medium
# Problem Statement:
# You have n boxes. You are given a binary string boxes of length n,
# where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.
#
# In one operation, you can move one ball from a box to an adjacent box.
# Box i is adjacent to box j if abs(i - j) == 1.
#
# Return an array answer of size n, where answer[i] is the minimum number
# of operations needed to move all the balls to the ith box.
#
# Each answer[i] is calculated considering the initial state of the boxes.
#
# Testcases:
# Example 1:
# Input: boxes = "110"
# Output: [1,1,3]
#
# Example 2:
# Input: boxes = "001011"
# Output: [11,8,5,4,3,4]
#
# Constraints:
# n == boxes.length
# 1 <= n <= 2000
# boxes[i] is either '0' or '1'.

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        for i in range(len(boxes)):
            moves = 0
            for j in range(len(boxes)):
                if boxes[j]=='1':
                    moves+=abs(i-j)
            ans.append(moves)
        return ans
## Approach:
# 1. We can iterate through each box and calculate the number of moves required to move all the balls to that box.
# 2. For each box, we can iterate through all the boxes and check if there is a ball in that box. If there is a ball, we can calculate the number of moves required to move that ball to the current box and add it to the total moves.
# 3. Finally, we can return the list of moves for each box.
# Time Complexity: O(n^2) where n is the length of the boxes string.
# Space Complexity: O(n) where n is the length of the boxes string.