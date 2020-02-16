'''
题目：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如一个输入长度为9的数组{1,2,3,2,2,2,5,4,2}, 由于数字2在数组中出现了5次，
超过数组长度的一半，因此输出2（注意：这个题主要考察的是时间复杂度和空间复杂度）

思路：
①创建一个字典，记录下每一个数字出现的次数，并判断其出现次数是否超过数组长度的一半（时间复杂度和空间复杂度都为O(n)）
②每次抵消两个前后两个不相同的数字，从而得到最后一个剩下的一个数字；再判别该数字的出现次数是否超过数组的一半（时间复杂度为O(n), 空间复杂度为O(1))）
'''

def moreThanHalfNum(nums):
	tmp = 0
	tmpLength = 0
	for num in nums:
		if tmpLength==0:
			tmp = num
			tmpLength = 1
		else:
			if num!=tmp:
				tmpLength -= 1
			else:
				tmpLength += 1
	if tmpLength==0:
		return None
	else:
		# print('最后剩下的数字为',tmp)
		tmpLength = 0
		for num in nums:
			if num==tmp:
				tmpLength += 1
			# print('此时统计的出现次数为',tmpLength)
			if tmpLength>(len(nums)>>1):
				return tmp
	return None

print(moreThanHalfNum((1,2,3,2,2,2,5,4,2)))    # 结果为2
print(moreThanHalfNum((1,1,2,2,3,3,3,3)))      # 结果为None，因为3的出现次数只是一半4，并没有超过4

