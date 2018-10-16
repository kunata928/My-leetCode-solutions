class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum = 0
        sett = set()
        
        while n != 1:
            while n != 0:
                sum += (n % 10) **2
                n //= 10
            if sum  not in sett:
                sett.add(sum)
            else: return False
            n = sum
            sum = 0
        
        return True
        