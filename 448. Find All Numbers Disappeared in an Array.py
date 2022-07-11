from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        i = 0
        while i < nums_len:
            pos = nums[i] - 1
            if nums[i] == nums[pos]:  # if el on current position, check next
                i += 1
            else:
                nums[i], nums[pos] = nums[pos], nums[i]

        res = []
        for i in range(1, nums_len + 1):
            if i != nums[i - 1]:
                res.append(i)
        return res