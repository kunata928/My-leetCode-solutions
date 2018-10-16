class Solution(object):
    def transpose(self,A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        n,L=len(A),len(A[0])
        newmatrix=[[0]*n for i in range(L)]
        for i in range(n):
            for j in range(L):
                newmatrix[j][i]=A[i][j]
        return newmatrix