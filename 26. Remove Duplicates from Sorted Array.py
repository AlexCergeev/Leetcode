class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i, _ in enumerate(nums):
            if nums[i] == nums[j]:
                continue
            else:
                j += 1
                nums[j] = nums[i]
        return j+1
