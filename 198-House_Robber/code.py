class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        res1 = 0
        res2 = 0
        i = 0
        for i in range(len(nums)):
            tmp = res1
            res1 = res2 + nums[i]
            res2 = max(tmp, res2)
        return max(res1,res2)