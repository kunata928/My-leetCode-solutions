class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        if not A:
            return []
        for a in A:
            if not a % 2:
                res.insert(0, a)
            else: 
                res.append(a)
        return res