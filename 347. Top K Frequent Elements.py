class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt_table = {cnt: [] for cnt in range(1, len(nums)+1)}
        n_cnt = Counter(nums)
        for key, val in n_cnt.items():
            cnt_table[val].append(key)
        
        res = []
        for cnt in range(1, len(nums)+1)[::-1]:
            for el in cnt_table[cnt]:
                res.append(el)
                if len(res) == k:
                    return res