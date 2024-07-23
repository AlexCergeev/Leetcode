class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        l, r = 1, max(piles)
        t = lambda k: sum([math.ceil(p/k) for p in piles])
        res = 0

        while l <= r:
            m = (l + r) // 2
            total_time = t(m)
            if h < total_time:
                l = m + 1
            elif total_time <= h:
                r = m - 1
                res = m
        return res
