'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
'''

class Solution:
    def lengthOfLastWord(self, s):
        s = s.strip()
        n = len(s)
        print(s)
        for i in range(n-1, -1, -1):
            if s[i] == ' ':
                return len(s[i+1:])
        return len(s)
        


if __name__=='__main__':
    obj = Solution

    s= "moon"
    result = obj.lengthOfLastWord(obj,s)
    print (result)