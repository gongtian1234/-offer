'''
题目：矩阵0变换。给定一个m*n的矩阵，如果有一个元素为0，则把该元素对应的行和列全部转换为0

思路：
【误区：遇到0直接就立马将其所在行与列都转变为0，结果会导致整个矩阵都变为0】
先定义两个列表来记录有0的行和列，通过遍历每一行去找0，如果遇到0则记录下其行号和列号，
然后再去将对应的行和列转为0
'''

def zeros(matrix):
	row_lst = []
	col_lst = []
	if len(matrix)==0 or len(matrix[0])==0:  # len([[], []]):2
		return 
	rows, cols = len(matrix), len(matrix[0])
	for i in range(rows):
		for j in range(cols):
			if matrix[i][j]==0:
				row_lst.append(i)
				col_lst.append(j)
	# 按照列表中的标号将其转换为0
	row_lst = set(row_lst)  # 【注意：此时row_lst与col_lst的length一定相等】
	col_lst = set(col_lst)
	if len(row_lst)==0:   
		return '该矩阵中没有0'
	#### 方法1 ####
	# 先将行对应的转为0
	# for i in row_lst:
	# 	matrix[i] = [0 for tmp in range(len(matrix[i]))]
	# # 再将列对应的转为0
	# for j in col_lst:
	# 	for i in range(len(matrix)):
	# 		matrix[i][j] = 0

	#### 方法2 ####
	# 这种方法是将行和列任意配成一对，来将对应的行和列转为0，转换完后再将其从对应的存储列表中删除，避免多次循环
	while 1:
		rowi = row_lst.pop()
		coli = col_lst.pop()
		matrix[rowi] = [0 for tmp in range(len(matrix[i]))]
		for i in range(len(matrix)):
			matrix[i][coli] = 0
		if len(row_lst)==0:
			break
	# 输出结果
	for i in range(len(matrix)):
		print(matrix[i])

zeros([[7,2,3,4,5,6],
	   [2,3,6,5,4,5],
	   [0,1,2,3,5,4],
	   [4,5,6,7,5,9],
	   [11,2,3,6,79,0]
	  ])
