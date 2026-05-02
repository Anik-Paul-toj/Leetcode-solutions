# Problem: Merge Two Sorted Lists
# Link: https://leetcode.com/problems/merge-two-sorted-lists/
# Difficulty: Easy

# Problem Statement:
# You are given two sorted linked lists list1 and list2.
# Merge them into one sorted linked list and return its head.

# Testcases:
# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        print(cur)

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 if list1 else list2
        return dummy.next
## Approach:
# 1. Create a dummy node to serve as the head of the merged linked list.
# 2. Use a pointer (cur) to keep track of the current position in the
#    merged linked list.
# 3. Iterate through both linked lists (list1 and list2) until one of them is exhausted.
# 4. At each step, compare the values of the current nodes of both lists.
#    - If the value of the current node in list1 is less than or equal to that in list2, append it to the merged list and move the pointer of list1 to the next node.
#    - Otherwise, append the current node of list2 to the merged list and move the pointer of list2 to the next node.
# 5. After the loop, if there are remaining nodes in either list1 or list2, append them to the merged list.
# 6. Finally, return the next node of the dummy node, which is the head
