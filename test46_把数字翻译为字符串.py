'''
题目：给定一个数字，我们按照如下规则把它翻译为字符串："0"翻译为"a"，"1"翻译为"b"，"2"翻译为"c"，……，"25"翻译为"z"。一个数字可能有多个翻译。
例如，"12258"有五种不同的翻译，分别是"bccfz"、"bwfi"、"bczi"、"mcfi"、"mzi"。写一个函数，计算一个数字有多少种不同的翻译。

思路：
采用递归的思路, 从后往前或从前往后，依次判断一位与两位（两位数必须小于26才行），有点类似于斐波那契数列递归的方法f(n)=f(n-1)+f(n-2)

6    
5               25 
2       12      1  11
1 11    1       1
1
'''
def getTranslateCount(number):
    if number is None or number<0:
        return
    numberStr = str(number)
    numLen = len(numberStr)
    if numLen==1:
        return 1
    if numLen==2 and number<26:
        return 2
    # print('int(numberStr[:-1]) is ',int(numberStr[:-1]))
    yiwei = getTranslateCount(int(numberStr[:-1]))
    if int(numberStr[-2:])<26:
        # print('int(numberStr[:-2]) is',int(numberStr[:-2]))
        liangwei = getTranslateCount(int(numberStr[:-2]))
    else:
        liangwei = 0
    return yiwei + liangwei

if __name__ == '__main__':
    print(getTranslateCount(456))
    print(getTranslateCount(None))
