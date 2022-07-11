class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_substr = ''
        max_len = 0
        for i in s:
            if i not in unique_substr:
                unique_substr = unique_substr.__add__(i)
            else:
                unique_substr = unique_substr.__add__(i)
                unique_substr = unique_substr[unique_substr.find(i)+1:]
            if max_len < len(unique_substr): max_len = len(unique_substr)
        return max_len