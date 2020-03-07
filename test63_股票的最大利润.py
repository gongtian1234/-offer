'''
题目：假设把某股票的价格按照时间先后顺序存储在数组里，请问买卖该股票一次可能获得的最大利润是多少？例如，一只股票在某些时间节点的价格为
{9,11,8,5,7,12,16,14}。如果我们能在价格为5的时候买入并在价格为16时卖出，则能收获的最大利润是11

思路：
（实际上是找数组的最大差值）
'''
def maxDiff(numbers, mairuPrice):
    if numbers is None or len(numbers)==0 or mairuPrice<0:
        return 
    tmpMax = None
    maxDiffVal = None
    for i in range(len(numbers)):
        if tmpMax is None and maxDiffVal is None:
            tmpMax = numbers[i]
            maxDiffVal = numbers[i] - mairuPrice
        else:
            if numbers[i]>tmpMax:
                tmpMax = numbers[i]
                maxDiffVal = numbers[i] - mairuPrice
    return maxDiffVal

if __name__ == '__main__':
    print(maxDiff((9,11,8,5,7,12,16,16),5))

