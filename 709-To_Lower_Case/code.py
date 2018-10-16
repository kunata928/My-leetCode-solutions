class Solution:
     def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for i in range(26):
            str = str.replace(upper[i], lower[i])
        return str
        