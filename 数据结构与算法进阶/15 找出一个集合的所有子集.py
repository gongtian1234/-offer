'''
题目：（重要）找出一个集合的所有子集。打印出来即可。（leetcode上的：https://leetcode-cn.com/problems/subsets/）
思路：1、有n个数字的集合共有2^n个子集。（技巧）第一个为空集，选出集合的第一个元素放在已有的子集中，再选出第二个元素分别放入已有的
      子集中，依次遍历，就找到了所有的子集。如原集合为{3,2}，第一个子集为空集，接下来取出第一个元素3，放入所有已有子集中，形成
      新的子集，{} + 3 => {3}，现在所有的子集为{}、{3}，再取出2放入所有已有的子集中形成新的子集，形成了{2}、{3,2}，一共就有了4
      子集（这种解法是利用了python的特性）
      2、回溯法(非常重要，死记)。感觉有点绕，不太理解。
'''
def solution1(nums):
	tmp = [[]]
	for num in nums:
		for tmpi in tmp[:]:   # 如果不加上[:]就会陷入死循环, [:]是deepcopy的意思
			x = tmpi[:]
			x.append(num)
			tmp.append(x)
	return tmp
nums = ['a','b','d']
print(solution1(nums))

def solution2(nums):
	lst = []
	result = []
	subsets_recursive_helper(result, lst, nums, 0)
	return result
def subsets_recursive_helper(result, lst, nums, pos):
	result.append(lst[:])
	# print('result is ', result)
	for i in range(pos, len(nums)):
		lst.append(nums[i])
		# print('i, pos is ',(i,pos))
		# print('lst is', lst)
		subsets_recursive_helper(result, lst, nums, i+1)
		lst.pop()
		# print('now lst is', lst)
		# print()
print(solution2(['a','b','c']))