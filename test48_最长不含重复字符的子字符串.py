'''
题目：请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度，假设字符串中只包含"a"~"z"的字符。例如，在字符串
'arabcacfr'中，最长的不含重复字符的子字符串为acfr，长度为4

思路：
①先找出所有的子字符串，再去判断子字符串是否重复，去掉重复的，再找到最长的子字符串，时间效率为O(n^3)
②遍历整个字符串，记录下当前无重复的最长子字符串，如果发现字符串i已经在记录的最长子字符串中，那么记录从字符串i第一次出现的下一个位置开始重新开始
③动态规划。（动态规划的解法没大看懂）
'''
def longestSubstringWithoutDuplication(s):
    print(len(s))
    if s is None or len(s)==0:
        return 0
    tmp = ''
    maxLen = 0
    for i in s:
        if i not in tmp:
            tmp += i
            maxLen = max(maxLen, len(tmp))
        else:
            tmp += i
            tmp = tmp[tmp.index(i)+1:]
    return maxLen, tmp

if __name__ == '__main__':
    print(longestSubstringWithoutDuplication('asdfghnsa'))
