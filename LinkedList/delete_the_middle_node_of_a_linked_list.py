# Problem: Delete the Middle Node of a Linked List
# Link: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
# Difficulty: Medium
# Problem Statement:
# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
#
# The middle node of a linked list of size n is the floor(n / 2)th node from the start using 0-based indexing.
#
# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
#
# Testcases:
# Example 1:
# Input: head = [1,3,4,7,1,2,6]
# Output: [1,3,4,1,2,6]
#
# Example 2:
# Input: head = [1,2,3,4]
# Output: [1,2,4]
#
# Example 3:
# Input: head = [2,1]
# Output: [2]
#
# Constraints:
# The number of nodes in the list is in the range [1, 10^5].
# 1 <= Node.val <= 10^5

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        temp = head
        c = 0
        while temp is not None:
            c +=1
            temp = temp.next
        mid = c//2
        temp1 = head
        for _ in range(mid-1):
            temp1 = temp1.next
        # print(temp1.val)
        temp1.next = temp1.next.next
        return head

## Approach:
# 1. We will first count the number of nodes in the linked list and store it in a variable `c`.
# 2. We will then calculate the middle index using `mid = c // 2
# 3. We will then traverse the linked list again until we reach the node just before the middle node (i.e., `mid - 1`).
# 4. We will then change the `next` pointer of the node at index `mid - 1` to point to the node at index `mid + 1`, effectively deleting the middle node from the linked list.
# 5. Finally, we will return the head of the modified linked list.
# The time complexity of this approach is O(n) because we traverse the linked list twice (once to count the nodes and once to delete the middle node). The space complexity is O(1) because we are using only a constant amount of extra space. 

# 