# Given a string s, find the length of the longest substring without repeating characters.

 

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3

# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

##SOLUTION##

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        longest_string = []
        len_string = 0
        count = 0
        i = 0
        while i < len(s):
            if s[i] in longest_string:
                if len(longest_string) > len_string:
                    len_string = len(longest_string)
                longest_string.clear()
                if ((count+1) < len(s)):
                    count += 1
                    i = count
                longest_string.append(s[i])
                i += 1
            else:
                longest_string.append(s[i])
                i += 1
                
        if len(longest_string) > len_string:
            len_string = len(longest_string)
        
        return len_string