'''
题目：打印对称的尺子。如n=1时，输出1；n=2时，输出1   1 2 1；n=3时，输出1   1 2 1    1 2 1 3 1 2 1；
      n=4时，输出1   1 2 1   1 2 1 3 1 2 1   1 2 1 3 1 4 1 3 1 2 1；……
思路：1、用for，找个空列表存入前半段数，后半段列表的前n-1个顺序反转一下即可, 这种还是有点慢，每一层还需要重新计算
2、f(n) = f(n-1) + 'n' + f(n-1)
'''

# 方法一
lst = []
n = 10
for i in range(n):
	if len(lst)==0:
		lst.append(1)
		continue
	lst.append(i+1)
	lst.append(1)

for i in range(n):
	if i==0:
		print([1])
	else:
		tmp = lst[:2*i]
		tmp.extend(lst[:2*i-1][::-1])
		print(tmp)



