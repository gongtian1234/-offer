# 最长的连续重复子串，如输入cdecdecdeabcdabcd，返回abcdabcd
## 关键有两点：①最长的；②连续重复
## 最快时间复杂度为O(n^2),需要借助四个辅助变量来记录最终/临时的最长子串及其重复次数

def maxRepeat(strs):
    if strs is None or len(strs)<1: return
    length = len(strs)
    repeat_time, repeat_str = 1, ''
    for i in range(length):
        for j in range(i+1,length):
            if strs[i]!=strs[j]: continue
            else:
                tmp_repeat_time, tmp_repeat_str = 1, ''
                single_length = j-i
                while j+single_length<=length and single_length>=len(repeat_str):
                    if strs[i:j]==strs[j:j+single_length]:
                        tmp_repeat_time += 1
                        tmp_repeat_str = strs[i:j]
                        i = j
                        j = j+single_length
                    else:
                        break
                if len(repeat_str)<len(tmp_repeat_str) or (len(repeat_str)==len(tmp_repeat_str) and repeat_time<tmp_repeat_time):
                    repeat_time, repeat_str = tmp_repeat_time, tmp_repeat_str
    return repeat_time * repeat_str
    
