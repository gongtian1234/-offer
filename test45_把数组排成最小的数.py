'''
题目：输入一个正整数数组，把数组里面所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如，输入数组{3,32,321}，则打印出这
3个数字能排成的最小数字321323（321 32 3）

思路：
(有点类似于面试题38————字符串的排列，n个数字共有n!种排列，但是如果使用这种方法的话，还是很慢)
参考网址：https://blog.csdn.net/u010005281/article/details/80085476
使用了快排的思路，但是不太理解，和书上讲的那一长串有点不一样
'''

def strSort(numbers):
	if len(numbers)<=1:
		return numbers
	left = strSort([i for i in numbers[1:] if int(str(i)+str(numbers[0]))<int(str(numbers[0])+str(i))])
	right = strSort([i for i in numbers[1:] if int(str(i)+str(numbers[0]))>=int(str(numbers[0])+str(i))])
	return left + [numbers[0]] + right

print(strSort([3,32,321]))
print(strSort([456]))

def quickSort(numbers):
	if len(numbers)<2:
		return numbers
	left = quickSort([i for i in numbers if i<numbers[0]])
	right = quickSort([i for i in numbers if i>=numbers[0]])
	return left+[numbers[0]]+right