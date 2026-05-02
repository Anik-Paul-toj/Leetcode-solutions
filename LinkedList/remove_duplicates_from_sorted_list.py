# Problem: Remove Duplicates from Sorted List
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Difficulty: Easy

# Problem Statement:
# Given the head of a sorted linked list, delete all duplicates
# such that each element appears only once.
# Return the updated sorted linked list.

# Testcases:
# Example 1:
# Input: head = [1,1,2]
# Output: [1,2]

# Example 2:
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while temp and temp.next:
            if temp.val == temp.next.val:
                
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head
## Approach:
# 1. Initialize a temporary pointer (temp) to the head of the linked list.
# 2. Iterate through the linked list while temp and temp.next are not null.
# 3. If the value of the current node (temp) is equal to the value of the next node (temp.next), it means we have found a duplicate. In this case, we skip the next node by setting temp.next to temp.next.next.
# 4. If the values are not equal, we move the temp pointer to the next

