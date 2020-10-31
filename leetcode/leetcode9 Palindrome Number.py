class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 方法一：转换为字符串，然后颠倒字符串再比对
        if x<0:
            return False
        else:
            if str(x)==str(x)[::-1]:
                return True
            else:
                return False
        # 方法二：
        # if x<0: return False
        # nums = []
        # while x>0:
        #     nums.append(x%10)
        #     x = x//10
        # for i in range(len(nums)//2):
        #     if nums[i]!=nums[-i-1]:
        #         return False
        # return True
