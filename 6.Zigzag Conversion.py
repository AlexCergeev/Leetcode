class Solution:
    def convert(self, s: str, numRows: int) -> str:
        mass = [[] for i in range(numRows)]
        s = list(s[::-1])
        while s:
           [i.append(s.pop()) for i in mass if s]
           [j.append(s.pop()) for j in mass[1:-1][::-1] if s]
        return ''.join((''.join(i) for i in mass))