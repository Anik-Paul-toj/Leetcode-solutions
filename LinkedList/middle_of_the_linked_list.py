# Problem: Middle of the Linked List
# Link: https://leetcode.com/problems/middle-of-the-linked-list/
# Difficulty: Easy
# Problem Statement:
# Given the head of a singly linked list, return the middle node of the linked list.
#
# If there are two middle nodes, return the second middle node.
#
# Testcases:
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
#
# Example 2:
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
#
# Constraints:
# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        import math
        temp = head
        c = 0
        while(temp):
            temp = temp.next
            c +=1        
        mid = (c//2)
        temp = head
        while mid:
            temp= temp.next
            mid -=1
        return temp

## Approach:
# 1. We can first count the number of nodes in the linked list.
# 2. We can then calculate the middle index using the formula mid = (c//2) where c is the count of nodes.
# 3. We can then iterate through the linked list again and return the node at the middle index.
# Time Complexity: O(n) where n is the number of nodes in the linked list.
# Space Complexity: O(1) since we are using only a constant amount of space to store the count and the middle index.