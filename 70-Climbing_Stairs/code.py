class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        num1 = 1
        num2 = 2
        for i in range(n-2):
            tmp = num1
            num1 = num2
            num2 = tmp + num1        
        return num2