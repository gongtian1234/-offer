'''
题目：最长连续子串。给定一个只包含0和1的数组，找出只包含1的最长子串。
思路：
1、（自己的解法，不仅找到了最长子数组，也找到了它的位置）用while从头到尾遍历一遍，把一个包含1的子数组用元组记下其头索引和长度
2、只判断出最长子数组是多长，代码相对比我的简洁很多
'''

def find_longeststr(array):
    if len(array)==0:
        print('请不要输入空数组')
        return 
    lst, i = [], 0
    while i<len(array):
        if array[i]==1:
            j = 1  # 用来记录连续子串1的个数
            while 1:
                if i+j>=len(array):
                    lst.append((i,j))
                    break
                if array[i+j]==1:
                    j += 1
                else:
                    lst.append((i,j))
                    i = i + j
                    break
            if i+j>=len(array):
                break
        else:
            i += 1
    print(lst)
    # 从lst找出最长子串的下标索引和长度
    tmp_index, tmp_length = 0, 0
    for tmp in lst:
        if tmp[1]>tmp_length:
            (tmp_index, tmp_length) = tmp
    print(tmp_index,tmp_length)

#### 方法2 ####
def find_longeststr2(array):
    local = maxi = 0
    for i in array:
        local = local + 1 if i==1 else 0
        maxi = max(local, maxi)
    print(maxi)

find_longeststr([0,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1])
find_longeststr([0,1,1,1,0,1,1,0,1,1,1,1,0])
find_longeststr([])
print('方法2')
find_longeststr2([0,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1])
import os
os.system('pause')