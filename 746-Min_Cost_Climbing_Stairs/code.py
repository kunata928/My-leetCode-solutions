class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        res = [cost[0], cost[1]]

        for i in range(2, len(cost)):
            elem = cost[i] + min(res[i-1], res[i-2])
            res.append(elem)
        return min(res[len(cost)-1], res[len(cost)-2])