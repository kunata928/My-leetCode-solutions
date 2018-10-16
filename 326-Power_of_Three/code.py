class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if not n: return False
        
        while n!= 1:
            if n % 3 != 0:
                return False
            n //= 3
        return True