# 计算质数。给一个数n，返回它里面的所有质数的个数；如17，它的质数个数为7（包含17），则返回7。

'''
思路：
1、1~n中的每一个数，都用其除以sqrt(n)以内的数，比如17，从1遍历到17，对于17个数中的每一个数都去除以是sqrt(n)以内的数，
   如5就去除以sqrt(5)以内的整数，来判断5是不是质数。缺点：时间复杂度较高，每一个数都需要遍历一次。
2、用空间换取时间，先找一个长度为n的bool数组，里面全设置为true，从2开始，判断2，是2的倍数(倍数从2开始，因为1倍数就是它自己)则全部赋值为false；然后再判断3；
   因为4被划掉了，所以下一个考虑5；接下来再考虑7，一直到bool数组的后面全部转换为false为止
'''
import time
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
			# print(bool_array)
			# print('当前{}的倍数为{}'.format(tmp, beishu))
			# print(1, end=' ')
			if tmp*beishu>num:
				break
			if bool_array[tmp*beishu]==0: # 如果对应位置已经是false了，直接跳过，进入下一次
				beishu += 1                   # 要不然，在进入循环还是上一个值，会进入死循环
				continue
			bool_array[tmp*beishu] = 0
			beishu += 1
			# time.sleep(0.01)
		# print(bool_array)

	count = sum(bool_array)
	# for bol in bool_array:
	# 	if bol:
	# 		count += 1

	return count

str_num = input('请输入一个大于1的整数：')
try:
	num = int(str_num)
	print('{}以内共有{}个质数'.format(str_num, solution(num)))
except:
	print('输入的数字不合规')
