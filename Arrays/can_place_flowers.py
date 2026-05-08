# Problem: Can Place Flowers
# Link: https://leetcode.com/problems/can-place-flowers/
# Difficulty: Easy

# Problem Statement:
# You have a flowerbed where some plots are planted and some are empty.
# Flowers cannot be planted in adjacent plots.
# Return true if n new flowers can be planted without violating the rule.

# Testcases:
# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        c = 0
        for j in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i ==0:
                    if len(flowerbed) ==1  or flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        c += 1
                elif i == len(flowerbed)-1:
                    if flowerbed[i-1] ==0:
                        flowerbed[i] = 1
                        c +=1
                else:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        c +=1
            i +=1
        if c >= n:
            return True
        else:
            return False
        
# Approach:
# We can iterate through the flowerbed and check if we can plant a flower at each position.
# If the current position is empty (0), we check the adjacent positions to ensure that we are not violating the rule of not planting flowers in adjacent plots.
# If we can plant a flower at the current position, we mark it as planted (1) and increment our count of planted flowers.
# Finally, we compare the count of planted flowers with n and return true if we have planted at least n flowers, otherwise we return false.