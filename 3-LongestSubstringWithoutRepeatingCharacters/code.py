class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxx = tmp = 0
        queue = []
        for ss in s:
            if ss not in queue:
                tmp += 1
            else:
                if tmp > maxx:
                    maxx = tmp
                while queue[0] != ss:          
                    del queue[0]
                    tmp -=1
                del queue[0]
            queue.append(ss)    
        if tmp > maxx:
            return tmp
        return maxx
                
