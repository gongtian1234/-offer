# test67：把字符串转换为数字
# 限制数字的范围[-2^32, 2^32-1]，超过范围则返回左或右区间值；首字符不为'+'、'-'、' '时，直接返回0；
# 当首次遇到字母时直接返回当前已经得到的数
# 思路：借助三个辅助变量用来记住正负号、当前的数字、for循环遍历开始的位置，res=10*res+(ord(strs[i])-ord('0'))

def strToInt(strs):
    strs = strs.strip()  # 先去除首尾的空格
    if not strs:
        return 0
    res, i, sign = 0, 1, 1
    int_max, int_min, bndry = 2**31-1, -2**31, 2**31//10
    if strs[0]=='-':
        sign = -1
    elif strs[0]!='+':
        i = 0
    for chari in strs[i:]:
        if chari>'9' or chari<'0':
            break
        if res>int_max or (res==int_max and chari>'7'):
            return int_max if sign==1 else int_min
        res = 10*res + (ord(chari)-ord('0'))
    return sign*res
