# Problem: Lemonade Change
# Link: https://leetcode.com/problems/lemonade-change/
# Difficulty: Easy
# Problem Statement:
# At a lemonade stand, each lemonade costs $5. Customers are standing in a queue
# to buy from you and order one at a time (in the order specified by bills).
#
# Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.
# You must provide the correct change to each customer so that the net transaction
# is that the customer pays $5.
#
# Note that you do not have any change in hand at first.
#
# Given an integer array bills where bills[i] is the bill the ith customer pays,
# return true if you can provide every customer with the correct change,
# or false otherwise.
#
# Testcases:
# Example 1:
# Input: bills = [5,5,5,10,20]
# Output: true
#
# Example 2:
# Input: bills = [5,5,10,10,20]
# Output: false
#
# Constraints:
# 1 <= bills.length <= 10^5
# bills[i] is either 5, 10, or 20.

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for bill in bills:
            if bill == 5:
                five +=1
            elif bill == 10:
                if five == 0:
                    return False
                five -=1
                ten +=1
            else:
                if ten > 0 and five > 0:
                    ten -=1
                    five -=1
                elif five >=3:
                    five -=3
                else:
                    return False
        return True
# Approach:
# 1. Initialize two counters, `five` and `ten`, to keep track of the number of $5 and $10 bills we have.
# 2. Iterate through each bill in the input array `bills`.
# 3. For each bill:
#    - If the bill is $5, increment the `five` counter. 
#    - If the bill is $10, check if we have at least one $5 bill to give as change. If not, return False. Otherwise, decrement the `five` counter and increment the `ten` counter.
#    - If the bill is $20, we have two options for giving change: either one $10 bill and one $5 bill, or three $5 bills. We check for the first option first, and if it's not possible, we check for the second option. If neither option is possible, return False.
# 4. If we successfully process all bills, return True at the end.
# Time Complexity: O(n), where n is the number of bills.
# Space Complexity: O(1), as we are using only a constant amount of extra space for the counters.
