'''
题目：请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100"、"5e2"、"-123"、"3.1416"及"-1E-16"都表示数值，但
"12e"、"1a3.14"、"1.2.3"、"+-5"、"12e+5.4"都不是

思路：
表示数字的字符串遵循A[.[B]][e|EC]或.B[e|EC]，其中A和C都是整数（可以有正负号，也可以没有），而B只能是一个无符号整数
找三个辅助变量分别表示正负号、小数点、E/e是否出现或出现的位置是否合适。遍历整个字符串，每个字符进行判断, 正负号只能出现在整数部分的前
面或者是e/E的后面；小数点只能出现一次, 且在e/E的部分不能出现小数；e/E只能在数字的后面且其前面不能没有数字，且只能出现一次
'''

def isNumeric(chars):
    if chars is None:
        return
    hasSign, decimal, hasE = False, False, False
    for i in range(len(chars)):
        tmpChar = chars[i]
        # print('tmpChar is ',tmpChar)
        # 正负号只能出现在整数部分的前面或者是e/E的后面
        if tmpChar in ['+', '-']:
            if not hasSign and i>0 and chars[i-1] not in ['e', 'E']:
                return False
        # 小数点只能出现一次, 且在e/E的部分不能出现小数
        elif tmpChar=='.':
            if decimal or hasE:
                return False
            decimal = True
        # e/E只能在数字的后面且其前面不能没有数字，且只能出现一次
        elif tmpChar in ['e', 'E']:
            if hasE or i==0 or (i>0 and chars[i-1]=='.'):
                return False
            hasE = True
        else:
            if tmpChar<'0' or tmpChar>'9':
                return False
    return True

if __name__ == '__main__':
    print(isNumeric("+100"))
    print(isNumeric("12e+5.4"))

