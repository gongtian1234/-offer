# 参考网址：https://leetcode-cn.com/problems/decrease-elements-to-make-array-zigzag/solution/fen-qing-kuang-tao-lun-python3-by-smoon1989/
class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        m = len(nums)
        rst1,rst2 = 0,0
        for i in range(m):
            # 只要调整，使得全奇数或全偶数位置任一满足条件即可
            # 处理奇数位置，但是由于只能“减”，所以在讨论奇数位置时，假设的是所有奇数位置元素小于偶数位置元素
            if i%2==0:
                t1 = nums[i]-nums[i-1]+1 if i>0 and nums[i]>=nums[i-1] else 0
                t2 = nums[i]-nums[i+1]+1 if i<m-1 and nums[i]>=nums[i+1] else 0
                rst1 += max(t1,t2)
            # 处理偶数
            else:
                t1 = nums[i]-nums[i-1]+1 if nums[i]>=nums[i-1] else 0
                t2 = nums[i]-nums[i+1]+1 if i<m-1 and nums[i]>=nums[i+1] else 0
                rst2 += max(t1,t2)
        return min(rst1,rst2)
