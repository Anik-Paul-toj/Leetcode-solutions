# Problem: Find Center of Star Graph
# Link: https://leetcode.com/problems/find-center-of-star-graph/
# Difficulty: Easy
# Problem Statement:
# There is an undirected star graph consisting of n nodes labeled from 1 to n.
# A star graph is a graph where there is one center node and exactly n - 1 edges
# that connect the center node with every other node.
#
# You are given a 2D integer array edges where each edges[i] = [ui, vi]
# indicates that there is an edge between the nodes ui and vi.
#
# Return the center of the given star graph.
#
# Testcases:
# Example 1:
# Input: edges = [[1,2],[2,3],[4,2]]
# Output: 2
#
# Example 2:
# Input: edges = [[1,2],[5,1],[1,3],[1,4]]
# Output: 1
#
# Constraints:
# 3 <= n <= 10^5
# edges.length == n - 1
# edges[i].length == 2
# 1 <= ui, vi <= n
# ui != vi
# The given edges represent a valid star graph.

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        delta = defaultdict(int)

        for src, dest in edges:
            delta[src] +=1
            delta[dest] +=1
        n = len(edges) + 1
        for i in range(1,n+1):
            if delta[i] == n-1:
                return i

## Approach:
# 1. We can use a dictionary to keep track of the degree of each node in the graph.
# 2. We can iterate through the edges and update the degree of each node accordingly.       
# 3. Finally, we can iterate through the degree dictionary and return the node that has a degree of n-1, which is the center of the star graph.
# Time Complexity: O(n) where n is the number of edges in the graph.    
# Space Complexity: O(n) since we are using a dictionary to store the degree of each node in the graph.

#or:
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return edges[0][0] if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1] else edges[0][1]

## Approach:
# 1. Since the graph is a star graph, the center node will be connected to all other nodes. Therefore, we can simply check the first two edges and determine which node is the center based on the common node in those edges.
# 2. We can check if the first node of the first edge is the same as    the first node of the second edge or the second node of the second edge. If it is, then that node is the center. Otherwise, the second node of the first edge is the center.
# Time Complexity: O(1) since we are only checking a constant number of edges.  
# Space Complexity: O(1) since we are not using any additional data structures to store the degree of each node in the graph.
    