# 参考链接：https://leetcode-cn.com/problems/matchsticks-to-square/solution/dfsjian-yi-pythonshi-xian-by-azad-u/
# 深度优先搜索 + 遍历每一个nums的元素
class Solution:
    def dfs(self,nums,target,pos):
        if pos==len(nums):
            return True
        for i in range(4):
            if nums[pos]<=target[i]:
                target[i] -= nums[pos]
                if self.dfs(nums,target,pos+1):
                    return True
                target[i] += nums[pos]
        return False

    def makesquare(self, nums):
        if sum(nums)%4!=0 or len(nums)<4:
            return False
        bianchang = sum(nums)/4
        target = [bianchang]*4
        return self.dfs(nums, target, 0)
        
