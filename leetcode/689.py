class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        l = len(nums)
        val_len = l-k+1

        vals = [0]*(val_len)
        vals[0] = sum(nums[0:k])
        for i in range(1,val_len):
            vals[i] = vals[i-1] - nums[i-1] + nums[i+k-1]

        left = [0]*l
        maxleft = 0
        for j in range(k,l-2*k+1):
            if vals[j-k]>maxleft:
                maxleft = vals[j-k]
                left[j] = j-k
            else:
                left[j] = left[j-1]

        right = [0]*l
        maxright = 0
        for j in range(l-2*k, k-1, -1):
            if vals[j+k]>maxright:
                maxright = vals[j+k]
                right[j] = j+k
            else:
                right[j] = right[j+1]

        summax = 0
        for j in range(k, l-2*k+1):
            if vals[left[j]]+vals[j]+vals[right[j]]>summax:
                summax = vals[left[j]]+vals[j]+vals[right[j]]
                pos = [left[j], j, right[j]]

        return pos

print(Solution().maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1],2))

print(Solution().maxSumOfThreeSubarrays([7,13,20,19,19,2,10,1,1,19],3))

print(Solution().maxSumOfThreeSubarrays([17,9,3,2,7,10,20,1,13,4,5,16,4,1,17,6,4,19,8,3],4))