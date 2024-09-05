'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

Example 3:
Input: s = "acb", t = "ahbgdc"
Output: false
'''

class Solution:
    def isSubsequence(self, s, t):
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        
        index = 0
        for alphabet in t:
            if alphabet == s[index]:
                index = index + 1
            if index == len(s):
                return True
        return False

if __name__=='__main__':
    str1 = "abc"
    str2 = "xahbgdc"
    s = Solution
    result = s.isSubsequence(s, str1, str2)
    print (result)