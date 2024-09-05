'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, 
but the order of the characters can be different.

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:
Input: strs = ["x"]
Output: [["x"]]

Example 3:
Input: strs = [""]
Output: [[""]]

Constraints:
1. 1 <= strs.length <= 1000.
2. 0 <= strs[i].length <= 100
3. strs[i] is made up of lowercase English letters.
'''
from collections import defaultdict

def groupAnagrams(strs):
    # Initialize a dictionary to store anagrams
    anagrams = defaultdict(list)
    
    # Iterate through each string in the input array
    for word in strs:
        # Sort the characters of the word to identify anagrams
        sorted_word = ''.join(sorted(word))
        
        # Append the original word to the list associated with the sorted word
        anagrams[sorted_word].append(word)
    
    # Return the values of the dictionary, which are lists of anagrams
    return list(anagrams.values())

# Driver code
if __name__ == "__main__":
    # Test cases
    strs1 = ["act","pots","tops","cat","stop","hat"]
    print(groupAnagrams(strs1))  # Output: [['act', 'cat'], ['pots', 'tops', 'stop'], ['hat']]

    strs2 = ["x"]
    print(groupAnagrams(strs2))  # Output: [['x']]

    strs3 = [""]
    print(groupAnagrams(strs3))  # Output: [['']]
