# 计算质数。给一个数n，返回它里面的所有质数的个数；如17，它的质数个数为7（包含17），则返回7。

def solution(num):
	count = 0
	if num<2:
		return 
	bool_array = [1 for i in range(num+1)] # 创建一个全为ture的数组 【考虑到时间复杂度，true全改为1，false改为0】
	bool_array[0], bool_array[1] = 0, 0                   # 因为0和1不是质数
	for tmp in range(2, num+1):
		if bool_array[tmp]==0:            # 如果bool数组的第tmp个位置已经是false，说明它的倍数已经处理过了，直接进入下一个
			continue
		beishu = 2                            # 用tmp这个数乘以倍数，得到的结果如果小于num，则将bool数组对应的位置转为false
		# print('当前判断的数字为：', tmp)
		while 1:
			if tmp*beishu>num:
				break
			if bool_array[tmp*beishu]==0: # 如果对应位置已经是false了，直接跳过，进入下一次
				beishu += 1                   # 要不然，在进入循环还是上一个值，会进入死循环
				continue
			bool_array[tmp*beishu] = 0
			beishu += 1

	count = sum(bool_array)

	return count

str_num = input('请输入一个大于1的整数：')
try:
	num = int(str_num)
	print('{}以内共有{}个质数'.format(str_num, solution(num)))
except:
	print('输入的数字不合规')
