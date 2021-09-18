# 题目链接：https://leetcode-cn.com/problems/subdomain-visit-count/
# 示例：["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        m = len(cpdomains)
        if m<1:
            return []
        rst_dic = {}
        for i in range(m):
            tmp_num = int(cpdomains[i].split(' ')[0])
            tmp_str = cpdomains[i].split(' ')[1].split('.')
            for j in range(len(tmp_str)-1,-1,-1):
                if j==len(tmp_str)-1:
                    if tmp_str[j] not in rst_dic.keys():
                        rst_dic[tmp_str[j]] = tmp_num
                    else:
                        rst_dic[tmp_str[j]] += tmp_num
                else:
                    s = '.'.join(tmp_str[j:])
                    if s not in rst_dic.keys():
                        rst_dic[s] = tmp_num
                    else:
                        rst_dic[s] += tmp_num
        return ['{} {}'.format(j,i) for i,j in rst_dic.items()]
