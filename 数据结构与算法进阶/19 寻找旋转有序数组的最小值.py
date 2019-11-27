'''
题目：给定一个旋转的有序数组，找到其最小值的位置（剑指offer上的那个）
思路：
1、先对数组排序，在返回第0个元素，虽然简单，但是时间复杂度为O(n)
2、用二分搜索，时间复杂度为log(n)

题目二：在旋转的有序数组中寻找某个值。【有难度】
思路：这个题目是有难度的，需要分类讨论的情况比较多，本人也是在不断试错的情况下解出来的，但明显没有答案优秀


'''
def ordersearch(array):
    cur = 0
    if len(array)==1:return 0
    while array[cur]>=array[cur+1]:
        cur += 1
    return cur      

def find_minval(array):
    if len(array)==0:return -1
    left, right = 0, len(array)-1
    mid = (left+right)//2
    if array[left]<array[right]:return left  # 特殊情况1：移动0个数，即没有移动
    if array[left]==array[right] and array[mid]==array[right]: return ordersearch(array)   # 特殊情况2：1 0 1 1 1 / 1 1 1 0 1，只能顺序查找
    while right-left>1:
        if array[left]>=array[mid]:
            right = mid
            mid = (left + right) // 2
        elif array[left]<array[mid]:
            left = mid
            mid = (left + right) //2
    return right

print(find_minval([6,7,8,9,10,1]))
print(find_minval([1,1,1,0,1]))

def find_value_in_rotated_array(array,item):
    if len(array)==0: return -1
    cur1, cur2 = 0, len(array)-1
    mid = (cur1+cur2)//2
    while cur2-cur1>1:
        if array[mid]==item:return mid

        '''
        # 这是正规的解题思路
        mid = (cur1 + cur2)//2
        if array[cur1]<array[mid]:
            if array[cur1]<=item and item<array[mid]:
                cur2 = mid
            else:
                cur1 = mid
        else:
            if array[cur2]>=item and item>array[mid]:
                cur1 = mid
            else:
                cur2 = mid
        '''

        if array[mid]>item and array[mid]<array[cur2]:   # 6 7 1 2 3 4 5 ==》1
            print('1:',mid)
            cur2 = mid
            mid = (cur1+cur2)//2
        if array[mid]>item and array[cur2]>item:   # 6 7 8 9 10 1 2 ==》1
            print('2:',mid)
            cur1 = mid
            mid = (cur1+cur2)//2
        elif array[mid]>item and array[cur2]<item:   # 6 7 8 9 10 1 2 ==》6
            print('3:',mid)
            cur2 = mid
            mid = (cur1+cur2)//2
        else:
            print('4:',mid)
            cur1 = mid
            mid = (cur1+cur2)//2
        if array[mid]<item:
            print('5:',mid)
            cur1 = mid
            mid = (cur1+cur2)//2
    if array[cur1]==item: return cur1
    if array[cur2]==item: return cur2
    return -2   # 没有找到返回-2
print(find_value_in_rotated_array([6,7,1,2,3,4,5],1))
print(find_value_in_rotated_array([6,7,8,9,10,1,2],6))
print(find_value_in_rotated_array([6,7,8,9,10,1,2],2))
