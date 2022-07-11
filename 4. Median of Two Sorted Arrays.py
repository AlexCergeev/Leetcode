class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # TO DO merge two lists
        nums = sorted(nums1 + nums2)

        # TO DO  find median
        nums_len = len(nums)
        if nums_len % 2 == 0:
            return sum(nums[nums_len // 2 - 1:nums_len // 2 + 1]) / 2
        else:
            return nums[nums_len // 2]