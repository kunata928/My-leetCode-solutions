import heapq
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
            
      
        q = []
        for key in freq:
            heapq.heappush(q, (freq[key],key))
        
        res = []
        largest = heapq.nlargest(k, q, key = None)
        for l in largest:
            res.append(l[1])
        return res
            