class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s)<1:
            return 0
        rst = 0
        longest_s = ''
        for i in range(len(s)):
            if s[i] not in longest_s:
                longest_s += s[i]
                rst = max(rst, len(longest_s))
            else:
                longest_s += s[i]
                for j in range(len(longest_s)):
                    if longest_s[j]==s[i]:
                        first_loc = j
                        break
                longest_s = longest_s[first_loc+1:]
                rst = max(rst, len(longest_s))
        return rst
