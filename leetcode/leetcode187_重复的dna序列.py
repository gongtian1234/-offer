# 题目地址：https://leetcode-cn.com/problems/repeated-dna-sequences/
# 思路1：如果直接使用for循环append的方式，可以解题，但是无法通过时间复杂度
# 思路2：借用两个set()，可以通过时间复杂度
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        tmp = set()
        rst = set()
        for i in range(len(s)-9):
            tmp_str = s[i:i+10]
            if tmp_str not in tmp:
                tmp.add(tmp_str)
            elif tmp_str not in rst:
                rst.add(tmp_str)
        return list(rst)
