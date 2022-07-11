from typing import List


class Solution:
    @staticmethod
    def getCommonPrefix(first: str, second: str) -> str:
        res = ''
        for a, b in zip(first, second):
            if a == b:
                res += a
            else:
                break
        return res

    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_str = strs[0]
        for el in strs[1:]:
            max_str = self.getCommonPrefix(max_str, el)
            if max_str == '':
                break
        return max_str
