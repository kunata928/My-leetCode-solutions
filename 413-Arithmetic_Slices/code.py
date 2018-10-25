class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        arr = []
        tmp = 1
        for i in range(len(A)-1):
            arr.append(A[i+1] - A[i])
        for j in range(len(arr)-1):
            if arr[j] == arr[j+1]:
                tmp += 1
            else:
                res += tmp*(tmp-1)/2
                tmp = 1
        res += tmp*(tmp-1)/2
        return int(res)