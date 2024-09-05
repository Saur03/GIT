'''
Duplicate Integer
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true
Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
'''


class Solution:
    def hasDuplicate_m1(self, nums) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if (nums[i] == nums[j]):
                    return True
        return False
    
    # used hash function to save the index
    def hasDuplicate_m2(self, nums) -> bool:
        n = len(nums)
        h1 = {}
        for i in range(0,n):
            if nums[i] in h1:
                return True
            h1[nums[i]] = i
        return False
    
    def hasDuplicate_m3(self, nums) -> bool:
        return len(nums) != len(set(nums))

if __name__=='__main__':
    nums = [1,2,3,3]
    s1 = Solution()
    result1 = s1.hasDuplicate_m1(nums)
    result2 = s1.hasDuplicate_m2(nums)
    result3 = s1.hasDuplicate_m3(nums)
    print(result3)