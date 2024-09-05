'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        # sort the array of strings
        strs.sort()

        prefix = ""
        first_str, last_str = strs[0], strs[-1]
        for i in range(min(len(first_str), len(last_str))):
            if first_str[i] == last_str[i]:
                prefix += first_str[i]
            else:
                break
        return prefix        

# Driver code
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    strs1 = ["flower", "flow", "flight"]
    print("Example 1:")
    print("Input:", strs1)
    print("Output:", solution.longestCommonPrefix(strs1))  
    print()

    # Example 2
    strs2 = ["dog", "racecar", "car"]
    print("Example 2:")
    print("Input:", strs2)
    print("Output:", solution.longestCommonPrefix(strs2)) 