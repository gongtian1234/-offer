'''
题目一：数字在排序数组中出现的次数。统计一个数字在排序数组中出现的次数。例如，输入排序数组{1,2,3,3,3,3,4,5}和数字3，由于3出现了4次，所以输出4

思路：
①直接从头遍历，但是这种方法的时间复杂度为O(n)
②根据二分查找的思路，先找到数字k首次出现的位置，再分别从前半段后半段找出k第一次和最后一次出现的位置(索引)，从而统计出k出现的次数,这种方法的时
间复杂度为O(logn)。编写两个函数分别寻找k首次出现和左后依次出现的索引位置，寻找k首次出现的位置，需要用到递归，为了能够保证找到位置，所以每次需
要传入原数组，用两个辅助变量firstIndex, lastIndex来表示每次的变动，这样就能准确找到首次出现的索引位置

题目二：0~n-1中缺失的数字。一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字范围都在0~n-1之内。在范围0~n-1内的n个数字中，有且只
有一个数字不再该数组中，请找出这个数字。

思路：
①从头遍历，找到缺失值，时间复杂度为O(n)
②采用二分查找的方法，时间复杂度可以为O(logn)

'''
def getNumberOfK(data, k):
    if len(data)==0 or k<data[0] or k>data[-1]:
        return 0
    def findFisrtK(data, firstIndex, lastIndex):
        if firstIndex>lastIndex:
            return 
        midPos = int((firstIndex+lastIndex)/2)
        midVal = data[midPos]
        if midVal==k:
            if (midPos!=0 and data[midPos-1]!=k) or midPos==0:
                return midPos
            else:
                lastIndex = midPos-1
        elif midVal<k:
            firstIndex = midPos+1
        elif midVal>k:
            lastIndex = midPos-1
        return findFisrtK(data, firstIndex, lastIndex)

    def findLastK(data,firstIndex,lastIndex):
        if firstIndex>lastIndex:
            return
        midPos = int((firstIndex+lastIndex)/2)
        midVal = data[midPos]
        if midVal==k:
            if (midPos==0) or (midPos!=0 and data[midPos+1]!=k):
                return midPos
            else:
                firstIndex  = midPos+1
        elif midVal>k:
            lastIndex = midPos-1
        elif midVal<k:
            firstIndex = midPos+1
        return findLastK(data, firstIndex, lastIndex)

    first = findFisrtK(data, 0, len(data)-1)
    last = findLastK(data, 0, len(data)-1)

    if first>last:
        return 
    else:
        return last-first+1

def getMissingNumber(numbers):
    ''' numbers: 0,1,2,3,4,5,7 or 1 or 0,2'''
    if len(numbers)==0:
        return None
    if len(numbers)>1 and numbers[0]!=0:
        return 0
    def main(numbers, firstIndex, lastIndex):
        if firstIndex>lastIndex:
            return
        midPos = int((firstIndex+lastIndex)/2)

        if numbers[midPos+1]-1!=numbers[midPos] or numbers[midPos-1]+1!=numbers[midPos]:
            if numbers[midPos+1]-1!=numbers[midPos]:
                return midPos
            if numbers[midPos-1]+1!=numbers[midPos]:
                return midPos-1
        elif (midPos-firstIndex+1)==numbers[midPos]-numbers[firstIndex]+1:    # 左边不缺
            firstIndex = midPos+1
        elif (lastIndex-midPos+1)==numbers[lastIndex]-numbers[midPos]+1:    # 右边不缺
            lastIndex = midPos-1
        return main(numbers, firstIndex, lastIndex)
    preIndex = main(numbers, 0, len(numbers)-1)
    return numbers[preIndex]+1

if __name__ == '__main__':
    print(getNumberOfK([1,2,3,3,3,3,4,5],3))
    print(getNumberOfK([2,2,3,3],1))
    
    print(getMissingNumber([0,1,3,4,5,6,7]))