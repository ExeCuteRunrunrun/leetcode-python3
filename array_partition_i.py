class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        summ = 0
        i = 0
        while i <= len(nums)-1:
            summ += nums[i]
            i += 2
        return summ
