'''
题目：最大数。给定一个数组，数组里有且只有一个最大数，判断这个数是否是其他数的两倍或更大，如果存在这个数，则返回其index，否则返回-1
注意：没有必要先找到最大的数，再去和每一个数进行比较，会增加时间复杂度；
      第二，如果直接用sort排序，再让第一大和第二大的数比较，代码够简洁，但是排序的时间复杂度为O(nlogn)
思路：(核心)遍历一次数组，找出最大和第二大的数，及第一大的数的索引，再去比较满足返回最大数的索引，不满足返回-1

'''

def largest_twice(array):
    maximum = sencond = indexm = 0
    for i in range(len(array)):
        if maximum<array[i]:
            sencond = maximum
            maximum = array[i]
            indexm = i
        elif sencond<array[i]:
            sencond = array[i]
    return indexm if maximum>sencond*2 else -1

print(largest_twice([0,1,2,3,4,15]))
print(largest_twice([0,0,0,0,1,0]))
