# 不断取数组的第一行放入结果列表中，每放一次，就把剩下的数组逆时针旋转90度，以把最后一列变为新数组的第一行，然后接着把第一行pop出来放入结果列表中

class Solution:
    def printMatrix(self, arr):
        if arr is None or len(arr)<1: return arr
        rst = []
        rst.extend(arr[0])
        sum_nums = len(arr)*len(arr[0])
        while len(rst)<sum_nums:
            arr.pop(0)
            arr = self.rotate_reverse(arr)
            rst.extend(arr[0])
        return rst
       
    def rotate_reverse(self, arr):  # 逆时针旋转数组
        if len(arr)<1: return arr
        m, n = len(arr), len(arr[0])
        rotate_rst = [[0]*m for _ in range(n)]  # 因为是要顺时针输出，所以在这必须逆时针旋转剩下的数组，这样就把最后一列变味了第一行
        for i in range(m):
            for j in range(n):
                rotate_rst[j][i] = arr[i][len(n-1 - j)]
        return rotate_rst
