'''
题目一：字符串中第一个只出现一次的字符。在字符串中找出第一个只出现一次的字符。如输入"abaccdeff"，则输出'b'

思路：
①拿第i个字符分别与其后面的字符串比较，如果其后面没有出现相同的，则输出，否则继续比较下一个字符。时间复杂度为O(n)
②用一个字典来统计出现的次数，用一个列表记录字典中的键先后的出现次数，最后通过列表记录下的键，寻找字典中值为1的键

题目二：字符流中第一个只出现一次的字符。写一个函数，找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个
只出现一次的字符是"g"；当从该字符流中读出前6个字符"google"时，第一个只出现一次的字符是"l"

思路：
可以根据题目一的思路改一下即可，每输入一个数据流字符串，都判断一下当前第一个出现的子字符串，为了避免每次重复计算，可以将字典和列表定义在
类下的init中
'''

def firstNotRepeatingChar(s):
    if s is None or len(s)==0:
        return 
    tmpDict = {}
    tmpList = []
    for i in s:
        if i not in tmpDict.keys():
            tmpDict[i] = 1
            tmpList.append(i)
        else:
            tmpDict[i] += 1
    for i in tmpList:
        if tmpDict[i]==1:
            return i
    return 

if __name__ == '__main__':
    print(firstNotRepeatingChar('habaccdeffk'))