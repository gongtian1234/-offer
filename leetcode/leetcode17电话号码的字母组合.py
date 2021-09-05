# 题目链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict_info = {'2':list('abc'),
            '3':list('def'),
            '4':list('ghi'),
            '5':list('jkl'),
            '6':list('mno'),
            '7':list('pqrs'),
            '8':list('tuv'),
            '9':list('wxyz')}
        length = len(digits)
        if length < 1:
            return []
        rst = ['']
        for num_i in list(digits):
            rst = [i+j for i in rst for j in dict_info[num_i]]
        return rst
