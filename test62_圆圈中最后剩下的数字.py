'''
题目：0,1,...,n-1这n个数字排成一个圆圈，从数字0开始每次从这个圆圈里删除第m个数字，求出这个圆圈里剩下的最后一个数字。如0,1,2,3,4这
      五个数字组成一个圆圈，从0开始每次删除第三个数字，则删除的前四个数字依次是2、0、4、1，因此最后剩下的数字是3

思路：
①依次遍历，从而找到剩下的最后一个数字，但是其时间复杂度为O(n^2)
②找规律，但是没搞明白，这种方法的时间复杂度为O(n)，空间复杂度为O(1)
'''

def LastRemainingSolution(n,m):
	if n<1 or m<1:
		return -1
	last = 0
	for i in range(2,n+1):
		last = (last+m)%i
	return last

if __name__=='__main__':
	print(LastRemainingSolution(5,3))
