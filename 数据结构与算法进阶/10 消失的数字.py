'''
题目：找到数组中消失（没有出现）的数。给定一个长度为n的数组，里面数字的范围为[1,n]，有的数字出现了
      多次，有的一次也没有出现，找到没有出现的数字。要求：不能占用其他的空间，时间复杂度不鞥超过O(n)
思路：既然要求不能占用新的空间，那就只能修改原来数组，从而标记[1,n]中那个数没有出现，出现的则将这个数
      对应的索引上的数字记为负数，那么最后哪个索引位置的数字为正就说明该索引（即该数字）没有出现
'''

def findDisapperedNum(array):
    for i in range(len(array)):
        array[abs(array[i])-1] = -abs(array[abs(array[i])-1])
    return [i+1 for i in range(len(array)) if array[i]>0]

print(findDisapperedNum([1,2,3,3,5,6]))
print(findDisapperedNum([10,3,3,4,6,6,9,8,9,10]))