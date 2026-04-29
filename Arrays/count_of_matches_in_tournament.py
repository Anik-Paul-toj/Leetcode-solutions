# Problem: Count of Matches in Tournament
# Link: https://leetcode.com/problems/count-of-matches-in-tournament/
# Difficulty: Easy

# Problem Statement:
# You are given an integer n, the number of teams in a tournament.
# If teams are even → n/2 matches played, n/2 teams advance.
# If teams are odd → (n-1)/2 matches played, (n-1)/2 + 1 teams advance.
# Return total number of matches played until one winner remains.

# Testcases:
# Example 1:
# Input: n = 7
# Output: 6

# Example 2:
# Input: n = 14
# Output: 13

## Approach:
    ## Brute:
        # Loop until n is greater than 1
        # If n is even, add n/2 to matches and update n to n/2
        # If n is odd, add (n-1)/2 to matches and update n to (n-1)/2 + 1
        # Time complexity: O(log n)
        # Space complexity: O(1)
class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n > 1:
            matches += n // 2
            n = (n // 2) + (n % 2)
        
        return matches