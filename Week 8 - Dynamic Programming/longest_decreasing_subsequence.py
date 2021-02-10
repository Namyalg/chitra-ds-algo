class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)
        
       This is strictly decreasing , change to equal to 
