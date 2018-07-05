class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        l = len(nums)
        left_vals = []
        left_indxs = []

        right_vals = []
        right_indexs = []
        
        mid_vals = []
        mid_indexs = []

    def _cal_max_val_and_index(subA, k, start_index):
        l = len(subA)
        dp_arr = [None]*(l-k+1)
        dp_index = [start_index+i for i in range(l-k+1)]
        dp_arr[0] = sum(subA[0:k])
        for i in range(1,l-k+1):
            dp_arr[i] = dp_arr[i-1]+subA[i+k-1]-subA[i-1]
        return dp_arr, dp_index
        

            
    
print(Solution().maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1],2))

print(Solution().maxSumOfThreeSubarrays([7,13,20,19,19,2,10,1,1,19],3))