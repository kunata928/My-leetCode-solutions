class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        maxS = nums[0]
        currS = 0
        for num in nums:
            currS = max(num, currS + num)
            maxS = max(currS, maxS)
        return maxS
                
            
        