# Problem: Find the Town Judge
# Link: https://leetcode.com/problems/find-the-town-judge/
# Difficulty: Easy
# Problem Statement:
# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
#
# If the town judge exists, then:
# 1. The town judge trusts nobody.
# 2. Everybody (except for the town judge) trusts the town judge.
# 3. There is exactly one person that satisfies properties 1 and 2.
#
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.
#
# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
#
# Testcases:
# Example 1:
# Input: n = 2, trust = [[1,2]]
# Output: 2
#
# Example 2:
# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3
#
# Example 3:
# Input: n = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1
#
# Constraints:
# 1 <= n <= 1000
# 0 <= trust.length <= 10^4
# trust[i].length == 2
# All the pairs of trust are unique.
# ai != bi
# 1 <= ai, bi <= n


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        for src,dest in trust:
            outgoing[src] +=1
            incoming[dest] +=1
        print(incoming)
        print(outgoing)
        for i in range(1,n+1):
            if outgoing[i] == 0 and incoming[i] == n-1:
                return i
        return -1
    
## Approach:
# 1. We can use two dictionaries to keep track of the number of people that trust each person (incoming) and the number of people that each person trusts (outgoing).
# 2. We can iterate through the trust array and update the incoming and outgoing dictionaries accordingly.
# 3. Finally, we can iterate through the range of people from 1 to n and check if there is a person who is trusted by n-1 people (incoming[i] == n-1) and does not trust anyone (outgoing[i] == 0). If such a person exists, we can return their label. Otherwise, we can return -1.
# Time Complexity: O(n + m) where n is the number of people and m is the length of the trust array.
# Space Complexity: O(n) since we are using two dictionaries to store the incoming and outgoing trust counts for each person.

