# 题目路径：https://leetcode-cn.com/problems/house-robber/
# 思路1：递归的方式
class Solution:
    def rob(self, nums: List[int]) -> int:
        m = len(nums)
        if m<1:
            return 
        elif m==1 or m==2:
            return max(nums)
        return max(nums[0]+self.rob(nums[2:]), nums[1]+self.rob(nums[3:]))

# 思路2：动态规划的方法
# https://leetcode-cn.com/problems/house-robber/solution/198-da-jia-jie-she-by-dine-1d2y/
class Solution:
    def rob(self, nums: List[int]) -> int:
        m = len(nums)
        if m<1:
            return 
        elif m==1 or m==2:
            return max(nums)
        dp = [0]*m
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        for i in range(2,m):
            dp[i] = max(dp[i-1],nums[i]+dp[i-2])
        return max(dp[-2:])
