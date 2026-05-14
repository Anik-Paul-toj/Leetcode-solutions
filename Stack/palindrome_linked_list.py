# Problem: Palindrome Linked List
# Link: https://leetcode.com/problems/palindrome-linked-list/
# Difficulty: Easy
# Problem Statement:
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
#
# Follow up: Could you do it in O(n) time and O(1) space?
#
# Testcases:
# Example 1:
# Input: head = [1,2,2,1]
# Output: true
#
# Example 2:
# Input: head = [1,2]
# Output: false
#
# Constraints:
# The number of nodes in the list is in the range [1, 10^5].
# 0 <= Node.val <= 9

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp =head
        stack =[]
        while(temp):
            stack.append(temp.val)
            temp = temp.next
        return stack == stack[::-1]
    
## Approach:
# We can use a stack to store the values of the linked list. Then we can compare the stack with its reverse to check if it is a palindrome.
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(n), for the stack to store the values.