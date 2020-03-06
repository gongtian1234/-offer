'''
题目：从扑克牌中随机抽5张牌，判断是不是一个顺子，即这五张牌是不是连续的，A为1，J为11，Q为12，K为13，而大小王可以看作任意数字。

思路：
大小王可以看成是任意数字，假设为0。先对数组进行排序，然后统计0的个数，再统计连续数字出现间隔的个数，如果0的个数大于等于出现间隔的个数，
则可以认为是连续的；否则，认为是不连续的
'''

def isContinuous(numbers):
    if numbers is None or len(numbers)!=5:
        return False
    zerosCount = 0
    jiangeCount = 0
    numbers.sort()
    for i in numbers:
        if i==0:
            zerosCount += 1
    if zerosCount>2:                          # 0的个数最大为2，因为大小王只有两个
        return False
    for i in range(1+zerosCount,5):  # 如果出现0，那么0不进行统计，直接跳过 
        if numbers[i]-numbers[i-1]>1:
            jiangeCount += 1
    if zerosCount>=jiangeCount:
        return True
    return False

if __name__ == '__main__':
    print(isContinuous([10,0,1,13,0]))

