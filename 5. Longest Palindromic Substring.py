class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_pal = ''
        max_len = 0
        for i, el1 in enumerate(s):
            for j, el2 in enumerate(s[i:]):
                if s[i:][:j + 1] == s[i:][:j + 1][::-1]:
                    if max_len < len(s[i:][:j + 1]):
                        max_len = len(s[i:][:j + 1])
                        max_pal = s[i:][:j + 1]
        return max_pal
