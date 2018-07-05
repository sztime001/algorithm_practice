class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        n = 1
        count = 0
        while n < N:
            if N%n == 0:
                count += 1
            n += 2

        n = 1
        while n < (N-n)/2:
            if (N*1.0/n-1)%2 == 0:
                count += 1
            n += 1
        return count

print(Solution().consecutiveNumbersSum(5))
print(Solution().consecutiveNumbersSum(9))
print(Solution().consecutiveNumbersSum(15))