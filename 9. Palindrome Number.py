class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        number = x
        res = 0
        while number:
            res = res * 10 + number % 10
            number //= 10
        return res == x
