class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        uniq_c = set([c for c in ''.join(strs)])
        res = {}

        for s in strs:
            dictS = {key:0 for key in uniq_c}
            for c in s: 
                dictS[c] += 1
            
            res[tuple(dictS.values())] = [s,] + res.get(tuple(dictS.values()), [])
        return res.values()