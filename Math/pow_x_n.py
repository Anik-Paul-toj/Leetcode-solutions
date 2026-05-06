# Problem: Pow(x, n)
# Link: https://leetcode.com/problems/powx-n/
# Difficulty: Medium

# Problem Statement:
# Implement pow(x, n), which calculates x raised to the power n (x^n).

# Testcases:
# Example 1:
# Input: x = 2.00000, n = 10
# Output: 1024.00000

# Example 2:
# Input: x = 2.10000, n = 3
# Output: 9.26100

# Example 3:
# Input: x = 2.00000, n = -2
# Output: 0.25000

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n<0:
            return (1/self.myPow(x,-n))
        elif n%2==0:
            y = self.myPow(x, n//2)
            return y*y
        else:
            return x*self.myPow(x,n-1)
# Explanation:
# The function myPow takes two parameters: x (the base) and n (the exponent). It uses recursion to calculate the power of x raised to n.
# The function handles three cases:
# 1. If n is 0, it returns 1, as any number raised to the power of 0 is 1.
# 2. If n is negative, it calculates the power for the positive exponent and takes the reciprocal to handle the negative exponent.
# 3. If n is even, it calculates the power for n//2 and squares the result to optimize the calculation.
# 4. If n is odd, it multiplies x by the result of the function called with n-1 to handle the odd exponent case.
# Time Complexity: O(log n) in the case of even n, and O(n) in the case of odd n.
# Space Complexity: O(log n) due to the recursive call stack in the case of even n, and O(n) in the case of odd n.  