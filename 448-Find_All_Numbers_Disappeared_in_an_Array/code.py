class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = list(set(range(1, len(nums)+1)) - set(nums))
        return res