# Problem: Delete Node in a Linked List
# Link: https://leetcode.com/problems/delete-node-in-a-linked-list/
# Difficulty: Medium

# Problem Statement:
# You are given a node in a singly linked list (not the head).
# Delete this node such that:
# - Its value no longer exists in the list
# - List size decreases by one
# - Order of other nodes remains same

# Testcases:
# Example 1:
# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]

# Example 2:
# Input: head = [4,5,1,9], node = 1
# Output: [4,5,9]

## Approach:
# 1. Since we are given the node to be deleted, we can simply copy the value of the next node to the current node and then delete the next node.


class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next  = node.next.next
