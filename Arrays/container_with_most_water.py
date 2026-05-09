# Problem: Container With Most Water
# Link: https://leetcode.com/problems/container-with-most-water/
# Difficulty: Medium

# Problem Statement:
# Given an array height where each element represents the height of a vertical line,
# find two lines that together form a container containing the maximum amount of water.
# Return the maximum water that can be stored.

# Testcases:
# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49

# Example 2:
# Input: height = [1,1]
# Output: 1

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        left, right = 0, len(height)-1
        while (left<=right):
            width = right - left
            hei = min(height[left], height[right])
            currArea = width * hei
            maxArea = max(maxArea, currArea)

            if(height[left]<height[right]):
                left +=1
            else:
                right -=1
        return maxArea
    
## Approach:
# We can use two pointers to solve this problem.
# We can initialize two pointers, one at the beginning of the array and one at the end of the array.
# We can calculate the area formed by the two pointers and update the maximum area accordingly.
# We can then move the pointer that is pointing to the shorter line towards the other pointer, as this will potentially increase the area.
# We can repeat this process until the two pointers meet.   
# The time complexity of this approach is O(n) and the space complexity is O(1).