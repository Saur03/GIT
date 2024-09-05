'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
 
Constraints:
1. 1 <= nums.length <= 2 * 104
2. -1000 <= nums[i] <= 1000
3. -107 <= k <= 107
'''
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        curSum=0
        prefixSum={0:1}

        for n in nums:
            curSum +=n
            diff =curSum-k

            res+=prefixSum.get(diff,0)
            prefixSum[curSum] = 1+prefixSum.get(curSum,0)

        return res    