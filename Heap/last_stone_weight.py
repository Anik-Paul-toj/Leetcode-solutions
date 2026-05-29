# Problem: Last Stone Weight
# Link: https://leetcode.com/problems/last-stone-weight/
# Difficulty: Easy
# Problem Statement:
# You are given an array of integers stones where stones[i] is the weight of the ith stone.
#
# We are playing a game with the stones. On each turn, we choose the heaviest two stones
# and smash them together. Suppose the heaviest two stones have weights x and y with x <= y.
#
# The result of this smash is:
# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
#
# At the end of the game, there is at most one stone left.
#
# Return the weight of the last remaining stone. If there are no stones left, return 0.
#
# Testcases:
# Example 1:
# Input: stones = [2,7,4,1,8,1]
# Output: 1
#
# Example 2:
# Input: stones = [1]
# Output: 1
#
# Constraints:
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) >1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            if first != second:
                heapq.heappush(stones,-(first-second))
            if len(stones) ==0:
                return 0
        return -stones[0]
    
## Approach:
# 1. We can use a max heap to keep track of the heaviest stones. Since Python's `heapq` module implements a min heap, we can insert the negative of the stone weights to simulate a max heap.
# 2. We will repeatedly pop the two heaviest stones (the two smallest negative values   from the heap), smash them together, and if they are not equal, we will push the difference back into the heap.
# 3. We will continue this process until there is at most one stone left in the heap. If there are no stones left, we will return 0; otherwise, we will return the weight of the last remaining stone (the negative of the value in the heap).
# Time Complexity: O(n log n) where n is the number of stones, because we may need to perform up to n-1 smash operations, and each operation involves popping and pushing elements from the heap.
# Space Complexity: O(n) for the heap that stores the stones.