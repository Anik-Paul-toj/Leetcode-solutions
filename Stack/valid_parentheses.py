# Problem: Valid Parentheses
# Link: https://leetcode.com/problems/valid-parentheses/
# Difficulty: Easy
# Problem Statement:
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
# Testcases:
# Example 1:
# Input: s = "()"
# Output: true
#
# Example 2:
# Input: s = "()[]{}"
# Output: true
#
# Example 3:
# Input: s = "(]"
# Output: false
#
# Example 4:
# Input: s = "([])"
# Output: true
#
# Example 5:
# Input: s = "([)]"
# Output: false
#
# Constraints:
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs= {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        for si in s:
            if si == "(" or si == "{" or si == "[":
                stack.append(si)
            # print(stack)
            elif si == ")" or si == "}" or si == "]":
                if not stack:
                    return False
                val = stack.pop()
                if pairs[val] != si:
                    return False
        return not stack

## Approach:
# We can use a stack to keep track of the opening brackets. For every closing bracket, we check if it matches the top of the stack.
# If it does, we pop the stack and continue. If it doesn't, we return false. At the end, if the stack is empty, we return true; otherwise, we return false.     
# Time Complexity: O(n), where n is the length of the string.
# Space Complexity: O(n), in the worst case when all characters are opening brackets.   
