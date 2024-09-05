'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:
Input: 
nums = [3,4,5,6], target = 7
Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:
Input: nums = [4,5,6], target = 10
Output: [0,2]

Example 3:
Input: nums = [5,5], target = 10
Output: [0,1]
'''

from typing import Counter


class Solution:
    def twoSum(self, nums, target):
        h = {}
        for i in range(0, len(nums)):
            balance = target-nums[i]
            if balance not in h:
                h[nums[i]] = i
            else:
                return [h[balance],i]
        

if __name__=='__main__':
    obj = Solution
    nums = [5,6,3,4]
    target = 7
    result = obj.twoSum(obj, nums, target)
    print(result)