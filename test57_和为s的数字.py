'''
题目一：和为s的两个数字，输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得他们的和正好是s。如果有多对数字和胃s，输出任意一对即可。

思路：
找两个指针，一个指向头，一个指向尾，从而去找s，这样的时间复杂度为O(1)

题目二：和为s的连续正数序列。输入一个正数s，打印出所有和为s的连续正数序列（至少含有两个数）。例如，输入15，由于1+2+3+4+5=4+5+6=7+8=15，所以
打印出3个连续序列1~5、4~6和7~8

思路：
找两个指针，指向1和2，如果cur1到cur2的和小于targetSum，那么cur2加1；如果大于targetSum，则cur1加1；等于，则记录下来，cur2加1，循环判断直到没
有为止（终止条件：cur1的值小于(1+targetSum)/2时一直满足条件）
'''
class Solution1:
    def findNumsWithSum(self, numbers, targetSum):
        if len(numbers)<2:
            return None
        if targetSum<numbers[0]+numbers[1] or numbers[-1]+numbers[-2]<targetSum:
            return None
        cur1,cur2 = 0, len(numbers)-1
        while cur1<cur2:
            if numbers[cur1]+numbers[cur2]<targetSum:
                cur1 += 1 
            elif targetSum<numbers[cur1]+numbers[cur2]:
                cur2 -= 1
            elif numbers[cur1]+numbers[cur2]==targetSum:
                return numbers[cur1], numbers[cur2]

class Solution2:
    def findContinuousSequence(self,targetSum):
        if targetSum<3:
            return 
        cur1, cur2 = 1, 2
        curSum = cur1 + cur2    # 同来保存上一次的和，从而避免每次都从cur1加到cur2
        queue = []
        while cur1<(1+targetSum)/2:
            if curSum<targetSum:
                cur2 += 1
                curSum += cur2
            elif curSum>targetSum:
                if (curSum-cur1)>targetSum:
                    curSum -= cur1
                    cur1 += 1
                elif (curSum-cur1)<targetSum:
                    cur2 += 1
                    curSum += cur2
                else:
                    curSum -= cur1
                    cur1 += 1
            else:
                queue.append((cur1, cur2))
                cur2 += 1
                curSum += cur2
        return queue

if __name__ == '__main__':
    s1 = Solution1()
    print(s1.findNumsWithSum([1,2,3,4,5,6,7,8,8], 10))
    print(s1.findNumsWithSum([1],2))

    s2 = Solution2()
    print(s2.findContinuousSequence(9))