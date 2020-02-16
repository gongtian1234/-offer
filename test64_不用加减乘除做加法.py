'''
题目：写一个函数，求两个整数之和，要求在函数体内不得使用+-*/四则运算符号

思路：
进行位运算，进行按位与、异或运算
将十进制数转换为二进制，第一步，先进行两者间先进行按位与运算，如果结果为0，那么二者再进行的异或结果转换为十进制就是最终结果；
第二步，如果按位与结果不为0，说明有地方需要进一位，对其右补一位0并记为x(左移1位)，原来的两者间进行异或操作得到y；第三步，将x与y重复前面的步骤
'''

def add(m,n):
	assert type(m) is int 
	assert type(n) is int

	t1, t2 = m, n
	rst_yu = m & n
	rst_yihuo = m ^ n
	while rst_yu!=0:
		rst_yu = t1 & t2
		# rst_yu = rst_yu<<1   # 左移一位相当于在右边补0
		rst_yihuo = t1 ^ t2
		t1,t2 = rst_yu<<1, rst_yihuo
	return rst_yihuo

print(add(-58,-21))

