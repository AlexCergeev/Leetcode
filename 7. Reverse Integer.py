class Solution:
    def reverse(self, x: int) -> int:
        flag = 0
        if x < 0:
            flag = 1
            x = -x
        res = 0
        while x:
            res = res*10 + x % 10
            x //= 10
        result = -int(res) if flag else int(res)
        if (result < -2**31) or (result > (2**31 - 1)): return 0
        return result