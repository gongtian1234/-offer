# 题目路径：https://leetcode-cn.com/problems/house-robber-ii/
class Solution:
    def solution(self,nums):
        m = len(nums)
        if m==1:
            return nums[0]
        elif m==2:
            return max(nums)
        dp = [0]*m
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        for i in range(2,m):
            dp[i] = max(dp[i-1],nums[i]+dp[i-2])
        return max(dp[-2:])

    def rob(self, nums: List[int]) -> int:
        m = len(nums)
        if m==1:
            return nums[0]
        return max(self.solution(nums[1:]),self.solution(nums[:-1]))
