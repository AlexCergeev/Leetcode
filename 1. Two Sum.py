class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, item in enumerate(nums):
            remaining = target - item
            if remaining in seen:
                return [seen[remaining], i]
            seen[item] = i
