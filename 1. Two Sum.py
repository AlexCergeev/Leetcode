class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevDiff = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevDiff.keys():
                return [prevDiff[diff], i]
            prevDiff[n] = i
        return 
