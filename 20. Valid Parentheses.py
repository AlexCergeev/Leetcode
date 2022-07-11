class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2: return False
        dct = {"(": ")", "[": "]", "{": "}"}
        a = []
        for ch in s:
            if ch in dct.keys():
                a.append(ch)
            else:
                if not a:
                    return False
                if dct[a[-1]] == ch:
                    a.pop()
                else:
                    return False
        return False if a else True
