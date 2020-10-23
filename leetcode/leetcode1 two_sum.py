class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums is None or len(nums)<1:
            return
        length = len(nums)
        sotted_id = sorted(range(len(nums)), key=lambda k:nums[k])
        # return sotted_id
        nums = sorted(nums)
        cur1, cur2 = 0, len(nums)-1
        while cur1<cur2:
            if nums[cur1]+nums[cur2]<target:
                cur1+=1
            elif nums[cur1]+nums[cur2]>target:
                cur2 -= 1
            else:
                return [sotted_id[cur1], sotted_id[cur2]]
        return None
