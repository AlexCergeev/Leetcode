class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in nums_set:
                lenth = 0
                while (n + lenth) in nums_set:
                    lenth += 1
                longest = max(lenth, longest)
        return longest
