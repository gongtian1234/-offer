'''
题目：数字以012345678910111213141516……的格式序列化到一个字符序列中，在这个序列中，第五位（从0开始计数）是5，第十三位是1，第十九位是4等。
写一个函数，求任意n位对应的数字。

思路：
①枚举法，从第0位开始遍历。一直找到第k位
②从1开始，个位数（只有一位的数字）有九个，占位9个；两位数有90个，占位90*2个；三位数有900个，占位900*3个；以此类推，如果要找的第
k位大于占位的累加和，则再增加一个位数，看目标数字是否在是这个位数，如果是则查找这个数，不是则再增加一个位数

'''

# 第1000位
# 1-9：9*1
# 10-99：90*2=10*9*2
# 100-999：900*3=100*9*3
# 1000-9999：9000*4=1000*9*4
# 9+180+2700
def digitAtIndex(index):
    if index<0:
        return
    if index==0:
        return 0
    weishu = 1
    tmpIndex = index-1    # 减1是因为targetNum中10的次方，在位数为1时，会多加一个1
    while 9*10**(weishu-1)*weishu<tmpIndex:
        tmpIndex -= 9*10**(weishu-1)*weishu
        weishu += 1
    targetNum = (tmpIndex // weishu) + 10**(weishu-1)
    diJiWei = tmpIndex%weishu
    return str(targetNum)[diJiWei]

print(digitAtIndex(9))