class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs: 
            res += f'{len(s)}#{s}'
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        while s:
            d = s[:s.index('#')]
            i = len(d)+1
            j = i+int(d)
            res.append(s[i:j])
            s = s[j:]
        return res