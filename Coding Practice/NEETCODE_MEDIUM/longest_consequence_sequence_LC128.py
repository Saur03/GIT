'''
Longest Consecutive Sequence
Given an array of integers nums, return the length of the longest consecutive sequence of elements.
A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [2,20,4,10,3,4,5]
Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:
Input: nums = [0,3,2,5,4,6,1,1]
Output: 7

Constraints:
1. 0 <= nums.length <= 1000
2. -10^9 <= nums[i] <= 10^9
'''
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            #check if its start of the sequence
            if (n-1) not in numSet:
                length = 0
                while(n+length) in numSet:
                    length += 1
                longest= max(length,longest)
        return longest            