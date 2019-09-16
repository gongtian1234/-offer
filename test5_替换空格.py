'''
题目：
实现一个函数，把字符串的每一个空格都替换为"%20".
备注：遇到特殊字符的转换规则是将其转换为服务器可以识别的字符。转换规则是“%”后加上ASCII码的两位16进制的表示，如空格的ASCII码是32，十六进制为0x20，所以空格替换为%20；“#”的ASCII为35，十六进制为0x23，所以在URL中替换为“%23”
解法一：从头到尾遍历一次，遇空格转换并后移后面的字符，但这种时间复杂度为O(n^2)；解法二的时间复杂度仅为O(n)
解法二：找两个指针，一个指向原字符串的末尾，另一个指向移动后字符串的末尾，先遍历一遍，记下空格的位置，然后进行替换，此时每个字符串只移动一次，时间复杂度为O(n)
'''

def solution(strs, cls_cha=' '):
    '''稍加修改可以改成替换任意特殊字符的函数'''
    p1 = len(strs)-1    # 用来标记最后一个字符串的位置
    lst = []    # 用来存放原字符串中空格的下标
    
    j = 0
    for i in strs:
        if i ==cls_cha:
            lst.append(j)
        j += 1
    # print(lst)

    # 先占位
    strs += '00'*len(lst) 
    # print(strs) 

    for k in range(len(lst)):
        # k=1
        p2 = lst[-(k+1)]    # p2用来标记空格的位置，倒着标记
        strs = list(strs)

        strs[p2+1 + 2*(len(lst)-k) : p1+1 + 2*(len(lst)-k)] = strs[p2+1:p1+1]
        strs[p2 + 2*(len(lst)-(k+1)) : p2 + 2*(len(lst)-(k+1)) + 3] = '%20'
        p1 = lst[-(k+1)]-1
    return ''.join(strs)


strs = 'we are family we are family'    # 13
strs2 = '百度 搜索 空格 处理'
rst = solution(strs2)
print(rst)

# 总结：字符串不能直接进行修改，所以先转换为列表，处理完后再转为字符串

'''
解题思路：先考虑一般情况，再放入函数
p1 = len(strs)    
p2 = 0
lst = []    # 用来存放原字符串中空格的下标
j = 0
for i in strs:
    if i ==' ':
        lst.append(j)
    j += 1
print(lst)

# 先占位
strs += '00'*len(lst) 
print(strs) 

p2 = lst[-1]    # p2用来标记空格的位置，倒着标记
strs = list(strs)
print(strs)

strs[p2+1 + 2*len(lst): p1 + 2*len(lst)] = strs[p2+1 : p1]     # 后移倒数第一个空格后的字符串
strs[p2 + 2*(len(lst)-1) : p2 + 2*(len(lst)-1) + 3] = '%20'    # 替换第一个空格
p1 = lst[-1]-1    # 倒数第二个空格后末尾字符的位置
p2 = lst[-2]      # 倒数第二个空格的位置

print(strs)

strs[p2+1 + 2*(len(lst)-1): p1+1 + 2*(len(lst)-1)] = strs[p2+1 : p1+1]     # 后移倒数第二个空格后的字符串
# print(strs[p2+1 : p1+1])
strs[p2 + 2*(len(lst)-2) : p2 + 2*(len(lst)-2) + 3] = '%20'    # 替换第二个空格
strs = ''.join(strs)
print(strs)
'''