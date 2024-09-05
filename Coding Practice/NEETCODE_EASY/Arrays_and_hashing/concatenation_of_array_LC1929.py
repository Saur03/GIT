'''
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
Example 2:

Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]
'''

class Solution:
    def getConcatenation_m1(self, nums):
        n = len(nums)
        arr=[]
        for i in range(2*n):
            arr.append(nums[i%n])
        return arr
    
    def getConcatenation_m2(self, nums):
        return nums*2
    
    def getConcatenation(self, nums):
        return nums+nums
        
        
if __name__=='__main__':
    s = Solution
    nums1 = [1,2,1]
    nums2 = [1,3,2,1]
    result1 = s.getConcatenation(s, nums1)
    result2 = s.getConcatenation(s, nums2)
    print (result1)
    print (result2)