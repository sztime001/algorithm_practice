class Solution:
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        f = 0
        sumf = 0
        for i in range(n):
            f += i * A[i]
            sumf += A[i]
        maxf = f
        rotf = f
        for i in range(n-1,0,-1):
            rotf = rotf + sumf - A[i]*n
            if maxf <rotf:
                maxf = rotf
            else:
                pass
        return maxf