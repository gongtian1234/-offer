'''
题目一：翻转单词顺序。输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。例如，输入字符串
"I am a student."，则输出"student. a am I"

思路：
先切分开，翻转后再用空格链接回去

题目二：左旋转字符串。字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。例如，输入字符串'abcdefg'和数字2，该函数将返回左旋转两位
得到的结果'cdefgab'

思路：将前面的n个字符串移动到后面即可/
'''
class Solution1:
    def reverseSentence(self, sentence):
        if sentence is None:
            return
        return (' ').join(sentence.split(' ')[::-1])

class Solution2:
    def leftRotateString(self, chars, n):
        if chars is None:
            return
        charsLen = len(chars)
        if charsLen<n:
            n = n%charsLen
        return chars[n:]+chars[:n]

if __name__ == '__main__':
    s1 = Solution1()
    print(s1.reverseSentence('I am a student, but I will graduate after ten months.'))
    print(s1.reverseSentence(None))

    s2 = Solution2()
    print(s2.leftRotateString('acsadad', 8))

