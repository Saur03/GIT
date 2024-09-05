'''
Is Anagram
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
'''

from typing import Counter


class Solution:
    def isAnagram_m1(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        return False
    
    # used hash function to count alphabets
    def isAnagram_m2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(0,len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if (countS[c] != countT.get(c, 0)):
                return False
        return True
    
    def isAnagram_m3(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__=='__main__':
    s1 = "racecar"
    t1 = "carrace"
    s2 = "jar"
    t2 = "jam"
    s3 = "bbcc"
    t3 = "ccbc"
    s = Solution
    result1_m1 = s.isAnagram_m1(s, s1,t1)
    result2_m1 = s.isAnagram_m1(s, s2,t2)
    result3_m1 = s.isAnagram_m1(s, s3, t3)
    print(result1_m1, result2_m1, result3_m1)
    result1_m2 = s.isAnagram_m2(s, s1,t1)
    result2_m2 = s.isAnagram_m2(s, s2,t2)
    result3_m2 = s.isAnagram_m2(s, s3, t3)
    print(result1_m2, result2_m2, result3_m2)
    result1_m3 = s.isAnagram_m3(s, s1,t1)
    result2_m3 = s.isAnagram_m3(s, s2,t2)
    result3_m3 = s.isAnagram_m3(s, s3, t3)
    print(result1_m3, result2_m3, result3_m3)
