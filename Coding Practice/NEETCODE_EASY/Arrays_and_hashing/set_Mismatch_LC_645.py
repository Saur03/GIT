'''
You have a set of integers s, which originally contains all the numbers from 1 to n. 
Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, 
which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.
Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]

Example 2:
Input: nums = [1,1]
Output: [1,2]
 
Constraints:
2 <= nums.length <= 104
1 <= nums[i] <= 104
'''
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N=len(nums)
        x=0 # duplicate-missing
        y=0 #duplicate^2-missing^2

        for i in range(1,N+1):
            x += nums[i-1] -i
            y += nums[i-1]**2-i**2

        missing = (y-x**2) // (2*x)
        duplicate = missing+x
        return [duplicate, missing]