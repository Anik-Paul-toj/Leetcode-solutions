# Problem: Convert Binary Number in a Linked List to Integer
# Link: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# Difficulty: Easy
# Problem Statement:
# Given head which is a reference node to a singly-linked list.
# The value of each node in the linked list is either 0 or 1.
# The linked list holds the binary representation of a number.
#
# Return the decimal value of the number in the linked list.
#
# The most significant bit is at the head of the linked list.
#
# Testcases:
# Example 1:
# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10
#
# Example 2:
# Input: head = [0]
# Output: 0
#
# Constraints:
# The Linked List is not empty.
# Number of nodes will not exceed 30.
# Each node's value is either 0 or 1.

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        num = 0
        while head:
            num = num * 2 + head.val
            head = head.next
        return num
    
## Approach:
# 1. We can initialize a variable num to 0.
# 2. We can then iterate through the linked list and for each node, we can update the value of num by multiplying it by 2 and adding the value of the current node.
# 3. Finally, we can return the value of num as the decimal representation of the binary number represented by the linked list.
# Time Complexity: O(n) where n is the number of nodes in the linked list.
# Space Complexity: O(1) since we are using only a constant amount of space to store the variable num.

## or 
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res = []
        temp = head
        while(temp):
            res.append(temp.val)
            temp = temp.next
        # print(res)
        binary = "".join(map(str, res))
        print(binary)
        return (int(binary,2))
    
## Approach:
# 1. We can initialize an empty list res to store the values of the nodes in the linked list.
# 2. We can then iterate through the linked list and append the value of each node to the list res.
# 3. We can then join the values in the list res to form a binary string.
# 4. Finally, we can convert the binary string to an integer using the int() function with base 2 and return the result.
# Time Complexity: O(n) where n is the number of nodes in the linked list.
# Space Complexity: O(n) where n is the number of nodes in the linked list since we are using a list to store the values of the nodes.